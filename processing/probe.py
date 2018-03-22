import numpy as np
import time
import os
from detectors import fixation_detection, saccade_detection
from gazeplotter import draw_fixations, draw_heatmap, draw_scanpath, draw_raw


#######################################

#
## Load data (raw and rt)
def import_eyedata(filename):
    st, x, y = np.loadtxt(filename, delimiter=';', unpack=True)
    return st, x, y


def import_rtdata(filename):
    st_rt, rt = np.loadtxt(filename, delimiter=';', unpack=True)
    st_rt = st_rt.tolist()
    rt = rt.tolist()
    return st_rt, rt


#
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
            print
            i, ind
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


#
## extracting RT and time for each sentence (list)
# def extracting_time(subjects, condition):
#
#     time_user={}
#     times={}
#     dir = os.path.dirname('__file__')
#     for i in subjects:
#             for h in condition:
#                 filename_eye = os.path.join(dir, 'data_exp', i, h, 'raw_eye.txt')
#                 filename_rt = os.path.join(dir, 'data_exp', i, h, 'rt.txt')
#                 st, x, y = import_eyedata(filename_eye)
#                 st_rt, rt = import_rtdata(filename_rt)
#                 raw_sent = extracting_eye(st, x, y, st_rt, rt)
#                 times[h + 'time_eye']= []
#                 times[h + 'time_key'] = []
#                 for j in range(1, len(raw_sent) + 1):
#                     y = (raw_sent['sent_' + str(j)]['st'][-1] - raw_sent['sent_' + str(j)]['st'][0]) / 1000
#                     time_eye.append(round(y, 2))
#                 times['time_eye_'+ i + '_'+ condition]= time_eye
#                 for k in range(0, len(st_rt)):
#                     if rt[k] == 1 and rt[k - 1] == 0:
#                         y = ((st_rt[k] - st_rt[k - 1]) / 1000)
#                         time_key.append([round(y, 2), 0])
#                     else:
#                         y = ((st_rt[k] - st_rt[k - 1]) / 1000)
#                         time_key.append([round(y, 2), 1])
#             times['time_key_'+ i + '_'+ condition]= time_key
#     return times

#
## Average Eye data for n subjects
def average_subjects(subjects, condition):  # condition= va or vs
    n_subj = len(subjects)
    usr = {}
    cond= {}
    dir = os.path.dirname('__file__')
    for i in subjects:
        for h in condition:
            filename_eye = os.path.join(dir, 'data_exp', i, h, 'raw_eye.txt')
            filename_rt = os.path.join(dir, 'data_exp', i, h, 'rt.txt')
            st, x, y = import_eyedata(filename_eye)
            st_rt, rt = import_rtdata(filename_rt)
            raw = extracting_eye(st, x, y, st_rt, rt)
            cond[h] = raw.copy()
        usr[i]=cond.copy()
        cond.clear()
    return usr

#
## Ploting
def visualization_eye(raw_sent, usr, condition, sent, type):  # Type: 0=fixation, 1=scanpath, 2=heatmap

    dir = os.path.dirname('__file__')
    st = np.array(raw_sent['raw_data_' + usr]['sent_' + sent]['st'])
    x = np.array(raw_sent['raw_data_' + usr]['sent_' + sent]['x'])
    y = np.array(raw_sent['raw_data_' + usr]['sent_' + sent]['y'])

    Sfix, Efix = fixation_detection(x, y, st)
    Ssac, Esac = saccade_detection(x, y, st)
    scrsize = (2560, 1440)
    dirimage = os.path.join(dir, 'data_exp', usr, condition, 'images', sent + '.png')
    if type == 0:
        draw_fixations(Efix, scrsize, imagefile=dirimage, durationsize=True, durationcolour=False, alpha=0.5,
                       savefilename=os.path.join(dir, usr + '_' + condition + '_' + sent + "_fixations"))
    elif type == 1:
        draw_scanpath(Efix, Esac, scrsize, imagefile=dirimage, alpha=0.5,
                      savefilename=os.path.join(dir, usr + '_' + condition + '_' + sent + "_scanpath"))
    elif type == 2:
        draw_heatmap(Efix, scrsize, imagefile=dirimage, durationweight=True, alpha=0.5,
                     savefilename=os.path.join(dir, usr + '_' + condition + '_' + sent + "_heatmap"))


# draw_raw(x,y,scrsize, imagefile='original.jpg', savefilename=os.path.join(os.path.dirname(__file__),"raw_data"))



subjects = ['004' , '007']
condition= ['va' , 'vs']
raw_sent = average_subjects(subjects, condition)
