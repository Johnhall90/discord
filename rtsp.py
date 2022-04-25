#!/usr/bin/python3
import cv2,time,threading
from datetime import datetime
imagesFolder = "/home/jhall/Pictures"


def get_frame(imagesFolder):
    cap = cv2.VideoCapture("rtsp://jhall:j1690h1990@192.168.1.106/live")
    ret, frame = cap.read()

    filename = imagesFolder + "/pooky" + ".jpg"
    cv2.imwrite(filename, frame)
    cap.release()
    print ("Done!")
    cv2.destroyAllWindows()

def capture(imagesFolder):
    #cap = cv2.VideoCapture("rtsp://username:password@cameraIP/axis-media/media.amp")
    # Use public RTSP Streaming for testing:
    cap = cv2.VideoCapture("rtsp://jhall:j1690h1990@192.168.1.106/live")
    #cap = cv2.VideoCapture("test2.mp4")
    frameRate = cap.get(5) #frame rate

    cur_time = time.time()  # Get current time

    # start_time_24h measures 24 hours
    start_time_24h = cur_time

    # start_time_1min measures 1 minute
    start_time_1min = cur_time - 59  # Subtract 59 seconds for start grabbing first frame after one second (instead of waiting a minute for the first frame).
    while cap.isOpened():
        frameId = cap.get(1)  # current frame number
        ret, frame = cap.read()

        if (ret != True):
            break

        cur_time = time.time()  # Get current time
        elapsed_time_1min = cur_time - start_time_1min  # Time elapsed from previous image saving.

        # If 60 seconds were passed, reset timer, and store image.
        if elapsed_time_1min >= 60:
            # Reset the timer that is used for measuring 60 seconds
            start_time_1min = cur_time

            filename = imagesFolder + "/pooky" + ".jpg"
            #filename = "image_" + str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))  + ".jpg"
            cv2.imwrite(filename, frame)

        elapsed_time_24h = time.time() - start_time_24h

        #Break loop after 24*60*60 seconds
        if elapsed_time_24h > 24*60*60:
            break

    cap.release()
    print ("Done!")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    #threading.Thread(target=capture(imagesFolder)).start()
    get_frame(imagesFolder)