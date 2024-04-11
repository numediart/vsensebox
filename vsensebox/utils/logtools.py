# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import os
import time
import logging

_TIMESTAMP = str(time.strftime("%Y%m%d_%H%M%S"))
_VSENSEBOX_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
_LOG_DIR = os.path.join(_VSENSEBOX_ROOT, "data/logs").replace(os.sep, '/')
_LOG_TXT_PATH = os.path.join(_LOG_DIR, "log_" + _TIMESTAMP + ".txt")
_MAX_AGE = 86400 * 1 # 1 DAY

# Remove old logs
if os.path.exists(_LOG_DIR):
    for filename in os.listdir(_LOG_DIR):
        if "git" in filename: continue
        filestamp = os.stat(os.path.join(_LOG_DIR, filename)).st_mtime
        if  filestamp < time.time() - _MAX_AGE:
            os.remove(os.path.join(_LOG_DIR, filename))
else: os.makedirs(_LOG_DIR)

# Initial logger
logging.basicConfig(
    filename=_LOG_TXT_PATH,
    filemode='a',
    format='%(asctime)s %(levelname)-3s %(message)-3s',
    datefmt='%H:%M:%S',
    level=logging.INFO
)

# Add header
with open(_LOG_TXT_PATH, 'w+') as log_txt:
    log_txt.write("-------------------------------------------------")
    log_txt.write("-------------------------------------------------\n")
    log_txt.write("#################################################")
    log_txt.write("#################################################\n")
    log_txt.write("-------------------------------------------------")
    log_txt.write("-------------------------------------------------\n")

# Global
__this_logger__ = logging.getLogger(__name__)
__this_logger__.info(": Here we go!")
__TRUE__ = True


#############################################################################


def add_warning_log(msg, terminal_log=__TRUE__, add_new_line=True):
    """
    :meta private:
    """
    global __this_logger__
    if terminal_log: print(msg)
    if add_new_line: msg = ': \n' + str(msg)
    else: msg = ': ' + str(msg)
    __this_logger__.warning(msg)

def add_info_log(msg, terminal_log=__TRUE__, add_new_line=False):
    """
    :meta private:
    """
    global __this_logger__
    if terminal_log: print(msg)
    if add_new_line: msg = ': \n' + str(msg)
    else: msg = ': ' + str(msg)
    __this_logger__.info(msg)

def add_error_log(msg, terminal_log=__TRUE__, add_new_line=True):
    """
    :meta private:
    """
    global __this_logger__
    if terminal_log: print(msg)
    if add_new_line: msg = ': \n' + str(msg)
    else: msg = ': ' + str(msg)
    __this_logger__.error(msg)

def ignore_this_logger(name, level=logging.ERROR):
    """
    :meta private:
    """
    logger_to_ignore = logging.getLogger(name)
    logger_to_ignore.setLevel(level)

def disable_this_logger(name, level=logging.ERROR):
    """
    :meta private:
    """
    ignore_this_logger(name=name, level=level)
    logger_to_disable = logging.getLogger(name)
    logger_to_disable.disabled = True

def disable_terminal_log():
    """
    Disable all console or terminal logging of VSenseBox.
    """
    global __TRUE__
    __TRUE__ = False

def enable_terminal_log():
    """
    Enable all console or terminal logging of VSenseBox.
    """
    global __TRUE__
    __TRUE__ = True
