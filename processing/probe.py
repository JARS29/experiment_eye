import numpy as np
import time
import os
from detectors import fixation_detection, saccade_detection
from gazeplotter import draw_fixations, draw_heatmap, draw_scanpath, draw_raw

#######################################
##
## Load data (raw and rt)
st, x, y = np.loadtxt('raw_eye.txt', delimiter=';', unpack=True)
st_rt, rt = np.loadtxt('rt.txt', delimiter=';', unpack=True)
##
##

##
## extracting eye data for each sentence (dictionary)
ind = 0
raw_sent = {}
data = {}
lensent = 1
st_rt = st_rt.tolist()
rt = rt.tolist()

for i in st_rt[1:]:
    data['x'] = []
    data['y'] = []
    data['st'] = []
    while i != st[ind]:
        data['x'].append(x[ind])
        data['y'].append(y[ind])
        data['st'].append(st[ind])
        ind += 1
    raw_sent['sent_' + str(lensent)] = data.copy()
    data.clear()
    lensent += 1
    if i == st_rt[-1]:
        data['x'] = []
        data['y'] = []
        data['st'] = []
        while ind < len(st):
            data['x'].append(x[ind])
            data['y'].append(y[ind])
            data['st'].append(st[ind])
            ind += 1
            if x[ind + 1] - x[ind] > 600 and x[ind] > 1200 and x[ind] < 1800:
                st_rt.append(st[ind])
                rt.append(1.0)
                break
        raw_sent['sent_' + str(lensent)] = data.copy()
        data.clear()
##
##

## extracting RT and time for each sentence (list)

time_key = []
time_eye = []

for i in range(1, len(raw_sent)):
    time_eye.append(raw_sent['sent_' + str(i)]['st'][-1] - raw_sent['sent_' + str(i)]['st'][0])
for i in range(0, len(st_rt) - 1):
    if rt[i + 1] == 1 and rt[i] == 0:
        time_key.append([st_rt[i + 1] - st_rt[i], 0])
    else:
        time_key.append([st_rt[i + 1] - st_rt[i], 1])


        ##
        ## Average Eye data for n subjects


        # st=np.array(raw_sent['sent_98']['st'])
        # x=np.array(raw_sent['sent_98']['x'])
        # y=np.array(raw_sent['sent_98']['y'])

        # Sfix,Efix= fixation_detection(x,y,st)
        # Ssac,Esac= saccade_detection(x,y,st)
        # scrsize=(2560,1440)
        # DIR = os.path.join(os.path.dirname(__file__), "images", "94.png")
        #
        # draw_raw(x,y,scrsize, imagefile='original.jpg', savefilename=os.path.join(os.path.dirname(__file__),"raw_data"))
        #
        # draw_fixations(Efix, scrsize, imagefile='original.png',durationsize=True, durationcolour=False,
        # alpha=0.5,savefilename=os.path.join(os.path.dirname(__file__),"fixations"))
#
# draw_scanpath(Efix, Esac, scrsize, imagefile='99.png', alpha=0.5,
#               savefilename=os.path.join(os.path.dirname(__file__),"scanpath"))
#
#
# draw_heatmap(Efix, scrsize,imagefile='99.png',durationweight=True,alpha=0.5,savefilename=os.path.join(os.path.dirname(__file__),"heatmap"))
