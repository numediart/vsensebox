# Example 01: Detect objects with default/internal configs

import cv2
from vsensebox import VSense
from vsensebox.utils.visualizetools import draw_boxes


# Input image file
input_image = "gta.jpg"

# Create a VSense object
vs = VSense()

# Detect object using internal or default YAML config file
# See example_02.py for using custom or local config file :)
vs.detect(img=input_image, img_is_mat=False)

# All results are stored as `vs.assets`
results = vs.assets

# Draw bounding boxes of the detected objects
visual_image = draw_boxes(
    input_image, 
    ids=results.ids, 
    boxes_xyxy=results.boxes_xyxy, 
    boxes_conf=results.boxes_conf, 
    img_is_mat=False
)

# Display
cv2.imshow("VSenseBox: Example 01", visual_image)
cv2.waitKey(0)
