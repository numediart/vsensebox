# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import numpy as np

from vsensebox.utils.commontools import to_xywh
from vsensebox.utils.logtools import ignore_this_logger

ignore_this_logger("tensorflow")
ignore_this_logger("preprocessing")
ignore_this_logger("nn_matching")
ignore_this_logger("generate_detections")
ignore_this_logger("detection")
ignore_this_logger("tracker")

from .utils import preprocessing
from .utils import nn_matching
from .utils import generate_detections as gdet
from .utils.detection import Detection as DSDetection
from .utils.tracker import Tracker as DSTracker
from .utils.box_matching import matchDetTrkByXYXY


class DeepSORT(object):

    """Class used as a custom layer or interface for interacting with DeepSORT tracker.
    """

    def __init__(self, cfg):
        """Initialize according to the given :obj:`cfg` and :obj:`auto_load`.

        Parameters
        ----------
        cfg : TCFG_DeepSORT
            A :class:`TCFG_DeepSORT` object which manages the configurations of tracker DeepSORT.
        """
        self.nms_max_overlap = cfg.nms_max_overlap
        self.encoder = gdet.create_box_encoder(cfg.model_file, batch_size=cfg.batch_size)
        self.metric = nn_matching.NearestNeighborDistanceMetric(
            "cosine", cfg.max_cosine_distance,cfg.nn_budget
        )
        self.tracker = DSTracker(self.metric)


    def update(self, boxes_xyxy, boxes_confs, boxes_cls=None, img=None):
        """Update the tracker and return a track list.

        Parameters
        ----------
        boxes_xyxy : list[[X1, Y1, X2, Y2], ...]
            A list of boxes; for example, [[X1, Y1, X2, Y2], [X1, Y1, X2, Y2], ...].
        boxes_confs : list[float, ...]
            A list of detection confidences corresponding to boxes_xyxy.
        boxes_cls : list[int, ...], default=None
            A list of detection class corresponding to boxes_xyxy.
        img : any, default=None
            A :obj:`Mat` like object.

        Returns
        -------
        list[[X1, Y1, X2, Y2], ...]
            A list of boxes; for example, [[X1, Y1, X2, Y2], [X1, Y1, X2, Y2], ...].
        list[int]
            A list of IDs corresponding to the the list of boxes.
        """

        dconfidences = boxes_confs
        dclasses = boxes_cls
        dboxes = [to_xywh(b) for b in boxes_xyxy]
        dfeatures = self.encoder(img, dboxes)
        detections = [DSDetection(dbox, dconfidence, dclass, dfeature) 
                        for dbox, dconfidence, dclass, dfeature in 
                        zip(dboxes, dconfidences, dclasses, dfeatures)]
        dboxes = np.array([d.tlwh for d in detections])
        scores = np.array([d.confidence for d in detections])
        indices = preprocessing.non_max_suppression(dboxes, self.nms_max_overlap, scores)
        detections = [detections[i] for i in indices]

        self.tracker.predict()
        self.tracker.update(detections)

        boxes_xyxy_trk = []
        ids_trk = []
        for t in self.tracker.tracks:
            if not t.is_confirmed() or t.time_since_update > 1:
                continue
            bxyxy = t.to_tlbr().tolist()
            boxes_xyxy_trk.append(bxyxy)
            ids_trk.append(int(t.track_id))
        ids = matchDetTrkByXYXY(boxes_xyxy, boxes_xyxy_trk, ids_trk)

        return boxes_xyxy, ids
