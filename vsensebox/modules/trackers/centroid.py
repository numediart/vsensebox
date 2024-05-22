# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


from math import dist


class Centroid(object):

    """Class reprensented a Centroid tracker.
    """

    def __init__(self, cfg):
        """Initialize according to the given :obj:`cfg` and :obj:`auto_load`.

        Parameters
        ----------
        cfg : TCFG_Centroid
            A :class:`TCFG_Centroid` object which manages the configurations of tracker Centroid.
        """
        self.previous_ct = []
        self.previous_id = []
        self.current_ct = []
        self.current_id = []
        self.max_spread = cfg.max_spread
        self.pref_y = cfg.pref_y

    def _generateID(self):
        self.used_ids = list(set(self.used_ids))
        if len(self.used_ids) == 0: aID = 0
        else: aID = max(self.used_ids) + 1
        self.used_ids.append(aID)
        return aID
    
    def _findRepspoint(self, box_xyxy):
        x = int((box_xyxy[0] + box_xyxy[2]) / 2)
        y = 0
        if self.pref_y.lower() == "center":
            y = int((box_xyxy[1] + box_xyxy[3]) / 2)
        elif self.pref_y.lower() == "bottom":
            y = max(box_xyxy[1], box_xyxy[3])
        else:
            y = min(box_xyxy[1], box_xyxy[3])
        return (x, y)

    def _findPID(self, point):
        pindex = -1
        min_d = 8192
        i = 0
        for ct in self.previous_ct:
            d = dist(point, ct)
            if d < min_d:
                min_d = d
                pindex = i
            i += 1
        if min_d > self.max_spread: pindex = -1
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

        self.previous_ct = self.current_ct
        self.previous_id = self.current_id

        self.current_id = []
        self.used_ids = []

        self.current_ct = [self._findRepspoint(b) for b in boxes_xyxy]
        hang_indexes_in_clist = []
        len_bb = len(boxes_xyxy)
        if len_bb > 0:
            for i in range(0, len_bb):
                self.current_id.append(-1)
                pindex = self._findPID(self.current_ct[i])
                if pindex >= 0:
                    prev_id = self.previous_id[pindex]
                    if prev_id in self.used_ids:
                        hang_indexes_in_clist.append(i)
                    else:
                        self.current_id[i] = prev_id
                        self.used_ids.append(prev_id)
                else:
                    hang_indexes_in_clist.append(i)
            len_hlist = len(hang_indexes_in_clist)
            if len_hlist > 0:
                for index in hang_indexes_in_clist:
                    self.current_id[index] = self._generateID()
        
        return boxes_xyxy, self.current_id
