# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


from vsensebox.config.strings import USTR
from vsensebox.config.confighelper import getCFGDict
from vsensebox.config.configurator import DCFG_YOLOULT, DCFG_YOLOCLS


def checkDet(detector, config_yaml, relative_to_vsensebox_root):
    """Automatically check, select, and config the supported detector according to the 
    input :obj:`config_yaml`.

    Parameters
    ----------
    detector : detector object
        A detector object; for example, :class:`YOLO_Ultralytics` or :class:`YOLO_Classic`.
    config_yaml : str or dict
        A YAML/JSON file path, or a raw/ready dictionary.
    relative_to_vsensebox_root : bool
        This parameter is passed to the corresponding configurator; for example, 
        :class:`DCFG_YOLOULT` or :class:`DCFG_YOLOCLS`.
    """
    cfg = getCFGDict(config_yaml)
    det_name = USTR.getUnifiedFormat(cfg['detector'])

    if detector is None:
        from .yolo_ultralytics import YOLO_Ultralytics
        from .yolo_classic import YOLO_Classic
        detectors = {
            USTR.getUnifiedFormat('yolo_ultralytics'): YOLO_Ultralytics, 
            USTR.getUnifiedFormat('yolo_classic'): YOLO_Classic
        }
        cfgs = {
            USTR.getUnifiedFormat('yolo_ultralytics'): DCFG_YOLOULT, 
            USTR.getUnifiedFormat('yolo_classic'): DCFG_YOLOCLS
        }
        detector = detectors[det_name](cfgs[det_name](
            config_yaml, 
            relative_to_vsensebox_root=relative_to_vsensebox_root)
        )
    return detector

