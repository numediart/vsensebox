# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import os

current_dir = os.path.dirname(__file__)

def config():
    """Launch GUI configuration tool of VSenseBox.
    """
    import sys
    import subprocess as sp
    p = sp.Popen([sys.executable, os.path.join(current_dir, 'cfgloader_ui.py')])
    stdout, stderr = p.communicate()
