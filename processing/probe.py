import numpy as np
import time
import os
from detectors import fixation_detection, saccade_detection
from gazeplotter import draw_fixations, draw_heatmap, draw_scanpath, draw_raw

#eye_f = file('raw_eye.txt')
#rt_f = file('rt.txt')
st, x, y = np.loadtxt('raw_eye.txt', delimiter = ';',  unpack=True)
st_, rt = np.loadtxt('rt.txt', delimiter = ';',  unpack=True)
st_1=st_[np.isin(rt,1)]
st_0=st_[np.isin(rt,0)]
it = np.nditer(st, flags=['f_index'])
it_1=np.nditer(st_1, flags=['f_index'])
it_0=np.nditer(st_0, flags=['f_index'])
index_1=[]
index_0=[]
#print(it_1[0], it_0[0])
it_1.iternext()


while not it.finished:
    if it_1.finished==False:
        if it[0]==it_1[0]:
            print(it_1[0])

            #print(it.index)
            index_1.append(it.index)
            it_1.iternext()
    if it_0.finished==False:
        if it[0]==it_0[0]:
            index_0.append(it.index)
            it_0.iternext()

    it.iternext()
    if it_1.finished and it_0.finished:
        break

#print(x[0:index_1[0]+1])
#print(index_0, len(index_0))
#print(it_1, len(index_1))
st_=[]
x_=[]
y_=[]
rt_=[]

# for line in eye_f:
#     col=line.split(';')
#     col=[c.strip() for c in col]
#     st_.append(float(col[0]))
#     x_.append(float(col[1]))
#     y_.append(float(col[2]))

    
# st=np.array(st_)
# x=np.array(x_)
# y=np.array(y_)

# Sfix,Efix= fixation_detection(x,y,st)
# Ssac,Esac= saccade_detection(x,y,st)
# scrsize=(2560,1440)
# DIR = (os.path.dirname(__file__)+"capture.png")
#
# draw_raw(x,y,scrsize, imagefile='original.jpg', savefilename=os.path.join(os.path.dirname(__file__),"raw_data"))
#
# draw_fixations(Efix, scrsize, imagefile='original.jpg',durationsize=True, durationcolour=False,
#                alpha=0.5,savefilename=os.path.join(os.path.dirname(__file__),"fixations"))
#
# draw_scanpath(Efix, Esac, scrsize, imagefile='original.jpg', alpha=0.5,
#               savefilename=os.path.join(os.path.dirname(__file__),"scanpath"))
#
#
# draw_heatmap(Efix, scrsize,imagefile='original.jpg',durationweight=True,alpha=0.5,savefilename=os.path.join(os.path.dirname(__file__),"heatmap"))
