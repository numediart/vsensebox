# Release Notes 

## **VSenseBox v0.1.x - One Small Step!**

* `VSenseBox` [v0.1.1](https://github.com/rathaumons/vsensebox/tree/v0.1.1)
  - Replace [`pyppbox-ultralytics`](https://github.com/rathaumons/ultralytics-for-pyppbox) with [`vsensebox-ultralytics`](https://github.com/rathaumons/ultralytics-for-vsensebox)
  - Use `lapx>=0.5.8` for speed boost
  - Update and improve documentation
  - Update GitHub workflow

* `VSenseBox` [v0.1.0](https://github.com/rathaumons/vsensebox/tree/v0.1.0)
  - Add basic IoU tracker -> `BasicIoU`
  - Fix minor bugs
  - Clean up and improve unified strings
  - Update and improve configurator and GUI
  - Update and improve documentation

## **VSenseBox v0.0.x - Hello World!**

* `VSenseBox` [v0.0.4](https://github.com/rathaumons/vsensebox/tree/v0.0.4)
  - Add minor bug fixes
  - Add example 03 for multithreading
  - Improve overall performance
  - Update and improve documentation

* `VSenseBox` [v0.0.3](https://github.com/rathaumons/vsensebox/tree/v0.0.3)
  - Improve `VSense` performance
  - Update and improve documentation

* `VSenseBox` [v0.0.2](https://github.com/rathaumons/vsensebox/tree/v0.0.2)
  - Add direct YAML file reading to `config()`
  - Update and improve documentation

* `VSenseBox` [v0.0.1](https://github.com/rathaumons/vsensebox/tree/v0.0.1)
  - Fix the wrong paths in yolo_classic *.yaml

* `VSenseBox` [v0.0.0](https://github.com/rathaumons/vsensebox/tree/v0.0.0)
  - Initialize first release 👋
  - Come with full [documentation](https://rathaumons.github.io/vsensebox/) 📄
  - Support both CPU and GPU ready 🚀
  - Support Python 3.9-3.12 on Windows, Linux, and macOS 🫶
  - Support multithreading 🛞
  - Support YAML config file ✍️
  - Integrate with PyQt GUI for easy config 🖱️
  - Integrate with object detectors and trackers 🤖
    - Built-in Classic YOLO v3 and v4 (.weights models)
    - PyTorch YOLO including Ultralytics v3, v4, v5, v8, v9
    - Built-in bbox trackers including Centroid, SORT, and DeepSORT
