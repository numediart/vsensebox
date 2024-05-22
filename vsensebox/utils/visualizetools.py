# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import cv2

from .commontools import getCVMat
from .logtools import add_warning_log

def draw_boxes(img, 
               ids=[], 
               show_ids=True, 
               boxes_xyxy=[], 
               boxes_conf=[], 
               boxes_color=(255, 255, 0), 
               boxes_thickness=2, 
               text_color=(150, 200, 50), 
               text_font=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
               text_font_scale=1, 
               text_thickness=1, 
               img_is_mat=True):
    """Draw the boxes add other decorations for the detected objects in the given image. 

    Parameters
    ----------
    img : str or Mat
        An image file or a :obj:`Mat` like object.
    show_ids : bool, default=True
        Whether to visualize the IDs.
    boxes_xyxy : list[[X1, Y1, X2, Y2], ...], default=[]
        A list of bounding boxes; for example, [[X1, Y1, X2, Y2], [X1, Y1, X2, Y2], ...].
    boxes_conf : list[float, ...], default=[]
        A list of detection confidences corresponding to bounding boxes.
    boxes_color : tuple(int, int, int), default=(255, 255, 0)
        Color space of bounding boxes.
    boxes_thickness : int, default=2
        Thickness of bounding boxes.
    text_color : tuple(int, int, int), default=(150, 200, 50)
        Color space of the texts for IDs and confs.
    text_font : int, default=cv2.FONT_HERSHEY_COMPLEX_SMALL
        Font of the texts for IDs and confs.
    text_font_scale : int, default=1
        Font scale of the texts for IDs and confs.
    text_thickness : int, default=2
        Thickness of the texts for IDs and confs.
    img_is_mat : bool, default=True
        Speed up the function by telling whether the :obj:`img` is :obj:`Mat` like object.
    
    Returns
    -------
    Mat
        A visualized :obj:`Mat` like object.
    """
    if img_is_mat and isinstance(img, str): img_is_mat = False
    if not img_is_mat: img = getCVMat(img)
    len_boxes = len(boxes_xyxy)
    if show_ids and len_boxes != len(ids) and len(ids) > 0:
        add_warning_log("VSenseBox:draw_boxes() -> Numbers of IDs and boxes are different!")
        show_ids = False
    if show_ids and len(ids) == 0:
        ids = [i for i in range(0, len_boxes)]
    for i in range(0, len_boxes):
        cv2.rectangle(
            img, 
            (int(boxes_xyxy[i][0]), int(boxes_xyxy[i][1])), (int(boxes_xyxy[i][2]), int(boxes_xyxy[i][3])), 
            boxes_color, 
            boxes_thickness
        )
        conf = 0.0
        try:
            conf = format(boxes_conf[i], '.2f')
            cv2.putText(img, str(conf), (int(boxes_xyxy[i][0]) + 5, int(boxes_xyxy[i][3]) - 5), 
                        text_font, text_font_scale, text_color, text_thickness)
        except Exception as e:
            add_warning_log("VSenseBox:draw_boxes() -> Numbers of confs and boxes are different!")
        if show_ids: 
            cv2.putText(img, "#" + str(ids[i]), (int(boxes_xyxy[i][0]), int(boxes_xyxy[i][1] - 5)), 
                        text_font, text_font_scale, text_color, text_thickness)
    return img
