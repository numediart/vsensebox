# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import torch
import torchvision.ops.boxes as bops
import numpy as np


class BasicIoU(object):

    """Class reprensented a basic IoU tracker.
    """

    def __init__(self, cfg):
        """Initialize according to the given :obj:`cfg` and :obj:`auto_load`.

        Parameters
        ----------
        cfg : TCFG_BasicIoU
            A :class:`TCFG_BasicIoU` object which manages the configurations of tracker BasicIoU.
        """
        self.prev_cls = []
        self.prev_ids = []
        self.curr_ids = []
        self.prev_boxes_xyxy = []
        self.min_iou = cfg.min_iou
        self.use_gpu = False
        if str(cfg.device) == "0":
            self.use_gpu = True
            torch.set_default_device('cuda')

    def _generateID(self):
        self.used_ids = list(set(self.used_ids))
        if len(self.used_ids) == 0: aID = 0
        else: aID = max(self.used_ids) + 1
        self.used_ids.append(aID)
        return aID
    
    def _getIoU(self, box_xyxy_1, box_xyxy_2):
        iou = 0.0
        if self.use_gpu:
            box1 = torch.tensor(np.array([box_xyxy_1]), dtype=torch.float)
            box2 = torch.tensor(np.array([box_xyxy_2]), dtype=torch.float)
            iou = bops.box_iou(box1, box2)
        else:
            xA = np.maximum(box_xyxy_1[0], box_xyxy_2[0])
            yA = np.maximum(box_xyxy_1[1], box_xyxy_2[1])
            xB = np.minimum(box_xyxy_1[2], box_xyxy_2[2])
            yB = np.minimum(box_xyxy_1[3], box_xyxy_2[3])
            interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
            boxAArea = (box_xyxy_1[2] - box_xyxy_1[0] + 1) * (box_xyxy_1[3] - box_xyxy_1[1] + 1)
            boxBArea = (box_xyxy_2[2] - box_xyxy_2[0] + 1) * (box_xyxy_2[3] - box_xyxy_2[1] + 1)
            iou = interArea / float(boxAArea + boxBArea - interArea)
        return iou

    def _findPID(self, box_xyxy, box_class):
        pindex = -1
        max_iou = -1
        i = 0
        for b in self.prev_boxes_xyxy:
            iou = self._getIoU(box_xyxy, b)
            if iou > max_iou and self.prev_cls[i] == box_class:
                max_iou = iou
                pindex = i
            i += 1
        if max_iou < self.min_iou: pindex = -1
        return pindex

    def update(self, boxes_xyxy, boxes_conf, boxes_cls=None, img=None):
        """Update the tracker and return a track list.

        Parameters
        ----------
        boxes_xyxy : list[[X1, Y1, X2, Y2], ...]
            A list of boxes; for example, [[X1, Y1, X2, Y2], [X1, Y1, X2, Y2], ...].
        boxes_conf : list[float, ...]
            Being consistent with other trackers, will be ignored.
        boxes_cls : list[int, ...], default=None
            A list of detection class corresponding to boxes_xyxy.
        img : any, default=None
            Being consistent with other trackers, will be ignored.

        Returns
        -------
        list[[X1, Y1, X2, Y2], ...]
            A list of boxes; for example, [[X1, Y1, X2, Y2], [X1, Y1, X2, Y2], ...].
        list[int]
            A list of IDs corresponding to the the list of boxes.
        """

        self.prev_ids = self.curr_ids

        self.curr_ids = []
        self.used_ids = []
        hang_indexes = []

        len_bb = len(boxes_xyxy)

        if len_bb > 0:
            for i in range(0, len_bb):
                self.curr_ids.append(-1)
                pindex = self._findPID(boxes_xyxy[i], boxes_cls[i])
                if pindex >= 0:
                    prev_id = self.prev_ids[pindex]
                    if prev_id in self.used_ids:
                        hang_indexes.append(i)
                    else:
                        self.curr_ids[i] = prev_id
                        self.used_ids.append(prev_id)
                else:
                    hang_indexes.append(i)
            if len(hang_indexes) > 0:
                for index in hang_indexes:
                    self.curr_ids[index] = self._generateID()
        
        self.prev_cls = boxes_cls
        self.prev_boxes_xyxy = boxes_xyxy
        
        return boxes_xyxy, self.curr_ids
