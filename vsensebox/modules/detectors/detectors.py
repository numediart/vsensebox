# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


from vsensebox.config.configurator import DCFG_YOLOULT, DCFG_YOLOCLS
from vsensebox.config.confighelper import getCFGDict

def checkDet(detector, config_yaml, relative_to_vsensebox_root):
    
    cfg = getCFGDict(config_yaml)
    det_name = cfg['detector'].lower()

    if detector is None:
        from .yolo_ultralytics import YOLO_Ultralytics
        from .yolo_classic import YOLO_Classic
        detectors = {
            'yolo_ultralytics': YOLO_Ultralytics, 
            'yolo_classic': YOLO_Classic
        }
        cfgs = {
            'yolo_ultralytics': DCFG_YOLOULT, 
            'yolo_classic': DCFG_YOLOCLS
        }
        detector = detectors[det_name](cfgs[det_name](
            config_yaml, 
            relative_to_vsensebox_root=relative_to_vsensebox_root)
        )
    return detector

