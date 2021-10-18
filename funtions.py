import  cv2
import numpy as np
from vidgear.gears import CamGear

options = {"CAP_PROP_BUFFERSIZE": 0,'THREADED_QUEUE_MODE': False}

def active_cam(camara):
    cap=[[0,1,0]]
    cap[0][1]=CamGear(source=camara,**options).start()# Galpon motos
    cap[0][2]= 'Hay una persona' 
    
    return cap

def read_camera (cap):
    frames=[[0,3]]
    for j ,i ,t in cap: 
        frames[j][0]=i.read()
        frames[j][1]= [t]
    return frames

def stop_cam(cap):
    cap[0][1].stop()

