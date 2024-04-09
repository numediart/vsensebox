# VSenseBox - Python toolbox for visual sensing
# GNU General Public License v3 or later (GPLv3+)
# Copyright (C) 2024 UMONS-Numediart


import cv2

from vsensebox.utils.commontools import to_xywh
from vsensebox.utils.logtools import ignore_this_logger


class YOLO_Ultralytics(object):

    """Class used as a custom layer or interface for interacting with 
    detector YOLO Ultralytics which uses PyTorch .pt model.

    Attributes
    ----------
    cfg : DCFG_YOLOULT
        A :class:`DCFG_YOLOULT` object which manages the configurations 
        of detector YOLO_Ultralytics.
    model: ultralytics.yolo.engine.YOLO
        A detection model object of YOLO_Ultralytics.
    """

    def __init__(self, cfg):
        """Initialize according to the given configuration :obj:`cfg` 
        as :class:`DCFG_YOLOULT` object.

        Parameters
        ----------
        cfg : DCFG_YOLOULT
            A :class:`DCFG_YOLOULT` object which manages the configurations 
            of detector YOLO_Ultralytics.
        """
        self.cfg = cfg
        self.cpu_only = False
        if isinstance(self.cfg.device, str):
            if self.cfg.device.lower() == 'cpu':
                self.cpu_only = True
        ignore_this_logger("ultralytics")
        if "nas" in self.cfg.model_file:
            # YOLO NAS isn't stable yet :/
            from ultralytics import NAS
            self.model = NAS(self.cfg.model_file)
        else:
            from ultralytics import YOLO
            self.model = YOLO(self.cfg.model_file)

    def detect(self, img):
        """Detect general object with object's class filter :obj:`classes` 
        in a given :obj:`Mat` like object.

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
        numpy_dets = []
        boxes_xyxy = []
        boxes_xywh = []
        keypoints = []
        confs = []
        cls = []
        dets = self.model.predict(
            img,
            imgsz=int(self.cfg.imgsz),
            conf=float(self.cfg.conf),
            classes=self.cfg.classes,
            show_boxes=False,
            device=self.cfg.device,
            max_det=int(self.cfg.max_det),
            line_width=self.cfg.line_width,
            verbose=False
        )
        if self.cpu_only:
            numpy_dets = dets[0].numpy()
        else:
            numpy_dets = dets[0].cuda().cpu().to("cpu").numpy()
        dt_boxes_xyxy = numpy_dets.boxes.xyxy
        dt_confidences = numpy_dets.boxes.conf
        dt_classes = numpy_dets.boxes.cls
        dt_keypoints = dets[0].keypoints
        if dt_keypoints is not None:
            for box_xyxy, conf, kp, cl in zip(dt_boxes_xyxy, dt_confidences, 
                                          reversed(dt_keypoints), dt_classes):
                box_xyxy = box_xyxy.astype(int)
                box_xywh = to_xywh(box_xyxy)
                if box_xywh[2] >= self.cfg.min_width:
                    boxes_xywh.append(box_xywh)
                    boxes_xyxy.append(box_xyxy)
                    keypoint = kp.data[0]
                    keypoints.append(keypoint)
                    confs.append(float(conf))
                    cls.append(int(cl))
        elif len(dt_boxes_xyxy) > 0:
            for box_xyxy, conf, cl in zip(dt_boxes_xyxy, dt_confidences, dt_classes):
                box_xyxy = box_xyxy.astype(int)
                box_xywh = to_xywh(box_xyxy)
                if box_xywh[2] >= self.cfg.min_width:
                    boxes_xywh.append(box_xywh)
                    boxes_xyxy.append(box_xyxy)
                    confs.append(float(conf))
                    cls.append(int(cl))
        return img, boxes_xywh, boxes_xyxy, keypoints, confs, cls
