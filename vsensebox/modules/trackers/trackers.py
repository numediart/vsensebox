# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


from vsensebox.config.strings import USTR
from vsensebox.config.confighelper import getCFGDict
from vsensebox.config.configurator import TCFG_Centroid, TCFG_SORT, TCFG_DeepSORT, TCFG_BasicIoU


def checkTrk(tracker, config_yaml, relative_to_vsensebox_root):
    """Automatically check, select, and config the supported tracker according to the 
    input :obj:`config_yaml`.

    Parameters
    ----------
    tracker : tracker object
        A tracker object; for example, :class:`Centroid` or :class:`SORT`.
    config_yaml : str or dict
        A YAML/JSON file path, or a raw/ready dictionary.
    relative_to_vsensebox_root : bool
        This parameter is passed to the corresponding configurator; for example, 
        :class:`TCFG_Centroid` or :class:`TCFG_SORT`.
    """
    cfg = getCFGDict(config_yaml)
    trk_name = USTR.getUnifiedFormat(cfg['tracker'])

    if tracker is None:
        from .centroid import Centroid
        from .sort import SORT
        from .deepsort import DeepSORT
        from .basiciou import BasicIoU
        trackers = {
            USTR.getUnifiedFormat('centroid'): Centroid, 
            USTR.getUnifiedFormat('sort'): SORT,
            USTR.getUnifiedFormat('deepsort'): DeepSORT,
            USTR.getUnifiedFormat('basiciou'): BasicIoU
        }
        cfgs = {
            USTR.getUnifiedFormat('centroid'): TCFG_Centroid, 
            USTR.getUnifiedFormat('sort'): TCFG_SORT,
            USTR.getUnifiedFormat('deepsort'): TCFG_DeepSORT,
            USTR.getUnifiedFormat('basiciou'): TCFG_BasicIoU
        }
        tracker = trackers[trk_name](cfgs[trk_name](
            config_yaml, 
            relative_to_vsensebox_root=relative_to_vsensebox_root)
        )
    return tracker

