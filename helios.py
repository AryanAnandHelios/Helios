import sys
import threading
import time

class Helios:

    def __init__(self):
        print("Starting helios...")
        
        # todo: Considerrunning start() in a thread.
        # self.thread = threading.Thread(target=start, args=(1,))
        # self.thread.start()

    def start(self):
        # This function runs in a thread to retrieve frames using opencv.
        # We then run inference on this frame and trigger the buzzes.
        
        #insert code to capture frame using opencv -> cvmat or numpy array
        
        # Make YOLO inference -> bounding boxes

        # Optionally display frame with bouding box overlay

        # Pass bounding boxes to buzzer function
        while (True):
            # Code goes here 
            time.sleep(0.067) # 67ms ~ 15fps 
            pass
    
def main(args=sys.args):
    app = Helios()
    app.start()


if __name__ == '__main__':
    main(sys.args)

