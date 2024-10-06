from vsensebox.config.configurator import DCFG_YOLOULT
from vsensebox.utils.commontools import joinFPathFull, getGlobalRootDir 


internal_root_dir = getGlobalRootDir()
internal_config_dir = joinFPathFull(internal_root_dir, 'config')
detectors_config_dir = joinFPathFull(internal_config_dir, 'detectors')

# Set "cpu"
config_yaml = joinFPathFull(detectors_config_dir, "yolo_ultralytics_v11n.yaml")
cfg = DCFG_YOLOULT(cfg=config_yaml, relative_to_vsensebox_root=True)
cfg.device = "cpu"
cfg.configs['device'] = "cpu"

# Hard overwrite
cfg.dumpDoc(output=config_yaml)

# Create a directory for tests' result
import os
os.makedirs("tests_outputs")
