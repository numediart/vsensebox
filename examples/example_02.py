# Example 02: Detect and track objects with custom configs

import cv2
from vsensebox import VSense
from vsensebox.utils.visualizetools import draw_boxes


# Input video file
input_video = "gta.mp4"
cap = cv2.VideoCapture(input_video)

# Create a VSense object
vs = VSense()

# Loop each frame
while cap.isOpened():

    hasFrame, frame = cap.read()
    if hasFrame:

        # Detect object using local YAML config > yolo_ultralytics_v8n.yaml
        # More detector config files -> vsensebox/config/detectors
        vs.detect(img=frame, 
                  config_yaml="yolo_ultralytics_v8n.yaml", 
                  img_is_mat=True)

        # Track object using local YAML config -> sort.yaml
        # More tracker config files -> vsensebox/config/trackers
        vs.track(img=frame, 
                 config_yaml="sort.yaml", 
                 img_is_mat=True)
        
        # Draw bounding boxes of the detected objects
        frame = draw_boxes(
            frame, ids=vs.assets.ids, 
            boxes_xyxy=vs.assets.boxes_xyxy, 
            boxes_conf=vs.assets.boxes_conf
        )

        # Display
        cv2.imshow("VSenseBox: Example 02", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
