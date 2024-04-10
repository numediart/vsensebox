# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import os

from vsensebox.utils.logtools import add_warning_log
from vsensebox.utils.commontools import isExist, joinFPathFull


current_dir = os.path.dirname(__file__)
ui_tmp = joinFPathFull(current_dir, "ui.tmp")

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
            with open(ui_tmp, "w+") as ui_tmp_file:
                ui_tmp_file.write(config_yaml + "\n")

    import sys
    import subprocess as sp
    p = sp.Popen([sys.executable, os.path.join(current_dir, 'cfgloader_ui.py')])
    stdout, stderr = p.communicate()
