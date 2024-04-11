# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


# Configurations
from vsensebox.config.configurator import DET_CONFIG_DIR, TRK_CONFIG_DIR, IN_ROOT_DIR
from vsensebox.config.confighelper import getCFGDict

# Utils & tools
from vsensebox.modules.detectors import checkDet
from vsensebox.modules.trackers import checkTrk
from vsensebox.utils.commontools import getCVMat, joinFPathFull, getAncestorDir

# Default detector
DEFAULT_DET_CONFIG = getCFGDict(joinFPathFull(DET_CONFIG_DIR, 'default.yaml'))
DEFAULT_DET_YAML = joinFPathFull(IN_ROOT_DIR, DEFAULT_DET_CONFIG['config_yaml'])
DET_YAML_TO_ROOT = True if getAncestorDir(DEFAULT_DET_CONFIG['config_yaml']) == 'config/detectors' else False

# Default tracker
DEFAULT_TRK_CONFIG = getCFGDict(joinFPathFull(TRK_CONFIG_DIR, 'default.yaml'))
DEFAULT_TRK_YAML = joinFPathFull(IN_ROOT_DIR, DEFAULT_TRK_CONFIG['config_yaml'])
TRK_YAML_TO_ROOT = True if getAncestorDir(DEFAULT_TRK_CONFIG['config_yaml']) == 'config/trackers' else False


class VSense(object):

    """
    VSense is used to operate the object detection and tracking.

    Attributes
    ----------
    assets : VSenseAssets
        A :class:`VSenseAssets` object used to store assets of VSense.
    """

    def __init__(self):
        self.assets = VSenseAssets()
        self._detector = None
        self._tracker = None
        self._yaml_det = None
        self._yaml_trk = None
        self._det_rel_to_root = False
        self._trk_rel_to_root = False

    def detect(self, img, config_yaml=None, img_is_mat=False):
        """Detect objects in the given image :obj:`img`.

        Parameters
        ----------
        img : str or Mat
            Image file or a :obj:`Mat` like object.
        config_yaml : str, default=None
            Path of YAML config file.
        img_is_mat : bool, default=False
            Speed up the function by telling whether the :obj:`img` is :obj:`Mat` like object.
        """
        if not img_is_mat: img = getCVMat(img)
        if config_yaml is None:
            config_yaml = DEFAULT_DET_YAML
            self._det_rel_to_root = DET_YAML_TO_ROOT
        if self._yaml_det != config_yaml:
            self._detector = checkDet(detector=self._detector, config_yaml=config_yaml, 
                                      relative_to_vsensebox_root=self._det_rel_to_root)
        else:
            self._yaml_det = config_yaml
        img, boxes_xywh, boxes_xyxy, keypoints, confs, cls = self._detector.detect(img)
        self.assets.update(
            boxes_xywh=boxes_xywh, 
            boxes_xyxy=boxes_xyxy, 
            keypoints=keypoints, 
            boxes_confs=confs,
            boxes_cls=cls
        )

    def track(self, img=None, config_yaml=None, img_is_mat=False):
        """Track the detected objects in the given image :obj:`img`.

        Parameters
        ----------
        img : str or Mat
            Image file or a :obj:`Mat` like object.
        config_yaml : str, default=None
            Path of YAML config file.
        img_is_mat : bool, default=False
            Speed up the function by telling whether the :obj:`img` is :obj:`Mat` like object.
        """
        if not img_is_mat: img = getCVMat(img)
        if config_yaml is None:
            config_yaml = DEFAULT_TRK_YAML
            self._trk_rel_to_root = TRK_YAML_TO_ROOT
        if self._yaml_trk != config_yaml:
            self._tracker = checkTrk(tracker=self._tracker, config_yaml=config_yaml, 
                                     relative_to_vsensebox_root=self._trk_rel_to_root)
        else:
            self._yaml_trk = config_yaml
        boxes_xyxy, self.assets.ids = self._tracker.update(
            self.assets.boxes_xyxy, 
            self.assets.boxes_confs, 
            boxes_cls=self.assets.boxes_cls, 
            img=img
        )


class VSenseAssets(object):
    
    """
    A class used to store assets of VSense.

    Attributes
    ----------
    boxes_xyxy : list[[X1, Y1, X2, Y2], ...], optional
        A list of bounding boxes; for example, [[X1, Y1, X2, Y2], [X1, Y1, X2, Y2], ...].
    boxes_xywh : list[[X, Y, W, H], ...], optional
        A list of bounding boxes; for example, [[X, Y, W, H], [X, Y, W, H], ...].
    boxes_confs : list[float, ...], optional
        A list of detection confidences corresponding to bounding boxes.
    boxes_cls : list[int, ...], optional
        A list of detection class corresponding to bounding boxes.
    keypoints : list[], optional
        A list of detected bodies' keypoints.
    ids: list[int, ...], optional
        A list of IDs corresponding to bounding boxes.
    masks: list[], optional
        A list of detected masks.
    misc : list[], optional
        A list of miscellaneous items.
    """
    
    def __init__(self):
        """Construct a VSenseAssets.
        """
        self.boxes_xyxy = []
        self.boxes_xywh = []
        self.boxes_confs = []
        self.boxes_cls = []
        self.keypoints = []
        self.ids = []
        self.masks = []
        self.miscs = []
    
    def update(self, 
               boxes_xyxy=[], 
               boxes_xywh=[], 
               boxes_confs=[], 
               boxes_cls=[], 
               keypoints=[], 
               ids=[], 
               masks=[], 
               miscs=[]):
        """Update a VSenseAssets.

        Parameters
        ----------
        boxes_xyxy : list[[X1, Y1, X2, Y2], ...], optional
            A list of bounding boxes; for example, [[X1, Y1, X2, Y2], [X1, Y1, X2, Y2], ...].
        boxes_xywh : list[[X, Y, W, H], ...], optional
            A list of bounding boxes; for example, [[X, Y, W, H], [X, Y, W, H], ...].
        boxes_confs : list[float, ...], optional
            A list of detection confidences corresponding to bounding boxes.
        boxes_cls : list[int, ...], optional
            A list of detection class corresponding to bounding boxes.
        keypoints : list[], optional
            A list of detected bodies' keypoints.
        ids: list[int, ...], optional
            A list of IDs corresponding to bounding boxes.
        masks: list[], optional
            A list of detected masks.
        misc : list[], optional
            A list of miscellaneous items.
        """
        self.boxes_xyxy = boxes_xyxy
        self.boxes_xywh = boxes_xywh
        self.boxes_confs = boxes_confs
        self.boxes_cls = boxes_cls
        self.keypoints = keypoints
        self.ids = ids
        self.masks = masks
        self.miscs = miscs

