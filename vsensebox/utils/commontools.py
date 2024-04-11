# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import os
import sys
import cv2
import numpy as np


def getCVMat(img, to_rgb=False):
    """
    :meta private:
    """
    if isinstance(img, str):
        if isExist(img):
            try:
                img = cv2.imread(getAbsPathFDS(img))
                if to_rgb:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            except Exception as e:
                msg = "getCVMat() -> " + str(e)
                raise ValueError(msg)
        else:
            print("getCVMat() -> The input 'img' does not exit.")
    elif isinstance(img, np.ndarray):
        if len(img.shape) == 3:
            if to_rgb:
                try:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                except Exception as e:
                    msg = "getCVMat() -> " + str(e)
                    raise ValueError(msg)
        else:
            msg = "getCVMat() -> The input 'img' is not valid."
            raise ValueError(msg)
    else:
        msg = "getCVMat() -> Can't determine the format of the given 'img'."
        raise ValueError(msg)
    return img

def isExist(path):
    """
    :meta private:
    """
    path = os.path.abspath(path).replace(os.sep, '/')
    return os.path.exists(path)

def getAbsPathFDS(input):
    """
    :meta private:
    """
    abspath = os.path.abspath(input).replace(os.sep, '/')
    return abspath

def getAdaptiveAbsPathFDS(from_here, input):
    """
    :meta private:
    """
    abspath = getAbsPathFDS(joinFPathFull(from_here, input))
    return abspath

def extendPathFDS(main_path, what_to_extend):
    """
    :meta private:
    """
    abspath = os.path.join(main_path, what_to_extend).replace(os.sep, '/')
    return abspath

def normalizePathFDS(main_path, what_to_normalize):
    """
    :meta private:
    """
    path = getAdaptiveAbsPathFDS(getGlobalRootDir(), what_to_normalize)
    if main_path.replace(os.sep, '/')[:2] == what_to_normalize.replace(os.sep, '/')[:2]:
        tmp = os.path.relpath(what_to_normalize, main_path).replace(os.sep, '/')
        if tmp[:2] != "..":
            path = tmp
    return path

def joinFPathFull(main, to_join):
    """
    :meta private:
    """
    return os.path.join(main, to_join).replace(os.sep, '/')

def getFileName(input):
    """
    :meta private:
    """
    from pathlib import Path 
    return Path(input).name

def getGlobalRootDir():
    """
    :meta private:
    """
    current_dir = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(current_dir, os.pardir)).replace(os.sep, '/')

def getParentDir(file_abs):
    """
    :meta private:
    """
    current_dir = os.path.dirname(file_abs)
    return os.path.abspath(os.path.join(current_dir, os.pardir)).replace(os.sep, '/')

def getAncestorDir(file_abs, num_of_gen=0):
    """
    :meta private:
    """
    ancestor_dir = os.path.dirname(file_abs)
    gen_count = 0
    while gen_count < int(num_of_gen):
        gen_count += 1
        ancestor_dir = os.path.abspath(os.path.join(ancestor_dir, os.pardir))
    return ancestor_dir.replace(os.sep, '/')

def getBool(input_string):
    """
    :meta private:
    """
    res = False
    if input_string.lower() == "true":
        res = True
    elif input_string.lower() == "false":
        res = False
    else:
        raise ValueError("getBool() -> Can't covert {} to a boolean.".format(input_string))
    return res

def getFloat(input_string, default_val=0.0, ignore_raise=True):
    """
    :meta private:
    """
    res = default_val
    try:
        res = float(input_string)
    except ValueError:
        msg = "The input can't be converted to float."
        if ignore_raise:
            print("IGNORE RAISE : " + msg)
        else:
            raise ValueError(msg)
    return res

def getInt(input_string, default_val=0, ignore_raise=True):
    """
    :meta private:
    """
    res = default_val
    try:
        res = int(input_string)
    except ValueError:
        msg = "The input can't be converted to int."
        if ignore_raise:
            print("IGNORE RAISE : " + msg)
        else:
            raise ValueError(msg)
    return res

def get2Dlist(input_string):
    """
    :meta private:
    """
    input_string = input_string.replace("[", "")
    input_string = input_string.replace("]", "")
    input_string = input_string.replace(" ", "")
    input_list = input_string.split(",")
    return [int(float(input_list[0])), int(float(input_list[1]))]

def to_xywh(box_xyxy):
    """
    :meta private:
    """
    box_xywh = box_xyxy.copy()
    box_xywh[2] = box_xywh[2] - box_xywh[0]
    box_xywh[3] = box_xywh[3] - box_xywh[1]
    return box_xywh

def to_xyxy(box_xywh):
    """
    :meta private:
    """
    ret = box_xywh.copy()
    ret[2:] += ret[:2]
    return ret

def silencer(func):
    """
    :meta private:
    """
    def func_wrapper(*args, **kwargs):
        sys.stdout = open(os.devnull, 'w')
        value = func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return value
    return func_wrapper
