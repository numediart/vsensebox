# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import os

from vsensebox.utils.logtools import add_warning_log, add_info_log
from vsensebox.utils.commontools import isExist, joinFPathFull
from vsensebox.config.configurator import DET_CONFIG_DIR, TRK_CONFIG_DIR, STR_CONFIG_DIR


CUR_DIR = os.path.dirname(__file__)
UI_TMP = joinFPathFull(CUR_DIR, "ui.tmp")

def config(config_yaml=None):
    """Launch GUI configuration tool of VSenseBox.

    Parameters
    ----------
    config_yaml : str, default=None
        Path of YAML config file.
    """
    if config_yaml is not None:
        if not isExist(str(config_yaml)):
            add_warning_log("VSenseBox:config() -> Input config_yaml is not valid.")
        else:
            with open(UI_TMP, "w+") as UI_TMP_file:
                UI_TMP_file.write(config_yaml + "\n")

    import sys
    import subprocess as sp
    p = sp.Popen([sys.executable, os.path.join(CUR_DIR, 'cfgloader_ui.py')])
    stdout, stderr = p.communicate()

def reset():
    """Reset the internal configurations.
    """
    import shutil
    shutil.unpack_archive(joinFPathFull(DET_CONFIG_DIR, 'detectors.zip'), DET_CONFIG_DIR)
    shutil.unpack_archive(joinFPathFull(TRK_CONFIG_DIR, 'trackers.zip'), TRK_CONFIG_DIR)
    shutil.unpack_archive(joinFPathFull(STR_CONFIG_DIR, 'strings.zip'), STR_CONFIG_DIR)
    add_info_log("Reset successfully!")
