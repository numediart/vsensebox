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
    """

    def __init__(self, strings_yaml=DEFAULT_STR_YAML):
        """Initailize by calling :meth:`load(strings_yaml=strings_yaml)`.

        Parameters
        ----------
        strings_yaml : str, default='{vsensebox root}/config/strings/strings.yaml'
            A path of a YAML file which stores the unified strings.
        """
        self.data = self.load(strings_yaml=strings_yaml)

    def load(self, strings_yaml): 
        """Load a configuration dictionary of a single document as a dictionary from 
        a :obj:`strings_yaml` file and automatically pass to :meth:`set()`.

        Parameters
        ----------
        strings_yaml : str
            A path of a YAML file which stores the unified strings.
        """
        with open(strings_yaml, 'r') as str_cfg:
            data = yaml.load(str_cfg, Loader=SafeLoader)
        return data

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
        if isinstance(input_str, str):
            if input_str.lower() in self.data['detector'].lower():
                res = self.data['detector']
            elif input_str.lower() in self.data['yolo_classic'].lower():
                res = self.data['yolo_classic']
            elif input_str.lower() in self.data['yolo_ultralytics'].lower():
                res = self.data['yolo_ultralytics']
            elif input_str.lower() in self.data['tracker'].lower():
                res = self.data['tracker']
            elif input_str.lower() in self.data['centroid'].lower():
                res = self.data['centroid']
            elif input_str.lower() in self.data['sort'].lower():
                res = self.data['sort']
            elif input_str.lower() in self.data['deepsort'].lower():
                res = self.data['deepsort']
            elif input_str.lower() in self.data['basiciou'].lower():
                res = self.data['basiciou']
            elif input_str.lower in ['top', 'center', 'bottom']:
                res = input_str.title()
            else:
                res = input_str
        else:
            res = input_str
        return res

USTR = UnifiedStrings()
