import cv2
from vsensebox import VSense
from vsensebox.utils.visualizetools import draw_boxes


# Input video file
input_video = "../examples/gta.mp4"
cap = cv2.VideoCapture(input_video)

# Create a VSense object
vs = VSense()

frame_index = 0 # Frame index
stop_after = 9 # Stop the test after 9 frames

# Loop each frame
while cap.isOpened():

    hasFrame, frame = cap.read()
    if hasFrame:

        # Detect object using local YAML config file 
        vs.detect(img=frame, img_is_mat=True)

        # Track object using internal YAML config file
        vs.track(img=frame, img_is_mat=True)
        
        # Draw bounding boxes of the detected objects
        frame = draw_boxes(
            frame, ids=vs.assets.ids, 
            boxes_xyxy=vs.assets.boxes_xyxy, 
            boxes_conf=vs.assets.boxes_conf
        )

        # Save frame as jpg
        cv2.imwrite("tests_outputs/test_01_frame_" + str(frame_index) + ".jpg", frame)
        frame_index += 1

        if frame_index == stop_after:
            break
    else:
        break

cap.release()
