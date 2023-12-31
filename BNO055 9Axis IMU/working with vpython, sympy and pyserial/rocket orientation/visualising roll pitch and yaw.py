from vpython import *
from time import sleep
import math
import numpy as np
import serial


scene.range = 10
scene.width=1280
scene.height=600
scene.forward=vector(-1,-1,-1)

#conversion factors
to_deg=180/np.pi
to_rad=1/to_deg

arr_len= 4
xarrow = arrow(axis=vector(1, 0, 0), length=arr_len,shaftwidth=.1, color=color.red)     #x axis
yarrow = arrow(axis=vector(0, 1, 0), length=arr_len,shaftwidth=.1, color=color.green)   #y axis
zarrow = arrow(axis=vector(0, 0, 1), length=arr_len,shaftwidth=.1, color=color.blue)    #z aixs

frontarrow = arrow(axis=vector(1, 0, 0), length=6,shaftwidth=.1, color=color.purple)    #x' axis
uparrow = arrow(axis=vector(0, 1, 0), length=3,shaftwidth=.1, color=color.yellow)       #y' axis
sidearrow = arrow(axis=vector(0, 0, 1), length=2,shaftwidth=.1, color=color.orange)     #z' axis

breadBoard = box(length=10, width=2, height=.2, color=color.white)
ardBoard = box(pos=vector(-3,.1,0),length=3, width=1.3, height=.2, color=color.green)
IMUsensor = box(pos=vector(-.5,.1,0),length=1.5, width=1.3, height=.2, color=color.blue)
my_obj= compound([breadBoard,ardBoard,IMUsensor])

while True:
    rate(50)
    pitch=15*to_rad #theta
    roll= 30*to_rad #phi

    for yaw in np.arange(0,2*np.pi,.01):
        rate(50)
        fa=vector(cos(pitch)*cos(yaw), sin(pitch), cos(pitch)*sin(yaw))
        sa=vector(-cos(roll)*sin(yaw), sin(roll), cos(roll)*cos(yaw))
        ua=cross(sa, fa)
        print(sa)

        frontarrow.axis=fa
        frontarrow.length=6
        sidearrow.axis=sa
        sidearrow.length=2
        uparrow.axis=ua
        uparrow.length=3

        my_obj.axis=fa
        my_obj.up=ua


