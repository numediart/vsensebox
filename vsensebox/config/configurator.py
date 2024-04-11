# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


from .strings import USTR
from .confighelper import getCFGDict, getListCFGDoc, dumpDocDict, dumpListDocDict
from vsensebox.utils.logtools import add_warning_log, add_error_log
from vsensebox.utils.commontools import (joinFPathFull, getGlobalRootDir, 
                                         getAdaptiveAbsPathFDS, normalizePathFDS)

IN_ROOT_DIR = getGlobalRootDir()
IN_DATA_DIR = joinFPathFull(IN_ROOT_DIR, 'data')
IN_CONFIG_DIR = joinFPathFull(IN_ROOT_DIR, 'config')
DET_CONFIG_DIR = joinFPathFull(IN_CONFIG_DIR, 'detectors')
TRK_CONFIG_DIR = joinFPathFull(IN_CONFIG_DIR, 'trackers')
STR_CONFIG_DIR = joinFPathFull(IN_CONFIG_DIR, 'strings')


class BaseCGF(object):

    """
    An base CFG class used to store the necessary configurations of a module.

    Attributes
    ----------
    unified_strings : MyStrings, auto
        A :class:`MyStrings` object used to store unified strings.
    configs : dict or list[dict], default={}
        A configuration dictionary of a single document or a list of multiple documents 
        of the configurations.
    """

    def __init__(self):
        self.unified_strings = USTR
        self.configs = {}
    
    def loadDoc(self, input):
        """Load and set dictionary of a single document from a YAML/JSON file or string.

        Parameters
        ----------
        input : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        """
        self.configs = getCFGDict(input)
    
    def loadDocs(self, input):
        """Load and set a list of multiple documents from a YAML/JSON file or string.

        Parameters
        ----------
        input : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        """
        self.configs = getListCFGDoc(input)
    
    def dumpDoc(self, output, header=""):
        """Dump the :attr:`configs` into a YAML file with simple format.

        Parameters
        ----------
        output : str
            A path file to dump.
        header : str
            A file header descriptoin.
        """
        dumpDocDict(output_file=output, doc=self.configs, header=header)
    
    def dumpDocs(self, output, header=""):
        """Dump the :attr:`configs` into a YAML file with simple format.

        Parameters
        ----------
        output : str
            A path file to dump.
        header : str
            A file header descriptoin.
        """
        dumpListDocDict(output_file=output, doc=self.configs, header=header)


class DCFG_YOLOCLS(BaseCGF):

    """
    A class used to store the necessary configurations of detector YOLO Classic which 
    use :code:`.weights` model.

    Attributes
    ----------
    detector : str
        Configured name of detector YOLO Classic.
    nms : float
        Parameter nms of YOLO Classic.
    conf : float
        Parameter conf of YOLO Classic.
    imgsz : int
        Input image size of YOLO Classic.
    min_width : int
        Minimum width filter.
    classes : list[int, ...]
        Filtering classes of detection.
    class_file : str
        Path of coco.names file of YOLO Classic.
    model_cfg_file : str
        Path of .cfg file of YOLO Classic.
    model_file : str
        Path of .weights file of YOLO Classic.
    from_dir : str
        Path of the root directory, relative to path of :attr:`model_file`.
    """

    def __init__(self, cfg=None, relative_to_vsensebox_root=False):
        """Initialize the class according to the :obj:`relative_to_vsensebox_root` which defines 
        whether all the paths inside your configuration file are relative to :code:`{vsensebox root}` 
        or not. If all the paths inside your configuration file have full absolute paths, 
        setting :obj:`relative_to_vsensebox_root` is optional.

        Parameters
        ----------
        cfg : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        relative_to_vsensebox_root : bool, default=False
            (1) Set :code:`relative_to_vsensebox_root=False` to use your current working directory 
            as where all the paths in your configuration file are relative to; for example, 
            the path of :attr:`model_file` inside your configuration file is set relatively 
            to your current working directory. 
            (2) Set :code:`relative_to_vsensebox_root=True` when all the paths in your configuration 
            file are relative to :code:`{vsensebox root}`.
        """
        super().__init__()
        self.from_dir = ""
        if relative_to_vsensebox_root:
            self.from_dir = IN_ROOT_DIR
        if cfg is not None:
            self.set(cfg)

    def set(self, input):
        """
        Set configurations according to :obj:`input`.

        Parameters
        ----------
        input : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        """
        super().loadDoc(input)
        if self.configs:
            try:
                self.detector = self.unified_strings.getUnifiedFormat(self.configs['detector'])
                self.nms = self.configs['nms']
                self.conf = self.configs['conf']
                self.imgsz = self.configs['imgsz']
                self.min_width = self.configs['min_width']
                self.classes = self.configs['classes']
                self.class_file = getAdaptiveAbsPathFDS(self.from_dir, self.configs['class_file'])
                self.model_cfg_file = getAdaptiveAbsPathFDS(self.from_dir, self.configs['model_cfg_file'])
                self.model_file = getAdaptiveAbsPathFDS(self.from_dir, self.configs['model_file'])
                self.configs = self.getDocument()
            except Exception as e:
                msg = "DCFG_YOLOCLS : set() -> " + str(e)
                add_error_log(msg)
                raise ValueError(msg)
        else:
            add_warning_log("DCFG_YOLOCLS : set() -> The configuration is empty.")

    def getDocument(self):
        """Return a configuration dictionary of a single document of the attributes which 
        are the parameters of detector YOLO Classic.

        Returns
        -------
        dict
            A configuration dictionary of a single document of the configurations.
        """
        yolocs_doc = {
            "detector": self.detector,
            "nms": self.nms,
            "conf": self.conf,
            "imgsz": self.imgsz,
            "min_width": self.min_width,
            "classes": self.classes,
            "class_file": normalizePathFDS(IN_ROOT_DIR, self.class_file),
            "model_cfg_file": normalizePathFDS(IN_ROOT_DIR, self.model_cfg_file),
            "model_file": normalizePathFDS(IN_ROOT_DIR, self.model_file),
        }
        return yolocs_doc


