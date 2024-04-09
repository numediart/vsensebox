# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


from vsensebox.config.configurator import TCFG_Centroid, TCFG_SORT, TCFG_DeepSORT
from vsensebox.config.confighelper import getCFGDict

def checkTrk(tracker, config_yaml, relative_to_vsensebox_root):

    cfg = getCFGDict(config_yaml)
    trk_name = cfg['tracker'].lower()

    if tracker is None:
        from .centroid import Centroid
        from .sort import SORT
        from .deepsort import DeepSORT
        trackers = {
            'centroid': Centroid, 
            'sort': SORT,
            'deepsort': DeepSORT
        }
        cfgs = {
            'centroid': TCFG_Centroid, 
            'sort': TCFG_SORT,
            'deepsort': TCFG_DeepSORT
        }
        tracker = trackers[trk_name](cfgs[trk_name](
            config_yaml, 
            relative_to_vsensebox_root=relative_to_vsensebox_root)
        )
    return tracker

