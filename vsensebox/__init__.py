# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


from vsensebox.vsense import VSense
from vsensebox.gui import config, reset
from vsensebox.utils.about import docs, github

__version__ = "0.1.1"
__author__ = "Ratha SIV"
__description__ = "VSenseBox - Python toolbox for visual sensing."
__homepage__ = "https://rathaumons.github.io/vsensebox"
__url__ = "https://github.com/rathaumons/vsensebox.git"

__all__ = (
    "__version__", 
    "VSense", 
    "config", 
    "reset", 
    "docs", 
    "github"
)

