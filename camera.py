"""
Capture and stream video
"""
from __future__ import print_function
import cv2
import numpy as np



class Video(object):
    """
    Class to capture video and sen the frame
    """
    def __init__(self, source=0):
        """
        if source is 0, captures video from the device camera
        if source is path to video file, captures video from source file
        """
        self.video = cv2.VideoCapture(source)
        self.shown = False  

    def __del__(self):
        self.video.release()

    def get_frame(self):
        """
        Since opencv captures raw images, we should encode it
        into JPEG
        Returns image as byte stream.

        """
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        if not success:
            raise Exception
        
        return self._convet_to_byte_stream(image), image
    
    def _convet_to_byte_stream(self, image):
        ret, jpeg = cv2.imencode('.jpg', image)
        if not ret:
            raise Exception
        
        return jpeg.tobytes()

 
    def save_image(self, image):
        """
        Save the frame(byte stream) to a specified location
        """

        # CV2
        cv2.imwrite("newimage.jpg", image)
        

    def display_video(self):
        """
        Display video in opencv destroyAllWindows
        """
        while True:
            ret, img = self.video.read()
            print(ret)

            cv2.imshow("input", img)

            key = cv2.waitKey(10)
            if key == 27:
                break
        cv2.destroyAllWindows()
        self.video.release()
