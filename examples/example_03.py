# Example 03: Detect and track objects in multithreading

import cv2
import threading
from vsensebox import VSense
from vsensebox.utils.visualizetools import draw_boxes


def detect_and_track(vsense, input_video, det_yaml, trk_yaml, name="Detect & Track"):
    
    # Read video
    cap = cv2.VideoCapture(input_video)
    
    # Loop each frame
    while cap.isOpened():

        hasFrame, frame = cap.read()
        if hasFrame:

            # Detect object using local YAML config
            vsense.detect(img=frame, 
                    config_yaml=det_yaml, 
                    img_is_mat=True)

            # Track object using local YAML config
            vsense.track(img=frame, 
                    config_yaml=trk_yaml, 
                    img_is_mat=True)
            
            # Draw bounding boxes of the detected objects
            frame = draw_boxes(
                frame, ids=vsense.assets.ids, 
                boxes_xyxy=vsense.assets.boxes_xyxy, 
                boxes_conf=vsense.assets.boxes_conf
            )

            # Display
            cv2.imshow("VSenseBox: Example 03 - " + name, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()


if __name__ == '__main__':

    vs1 = VSense()
    vs2 = VSense()

    vs1_thread = threading.Thread(
        target=detect_and_track, 
        args=(vs1, "gta.mp4", "yolo_ultralytics_v8n.yaml", "sort.yaml", "VSense 1")
    )

    vs2_thread = threading.Thread(
        target=detect_and_track, 
        args=(vs2, "gta.mp4", "yolo_ultralytics_v8n.yaml", "centroid.yaml", "VSense 2")
    )

    vs1_thread.start()
    vs2_thread.start()
    vs1_thread.join()
    vs2_thread.join()

