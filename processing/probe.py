import numpy as np
import time
import os
from detectors import fixation_detection, saccade_detection
from gazeplotter import draw_fixations, draw_heatmap, draw_scanpath, draw_raw


#######################################
##
## Load data (raw and rt)


def import_eyedata(filename):
    st, x, y = np.loadtxt(filename, delimiter=';', unpack=True)
    return st, x, y


def import_rtdata(filename):
    st_rt, rt = np.loadtxt(filename, delimiter=';', unpack=True)
    st_rt = st_rt.tolist()
    rt = rt.tolist()
    return st_rt, rt


##
## extracting eye data for each sentence (dictionary)

def extracting_eye(st, x, y, st_rt, rt):
    ind = 0
    raw_sent = {}
    data = {}
    lensent = 1

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
            print i, ind
            while ind < len(st):
                data['x'].append(x[ind])
                data['y'].append(y[ind])
                data['st'].append(st[ind])
                ind += 1
                if x[ind - 1] - x[ind - 2] > 500 and 1200 < x[ind - 1] < 1400:
                    st_rt.append(st[ind])
                    rt.append(1.0)
                    break
            raw_sent['sent_' + str(lensent)] = data.copy()
            data.clear()
    return raw_sent


##
##

## extracting RT and time for each sentence (list)

def extracting_time(raw_sent, rt, st_rt):
    time_key = []
    time_eye = []

    for i in range(1, len(raw_sent) + 1):
        y = (raw_sent['sent_' + str(i)]['st'][-1] - raw_sent['sent_' + str(i)]['st'][0]) / 1000
        time_eye.append(round(y, 2))

    for i in range(0, len(st_rt)):
        if rt[i] == 1 and rt[i - 1] == 0:
            y = ((st_rt[i] - st_rt[i - 1]) / 1000)
            time_key.append([round(y, 2), 0])
        else:
            y = ((st_rt[i] - st_rt[i - 1]) / 1000)
            time_key.append([round(y, 2), 1])

#
## Average Eye data for n subjects

def average_subjects(subjects, condition):  #condition= va or vs
    n_subj= len(subjects)
    usr={}
    dir=os.path.dirname('__file__')
    for i in subjects:
        filename_eye= os.path.join(dir, 'data_exp', i, condition , 'raw_eye.txt')
        filename_rt= os.path.join(dir, 'data_exp', i, condition , 'rt.txt')
        st, x, y = import_eyedata(filename_eye)
        st_rt, rt =import_rtdata(filename_rt)
        raw = extracting_eye(st,x,y,st_rt,rt)
        usr['raw_data_'+i]=raw.copy()
    return usr
        
subjects=['007']
raw_sent=average_subjects(subjects, 'va')
    
    




## Ploting (individual)



st=np.array(raw_sent['raw_data_007']['sent_13']['st'])
x=np.array(raw_sent['raw_data_007']['sent_13']['x'])
y=np.array(raw_sent['raw_data_007']['sent_13']['y'])

Sfix,Efix= fixation_detection(x,y,st)
Ssac,Esac= saccade_detection(x,y,st)
scrsize=(2560,1440)
# DIR = os.path.join(os.path.dirname(__file__), "images", "94.png")
#
# draw_raw(x,y,scrsize, imagefile='original.jpg', savefilename=os.path.join(os.path.dirname(__file__),"raw_data"))
#
# draw_fixations(Efix, scrsize, imagefile='original.png',durationsize=True, durationcolour=False,
# alpha=0.5,savefilename=os.path.join(os.path.dirname(__file__),"fixations"))
#
draw_scanpath(Efix, Esac, scrsize, imagefile='13.png', alpha=0.5,
               savefilename=os.path.join(os.path.dirname(__file__),"scanpath"))
#
#
draw_heatmap(Efix, scrsize,imagefile='13.png',durationweight=True,alpha=0.5,savefilename=os.path.join(os.path.dirname(__file__),"heatmap"))
