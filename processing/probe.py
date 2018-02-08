import numpy as np
import time
import os

from detectors import fixation_detection, saccade_detection
from gazeplotter import draw_fixations, draw_heatmap, draw_scanpath, draw_raw

eye_f = file('raw_eye.txt')
rt_f = file('rt.txt')
st_=[]
x_=[]
y_=[]
rt_=[]
for line in eye_f:
    col=line.split(';')
    col=[c.strip() for c in col]
    st_.append(float(col[0]))
    x_.append(float(col[1]))
    y_.append(float(col[2]))

    
st=np.array(st_)
x=np.array(x_)
y=np.array(y_)

Sfix,Efix= fixation_detection(x,y,st)
Ssac,Esac= saccade_detection(x,y,st)
scrsize=(2560,1440)
DIR = (os.path.dirname(__file__)+"capture.png")

draw_raw(x,y,scrsize, imagefile='original.jpg', savefilename=os.path.join(os.path.dirname(__file__),"raw_data"))

draw_fixations(Efix, scrsize, imagefile='original.jpg',durationsize=True, durationcolour=False,
               alpha=0.5,savefilename=os.path.join(os.path.dirname(__file__),"fixations"))

draw_scanpath(Efix, Esac, scrsize, imagefile='original.jpg', alpha=0.5,
              savefilename=os.path.join(os.path.dirname(__file__),"scanpath"))


draw_heatmap(Efix, scrsize,imagefile='original.jpg',durationweight=True,alpha=0.5,savefilename=os.path.join(os.path.dirname(__file__),"heatmap"))
