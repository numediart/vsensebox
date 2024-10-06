# 🚀 Getting Started

Installing `VSenseBox` is very easy and straightforward. You can install from [PyPI](https://pypi.org/project/vsensebox/) directly or use the prebuilt `.whl` files on [GitHub releases](https://github.com/numediart/vsensebox/releases) or install from GitHub directly or build it from source on your own machine. However, in order to get it work, you need to install all the necessary dependencies or requirements for the modules you need.

## ⚙️ Requirements

All requirements are not strictly limited. However, some specific modules might need some special dependencies; for example, `YOLO_Classic` (With `.weights` model) runs faster using [OpenCV DNN](https://docs.opencv.org/4.x/d2/d58/tutorial_table_of_content_dnn.html) with GPU. In this case, you might need to build OpenCV from source with GPU support or use our [`pyppbox-opencv`](https://github.com/rathaumons/opencv-for-pyppbox) instead of the official `opencv-contrib-python`.

* Prerequisite: 
  - Python [[3.9-3.12]](https://www.python.org/downloads/)
  - Local `VSenseBox` repo: `git clone https://github.com/numediart/vsensebox.git`

* Before you install dependencies/requirements:
  - For Linux, recommend changing `python3` to `python`: `sudo apt install python-is-python3`
  - If you prefer conda + Python [3.9-3.12]: `conda create --name vsensebox_env python=3.11`
  - Upgrade `pip` and `setuptools`:
    ```
    python -m pip install --upgrade pip
    pip install "setuptools>=67.2.0"
    ```
  - Recommend uninstalling the official `Ultralytics`: 
    ```
    pip uninstall -y ultralytics
    ```

* Install dependencies/requirments under `vsensebox/requirements/`: 
  - On Windows:
    - With GPU:
      ```
      pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
      pip install -r requirements.txt
      ```
    - For CPU-only:
      ```
      pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
      pip install -r requirements.txt
      ```
  - On Linux:
    - With GPU:
      ```
      python -m pip install tensorflow[and-cuda] # TensorFlow GPU
      pip install torch torchvision torchaudio
      pip install -r requirements.txt
      ```
    - For CPU-only:
      ```
      python -m pip install tensorflow # TensorFlow CPU
      pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
      pip install -r requirements.txt
      ```
  - On macOS:
    - With GPU: Not available!
    - For CPU:
      ```
      pip install torch torchvision torchaudio
      pip install -r requirements.txt
      ```

* ***ATTENTION ⚠️⚠️⚠️***
  - Default configurations of `VSenseBox` are set to use GPU, and to switch to CPU, you need to set `cpu` as string for the parameter `device` in the YAML config file; for example, line #8 in [`yolo_ultralytics_v8s.yaml`](https://github.com/numediart/vsensebox/blob/main/vsensebox/config/detectors/yolo_ultralytics_v8s.yaml).


## 💽 Setup

`vsensebox` is the main package and if you use the classic YOLO detectors and DeepSORT tracker, etc., you need to also install `vsensebox-data-xxx`.

* Install `vsensebox`
  - Download and install the latest wheel in GitHub [releases](https://github.com/numediart/vsensebox/releases) or install from [PyPI](https://pypi.org/project/vsensebox/):
    ```
    pip install vsensebox
    ``` 
  - Or install directly from GitHub:
    ```
    pip install git+https://github.com/numediart/vsensebox.git
    ```
  - Or build from source:
    ```
    pip install setuptools wheel build PyYAML
    python -m build --wheel --skip-dependency-check --no-isolation
    ```

* Install [`vsensebox-data-xxx`](https://github.com/numediart/vsensebox-data/)
  - Download the latest from GitHub [releases](https://github.com/numediart/vsensebox-data/releases) and install
  - Or install the ones you need directly from the links below:
    ```
    pip install https://github.com/numediart/vsensebox-data/releases/download/v0.0.0/vsensebox_data_yolocls-0.0.0-py3-none-any.whl
    pip install https://github.com/numediart/vsensebox-data/releases/download/v0.0.2/vsensebox_data_yoloult-0.0.2-py3-none-any.whl
    pip install https://github.com/numediart/vsensebox-data/releases/download/v0.0.0/vsensebox_data_deepsort-0.0.0-py3-none-any.whl
    ```

* Let's try some basic features of `VSenseBox`
  - Configurator GUI can be called in Python terminal:
    ```
    import vsensebox
    vsensebox.config()
    ```
    Now you should see the Configurator GUI like in this scheenshot:
    <img src="https://raw.githubusercontent.com/rathaROG/screenshot/refs/heads/master/VSenseBox/vsensebox_config_gui.jpg">
  - You can also easily reset the internal configurations by calling the `reset()`. **THIS CAN'T BE REVERSED!** ⚠️
    ```
    vsensebox.reset()
    ```
  - For the details of GUI functions and configurations, check [Configurations page](https://numediart.github.io/vsensebox/vsensebox/config.html).
  - Check the [Examples page](https://numediart.github.io/vsensebox/examples.html) for some real coding!
* For ***Linux***, if the GUI does not work, you might need to install these:
  ```
  sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
  ```
* For ***Ubuntu on WSL 2***, if the GUI does not work, you need to install these:
  ```
  sudo apt-get install libgl1-mesa-glx xdg-utils libegl1
  ```

## 📢 FYI

### 1️⃣ Customized OpenCV

OpenCV is widely used in many well-known packages, but the majority of the prebuilt WHLs on the Internet including the official one on PyPI do not include GPU support. Thus, we build our custom one which includes NVIDIA [CUDA](https://developer.nvidia.com/cuda-downloads) & [cuDNN](https://developer.nvidia.com/rdp/cudnn-download) supports for the [OpenCV DNN module](https://docs.opencv.org/4.x/d2/d58/tutorial_table_of_content_dnn.html). In order to well distinguish from the rest, we decided to build and change the package name from `opencv-contrib-python` to [`pyppbox-opencv`](https://github.com/rathaumons/opencv-for-pyppbox) -> [[Repo]](https://github.com/rathaumons/opencv-for-pyppbox) [[WHL]](https://github.com/rathaumons/opencv-for-pyppbox/releases)

### 2️⃣ Customized Ultralytics

Also, similar to `pyppbox-opencv`, our custom `ultralytics` is changed to [`vsensebox-ultralytics`](https://github.com/numediart/ultralytics-for-vsensebox), but this time, the module name is still the same `ultralytics` and it is the main reason why the official `ultralytics` must be removed. Find out more why `VSenseBox` needs the customized `vsensebox-ultralytics` -> [[Repo]](https://github.com/numediart/ultralytics-for-vsensebox) [[PyPI]](https://pypi.org/project/vsensebox-ultralytics/)
