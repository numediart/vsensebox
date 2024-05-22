# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import numpy as np
from vsensebox.utils.logtools import ignore_this_logger

ignore_this_logger("sort")
from .utils.sort import Sort as ST
from .utils.box_matching import matchDetTrkByXYXYForSORT


class SORT(object):

    """Class used as a custom layer or interface for interacting with SORT tracker.
    """

    def __init__(self, cfg):
        """Initialize according to the given :obj:`cfg` and :obj:`auto_load`.

        Parameters
        ----------
        cfg : TCFG_SORT
          A :class:`TCFG_SORT` object which manages the configurations of tracker SORT.
        """
        self.st = ST(cfg.max_age, cfg.min_hits, cfg.iou_threshold)

    def update(self, boxes_xyxy, boxes_conf, boxes_cls=None, img=None):
        """Update the tracker and return a track list.

        Parameters
        ----------
        boxes_xyxy : list[[X1, Y1, X2, Y2], ...]
          A list of boxes; for example, [[X1, Y1, X2, Y2], [X1, Y1, X2, Y2], ...].
        boxes_conf : list[float, ...]
          A list of detection confidence corresponding to boxes_xyxy.
        boxes_cls : list[int, ...], default=None
          Being consistent with other trackers, will be ignored.
        img : any, default=None
          Being consistent with other trackers, will be ignored.

        Returns
        -------
        list[[X1, Y1, X2, Y2], ...]
            A list of boxes; for example, [[X1, Y1, X2, Y2], [X1, Y1, X2, Y2], ...].
        list[int]
            A list of IDs corresponding to the the list of boxes.
        """
        detection = []
        for b, c in zip(boxes_xyxy, boxes_conf):
          b = np.append(b, c)
          detection.append(b)
        track = self.st.update(np.array(detection)).astype(int)
        ids = matchDetTrkByXYXYForSORT(boxes_xyxy, track, max_spread=10)
        return boxes_xyxy, ids