class DCFG_YOLOULT(BaseCGF):

    """
    A class used to store the necessary configurations of detector Ultralytics.

    Attributes
    ----------
    detector : str
        Configured name of detector YOLO Ultralytics.
    conf : float
        Parameter conf of YOLO Ultralytics.
    iou : float
        Parameter iou of YOLO Ultralytics.
    imgsz : int
        Parameter imgsz of YOLO Ultralytics.
    half : bool
        Parameter half of YOLO Ultralytics.
    min_width : int
        Minimum width filter.
    classes : list[int, ...]
        Parameter classes of YOLO Ultralytics.
    device : str
        Parameter of device to compute; for example, 0 or cpu.
    max_det : int
        Parameter max_det of YOLO Ultralytics.
    line_width : int
        Parameter line_width of YOLO Ultralytics.
    model_file : str
        Path of :attr:`model_file` for YOLO Ultralytics.
    from_dir : str
        Path of the root directory, relative to path of :attr:`model_file`.
    """

    def __init__(self, cfg=None, relative_to_vsensebox_root=False):
        """Initialize the class according to the :obj:`relative_to_vsensebox_root` which 
        defines whether all the paths inside your configuration file are relative to 
        :code:`{vsensebox root}` or not. If all the paths inside your configuration file have 
        full absolute paths, setting :obj:`relative_to_vsensebox_root` is optional.

        Parameters
        ----------
        cfg : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        relative_to_vsensebox_root : bool, default=False
            (1) Set :code:`relative_to_vsensebox_root=False` to use your current working 
            directory as where all the paths in your configuration file are relative to; 
            for example, the path of :attr:`model_file` inside your configuration file is 
            set relatively to your current working directory. 
            (2) Set :code:`relative_to_vsensebox_root=True` when all the paths in your 
            configuration file are relative to :code:{vsensebox root}.
        """
        super().__init__()
        self.from_dir = ""
        if relative_to_vsensebox_root:
            self.from_dir = IN_ROOT_DIR
        if cfg is not None:
            self.set(cfg)

    def set(self, input):
        """
        Set configurations according to :obj:`input`.

        Parameters
        ----------
        input : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        """
        super().loadDoc(input)
        if self.configs:
            try:
                self.detector = self.unified_strings.getUnifiedFormat(self.configs['detector'])
                self.conf = self.configs['conf']
                self.iou = self.configs['iou']
                self.imgsz = self.configs['imgsz']
                self.half = self.configs['half']
                self.min_width = self.configs['min_width']
                self.classes = self.configs['classes']
                self.device = self.configs['device']
                self.max_det = self.configs['max_det']
                self.line_width = self.configs['line_width']
                self.model_file = getAdaptiveAbsPathFDS(self.from_dir, self.configs['model_file'])
                self.configs = self.getDocument()
            except Exception as e:
                msg = "DCFG_YOLOULT : set() -> " + str(e)
                add_error_log(msg)
                raise ValueError(msg)
        else:
            add_warning_log("DCFG_YOLOULT : set() -> The configuration is empty.")

    def getDocument(self):
        """Return yolout_doc, a configuration dictionary of a single document of the attributes which 
        are the parameters of detector YOLO Ultralytics.

        Returns
        -------
        dict
            A configuration dictionary of a single document of the configurations.
        """
        yolout_doc = {
            "detector": self.detector,
            "conf": self.conf,
            "iou": self.iou,
            "imgsz": self.imgsz,
            "half": self.half,
            "min_width": self.min_width,
            "classes": self.classes,
            "device": self.device,
            "max_det": self.max_det,
            "line_width": self.line_width,
            "model_file": normalizePathFDS(IN_ROOT_DIR, self.model_file),
        }
        return yolout_doc


