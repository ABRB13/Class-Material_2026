#class and objects 
#constructors 
#instance and class attributes 
#static methods 
#encapsualtion 
#decorators 
#inheritance 
#multiple inheritance 
#method overiding 
#polymorphism 
#magic methods (operator overloading)
#super()

import tkinter as tk
from PIL import Image, ImageTk  # image processing
import cv2  # mostly for advanced image and video processing 

class WebcamApp:
    def __init__(self, window):
        self.window = window
        self.window.title("OpenCV, Pillow, and Tkinter")
        
        self.cap = cv2.VideoCapture(0)
        self.label = tk.Label(window)
        self.label.pack()
        
        self.update_frame()
    
    def update_frame(self):
        ret, frame = self.cap.read()
        
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert color to RGB
            frame = cv2.resize(frame, (640, 480))  # resize image
            
            img = Image.fromarray(frame)  # create new frame
            self.photo = ImageTk.PhotoImage(image=img)
            self.label.config(image=self.photo)
            
        self.window.after(10, self.update_frame)
    
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

root = tk.Tk()
app = WebcamApp(root)
root.mainloop()