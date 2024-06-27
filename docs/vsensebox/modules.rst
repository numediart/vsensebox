.. _supportedmodules-page:

Supported Modules
=================

The table below shows all the current supported modules which are integrated in **VSenseBox** in many different ways. The main idea of this toolbox is to connect all visual/vision modules and to make them work well together so that they can be ultilized in various applications with minimal coding. **Not all original features of every supported module are fully functioning** as this toolbox focuses on application; for example, the supported `YOLO_Classic` and `YOLO Ultralytics` modules in the table below can only be used as object detectors (Inference/Prediction) using the native or official **`.weights`** or **`.pt`** files, and you can't train a custom module with custom dataset because `VSenseBox` does not provides such feature.

| 

.. table:: 
   :widths: auto

   +------------+--------------+------------------+-------------------------------------------------+
   | Modules    | General Name | Config Name      | Details                                         |
   +============+==============+==================+=================================================+
   | Detectors  | YOLO         | YOLO_Classic     | | * Built-in by using OpenCV DNN                |
   |            |              |                  | | * Model: .weights `v2, v3`_, v4_              |
   |            |              |                  | | * Run on: CPU or GPU (OpenCV DNN)             |
   |            |              +------------------+-------------------------------------------------+
   |            |              | YOLO_Ultralytics | | * Integrated by linking `ultralytics`_        |
   |            |              |                  | | * Model: .pt `v3, v5, v8, v9`_, v10_          |
   |            |              |                  | | * Run on: CPU or GPU (PyTorch)                |
   +------------+--------------+------------------+-------------------------------------------------+
   | Trackers   | Centroid     | Centroid         | | * Built-in / Native                           |
   |            |              |                  | | * Run on: CPU                                 |
   |            +--------------+------------------+-------------------------------------------------+
   |            | SORT         | SORT             | | * Integrated by embedding                     |
   |            |              |                  | | * `SORT repo`_                                |
   |            |              |                  | | * Run on: CPU                                 |
   |            +--------------+------------------+-------------------------------------------------+
   |            | DeepSORT     | DeepSORT         | | * Integrated by embedding                     |
   |            |              |                  | | * `DeepSORT repo`_                            |
   |            |              |                  | | * Run on: CPU or GPU (Tensorflow)             |
   |            +--------------+------------------+-------------------------------------------------+
   |            | BasicIoU     | BasicIoU         | | * Built-in / Native                           |
   |            |              |                  | | * Run on: CPU or GUP (PyTorch)                |
   +------------+--------------+------------------+-------------------------------------------------+

.. _v2, v3: https://pjreddie.com/darknet/yolo/
.. _V4: https://github.com/AlexeyAB/darknet
.. _ultralytics: https://github.com/numediart/ultralytics-for-vsensebox
.. _v3, v5, v8, v9: https://github.com/ultralytics/assets/releases
.. _v10: https://github.com/THU-MIG/yolov10/releases
.. _SORT repo: https://github.com/abewley/sort
.. _DeepSORT repo: https://github.com/deshwalmahesh/yolov7-deepsort-tracking

| 

.. toctree::
   :maxdepth: 2

   modules/detectors
   modules/trackers

|