class TCFG_Centroid(BaseCGF):

    """
    A class used to store the necessary configurations of tracker Centroid.

    Attributes
    ----------
    tracker : str
        Configured name of tracker Centroid.
    max_spread : int
        Maximum distance of the being tracked :class:`Person` object of previous and current state.
    pref_y : str
        Prefered Y of represented point; Choices of Top/Center/Bottom.
    """

    def __init__(self, cfg=None, relative_to_vsensebox_root=False):
        """Initialize the class.

        Parameters
        ----------
        cfg : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        relative_to_vsensebox_root : bool, default=False
            Being consistent with others, will be ignored.
        """
        super().__init__()
        self.from_dir = ""
        if relative_to_vsensebox_root:
            self.from_dir = IN_ROOT_DIR
        if cfg is not None:
            self.set(cfg)

    def set(self, input):
        """
        Set configurations according to :obj:`input`.

        Parameters
        ----------
        input : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        """
        super().loadDoc(input)
        if self.configs:
            try:
                self.tracker = self.unified_strings.getUnifiedFormat(self.configs['tracker'])
                self.max_spread = self.configs['max_spread']
                self.pref_y = self.configs['pref_y']
                self.configs = self.getDocument()
            except Exception as e:
                msg = "TCFG_Centroid : set() -> " + str(e)
                add_error_log(msg)
                raise ValueError(msg)
        else:
            add_warning_log("TCFG_Centroid : set() -> The configuration is empty.")

    def getDocument(self):
        """Return a configuration dictionary of a single document of the attributes which 
        are the parameters of tracker Centroid.

        Returns
        -------
        dict
            A configuration dictionary of a single document of the configurations.
        """
        centroid_doc = {
            "tracker": self.tracker,
            "max_spread": self.max_spread,
            "pref_y": self.pref_y
        }
        return centroid_doc


class TCFG_BasicIoU(BaseCGF):

    """
    A class used to store the necessary configurations of tracker BasicIoU.

    Attributes
    ----------
    tracker : str
        Configured name of tracker BasicIoU.
    min_iou : float
        Minimum IoU value for matching.
    device : str
        Device to compute; for example, 0 or cpu.
    """

    def __init__(self, cfg=None, relative_to_vsensebox_root=False):
        """Initialize the class.

        Parameters
        ----------
        cfg : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        relative_to_vsensebox_root : bool, default=False
            Being consistent with others, will be ignored.
        """
        super().__init__()
        self.from_dir = ""
        if relative_to_vsensebox_root:
            self.from_dir = IN_ROOT_DIR
        if cfg is not None:
            self.set(cfg)

    def set(self, input):
        """
        Set configurations according to :obj:`input`.

        Parameters
        ----------
        input : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        """
        super().loadDoc(input)
        if self.configs:
            try:
                self.tracker = self.unified_strings.getUnifiedFormat(self.configs['tracker'])
                self.min_iou = self.configs['min_iou']
                self.device = self.configs['device']
                self.configs = self.getDocument()
            except Exception as e:
                msg = "TCFG_BasicIoU : set() -> " + str(e)
                add_error_log(msg)
                raise ValueError(msg)
        else:
            add_warning_log("TCFG_BasicIoU : set() -> The configuration is empty.")

    def getDocument(self):
        """Return a configuration dictionary of a single document of the attributes which 
        are the parameters of tracker BasicIoU.

        Returns
        -------
        dict
            A configuration dictionary of a single document of the configurations.
        """
        basiciou_doc = {
            "tracker": self.tracker,
            "min_iou": self.min_iou,
            "device": self.device
        }
        return basiciou_doc


