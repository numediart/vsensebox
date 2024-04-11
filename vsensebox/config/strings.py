# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import yaml
from yaml.loader import SafeLoader
from vsensebox.utils.commontools import joinFPathFull, getGlobalRootDir


DEFAULT_STR_YAML = joinFPathFull(getGlobalRootDir(), "config/strings/strings.yaml")

class UnifiedStrings(object):

    """
    A class used to set up unified strings of VSenseBox based on the internal strings.yaml.

    Attributes
    ----------
    data : dict, auto
        Data or documents read from strings.yaml.
    none : str, auto
        Unified string of word 'None'.
    detector : str, auto
        Unified string of word 'Detector'.
    tracker : str, auto
        Unified string of word 'Tracker'.
    yolo_classic : str, auto
        Unified string of words 'YOLO Classic'.
    yolo_ultralytics : str, auto
        Unified string of words 'YOLO Ultralytics'.
    sort : str, auto
        Unified string of word 'SORT'.
    deepsort : str, auto
        Unified string of word 'DeepSORT'.
    centroid : str, auto
        Unified string of word 'Centroid'.
    """

    def __init__(self, strings_yaml=DEFAULT_STR_YAML):
        """Initailize by calling :meth:`load(strings_yaml=strings_yaml)`.

        Parameters
        ----------
        strings_yaml : str, default='{vsensebox root}/config/strings/strings.yaml'
            A path of a YAML file which stores the unified strings.
        """
        self.load(strings_yaml=strings_yaml)

    def load(self, strings_yaml): 
        """Load a configuration dictionary of a single document as a dictionary from 
        a :obj:`strings_yaml` file and automatically pass to :meth:`set()`.

        Parameters
        ----------
        strings_yaml : str
            A path of a YAML file which stores the unified strings.
        """
        with open(strings_yaml, 'r') as str_cfg:
            self.data = yaml.load(str_cfg, Loader=SafeLoader)
        self.set(self.data)

    def set(self, data):
        """Set a configuration dictionary of a single document to all attributes.

        Parameters
        ----------
        data : dict
            A configuration dictionary of a single document of the unified strings.
        """
        # module
        self.none = data['none']
        self.detector = data['detector']
        self.tracker = data['tracker']
        # detector
        self.yolo_classic = data['yolo_classic']
        self.yolo_ultralytics = data['yolo_ultralytics']
        # tracker
        self.sort = data['sort']
        self.deepsort = data['deepsort']
        self.centroid = data['centroid']

    def getUnifiedFormat(self, input_str):
        """Return a standard unified format string.

        Parameters
        ----------
        input_str : str
            An input string.
        
        Returns
        -------
        str
            A unified format string.
        """
        res = ""
        input_str = str(input_str)

        if 'yolo' in input_str.lower():
            res = input_str.title().replace("Yolo", "YOLO")
        elif 'ultralytics' in input_str.lower():
            res = input_str.title().replace("ultralytics", "Ultralytics")
        elif self.centroid.lower() == input_str.lower():
            res = input_str.title()
        elif self.sort.lower() == input_str.lower():
            res = input_str.upper()
        elif self.deepsort.lower() == input_str.lower():
            res = input_str.title().replace("Deepsort", "DeepSORT")
        elif self.none.lower() == input_str.lower():
            res = input_str.title()
        elif input_str.lower in ['top', 'center', 'bottom']:
            res = input_str.title()
        else:
            res = input_str
        
        return res

USTR = UnifiedStrings()
