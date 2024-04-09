# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import cv2

from vsensebox.utils.commontools import to_xyxy


class YOLO_Classic(object):

    """Class used as a custom layer or interface for interacting with detector module 
    YOLO_Classic which uses :code:`.weights` model.
    
    Attributes
    ----------
    cfg : DCFG_YOLOCLS
        A :class:`DCFG_YOLOCLS` object which manages the configurations of detector 
        YOLO_Classic.
    model: cv::dnn::DetectionModel
        A detection model object of OpenCV's deep learning network.
    """

    def __init__(self, cfg):
        """Initialize according to the given configuration :obj:`cfg` 
        as :class:`DCFG_YOLOCLS` object.

        Parameters
        ----------
        cfg : DCFG_YOLOCLS
            A :class:`DCFG_YOLOCLS` object which manages the configurations of detector 
            YOLO_Classic.
        """
        self.cfg = cfg
        net = cv2.dnn.readNet(cfg.model_file, cfg.model_cfg_file)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(cfg.imgsz, cfg.imgsz), scale=1/255.0)

    def detect(self, img):
        """Detect general object with object's class filter :obj:`classes` in a 
        given :obj:`Mat` like object.

        Parameters
        ----------
        img : Mat
            A :obj:`Mat` like object.

        Returns
        -------
        Mat
            A :obj:`Mat` like object.
        list[ndarray[int int int int], ...]
            A list of bounding box :code:`ndarray[x y width height]`.
        list[ndarray[int int int int], ...]
            A list of bounding box :code:`ndarray[x1 y1 x2 y2]`.
        list[]
            A list of detected bodies' keypoints.
        list[float]
            A list of the detection confidence of every detected object.
        list[int]
            A list of detection classes.
        """
        boxes_xywh = []
        boxes_xyxy = []
        keypoints = []
        confs = []
        cls = []
        if self.cfg.classes is None:
            self.cfg.classes = [i for i in range(0, 80)]
        _classes, confidences, boxes = self.model.detect(
            img, 
            confThreshold=float(self.cfg.conf), 
            nmsThreshold=float(self.cfg.nms)
        )
        if len(boxes) > 0:
            for cl, conf, box_xywh in zip(_classes.flatten(), confidences, boxes):
                if cl in self.cfg.classes and box_xywh[2] >= self.cfg.min_width:
                    box_xywh = box_xywh.astype(int)
                    boxes_xywh.append(box_xywh)
                    box_xyxy = to_xyxy(box_xywh)
                    boxes_xyxy.append(box_xyxy)
                    confs.append(float(conf))
                    cls.append(int(cl))
        return img, boxes_xywh, boxes_xyxy, keypoints, confs, cls