class TCFG_SORT(BaseCGF):

    """
    A class used to store the necessary configurations of tracker SORT.

    Attributes
    ----------
    tracker : str
        Configured name of tracker SORT.
    max_age : int
        Parameter :obj:`max_age` of tracker SORT.
    min_hits : int
        Parameter :obj:`min_hits` of tracker SORT.
    iou_threshold : float
        Parameter :obj:`iou_threshold` of tracker SORT.
    """

    def __init__(self, cfg=None, relative_to_vsensebox_root=False):
        """Initialize the class.

        Parameters
        ----------
        cfg : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        relative_to_vsensebox_root : bool, default=False
            Being consistent with others, will be ignored.
        """
        super().__init__()
        self.from_dir = ""
        if relative_to_vsensebox_root:
            self.from_dir = IN_ROOT_DIR
        if cfg is not None:
            self.set(cfg)

    def set(self, input):
        """
        Set configurations according to :obj:`input`.

        Parameters
        ----------
        input : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        """
        super().loadDoc(input)
        if self.configs:
            try:
                self.tracker = self.unified_strings.getUnifiedFormat(self.configs['tracker'])
                self.max_age = self.configs['max_age']
                self.min_hits = self.configs['min_hits']
                self.iou_threshold = self.configs['iou_threshold']
                self.configs = self.getDocument()
            except Exception as e:
                msg = "TCFG_SORT : set() -> " + str(e)
                add_error_log(msg)
                raise ValueError(msg)
        else:
            add_warning_log("TCFG_SORT : set() -> The configuration is empty.")

    def getDocument(self):
        """
        Return a configuration dictionary of a single document of the attributes which 
        are the parameters of tracker SORT.

        Returns
        -------
        dict
            A configuration dictionary of a single document of the configurations.
        """
        sort_doc = {
            "tracker": self.tracker,
            "max_age": self.max_age,
            "min_hits": self.min_hits,
            "iou_threshold": self.iou_threshold
        }
        return sort_doc
        

class TCFG_DeepSORT(BaseCGF):

    """
    A class used to store the necessary configurations of tracker DeepSORT.

    Attributes
    ----------
    tracker : str
        Configured name of tracker DeepSORT.
    nn_budget : int
        Parameter :obj:`nn_budget` of tracker DeepSORT.
    batch_size : int
        Parameter :obj:`batch_size` of tracker DeepSORT.
    nms_max_overlap : float
        Parameter :obj:`nms_max_overlap` of tracker DeepSORT.
    max_cosine_distance : float
        Parameter :obj:`max_cosine_distance` of tracker DeepSORT.
    model_file : str
        Path of model file for tracker DeepSORT.
    from_dir : str
        Path of the root directory, relative to path of :attr:`model_file`.
    """

    def __init__(self, cfg=None, relative_to_vsensebox_root=False):
        """Initialize the class according to the :obj:`relative_to_vsensebox_root` which defines 
        whether all the paths inside your configuration file are relative to :code:`{vsensebox root}` 
        or not. If all the paths inside your configuration file have full absolute paths, setting 
        :obj:`relative_to_vsensebox_root` is optional.

        Parameters
        ----------
        cfg : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        relative_to_vsensebox_root : bool, default=False
            (1) Set :code:`relative_to_vsensebox_root=False` to use your current working directory 
            as where all the paths in your configuration file are relative to; for example, 
            the path of :attr:`model_file` inside your configuration file is set relatively to 
            your current working directory. 
            (2) Set :code:`relative_to_vsensebox_root=True` when all the paths in your configuration 
            file are relative to :code:`{vsensebox root}`.
        """
        super().__init__()
        self.from_dir = ""
        if relative_to_vsensebox_root:
            self.from_dir = IN_ROOT_DIR
        if cfg is not None:
            self.set(cfg)

    def set(self, input):
        """
        Set configurations according to :obj:`input`.

        Parameters
        ----------
        input : str or dict
            A YAML/JSON file path, or a raw/ready dictionary.
        """
        super().loadDoc(input)
        if self.configs:
            try:
                self.tracker = self.unified_strings.getUnifiedFormat(self.configs['tracker'])
                self.nn_budget = self.configs['nn_budget']
                self.batch_size = self.configs['batch_size']
                self.nms_max_overlap = self.configs['nms_max_overlap']
                self.max_cosine_distance = self.configs['max_cosine_distance']
                self.model_file = getAdaptiveAbsPathFDS(self.from_dir, self.configs['model_file'])
                self.configs = self.getDocument()
            except Exception as e:
                msg = "TCFG_DeepSORT : set() -> " + str(e)
                add_error_log(msg)
                raise ValueError(msg)
        else:
            add_warning_log("TCFG_DeepSORT : set() -> The configuration is empty.")

    def getDocument(self):
        """Return a configuration dictionary of a single document of the attributes which 
        are the parameters of tracker DeepSORT.

        Returns
        -------
        dict
            A configuration dictionary of a single document of the configurations.
        """
        deepsort_doc = {
            "tracker": self.tracker,
            "nn_budget": self.nn_budget,
            "batch_size": self.batch_size,
            "nms_max_overlap": self.nms_max_overlap,
            "max_cosine_distance": self.max_cosine_distance,
            "model_file": normalizePathFDS(IN_ROOT_DIR, self.model_file)
        }
        return deepsort_doc

