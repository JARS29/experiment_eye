import numpy as np
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
            while ind < len(st):
                data['x'].append(x[ind])
                data['y'].append(y[ind])
                data['st'].append(st[ind])
                ind += 1
            raw_sent['sent_' + str(lensent)] = data.copy()
            data.clear()
    return raw_sent


#
## Average Eye data for n subjects
def extract_data_subjects(subjects, condition, time_sent=0):  # both lists of subjects and conditions  must be string, sent= 0, time =1
    usr_sent = {}
    usr_time={}
    cond= {}
    times = {}
    dir = os.path.dirname('__file__')
    for i in subjects:
        for h in condition:
            filename_eye = os.path.join(dir, 'data_exp', i, h, 'raw_eye.txt')
            filename_rt = os.path.join(dir, 'data_exp', i, h, 'rt.txt')
            st, x, y = import_eyedata(filename_eye)
            st_rt, rt = import_rtdata(filename_rt)
            raw = extracting_eye(st, x, y, st_rt, rt)
            cond[h] = raw.copy()
            if time_sent == 1:
                times[h] = {}
                times[h]['time_eye']=[]
                times[h]['time_key']=[]
                for k in range(1, len(raw) + 1):
                    z = np.sum(np.diff(raw['sent_' + str(k)]['st']))/1000
                    times[h]['time_eye'].append(np.round(z, 2))
                z = np.diff(st_rt) / 1000
                times[h]['time_key'].append(np.round(z,2))
        usr_time[i]=times.copy()
        times.clear()
        usr_sent[i]=cond.copy()
        cond.clear()
    if time_sent:
        return usr_time
    else:
        return usr_sent

#
## Ploting
def visualization_eye(raw_sent, usr, condition, sent, type):  # Type: 0=fixation, 1=scanpath, 2=heatmap

    dir = os.path.dirname('__file__')
    st = np.array(raw_sent[usr][condition]['sent_' + sent]['st'])
    x = np.array(raw_sent[usr][condition]['sent_' + sent]['x'])
    y = np.array(raw_sent[usr][condition]['sent_' + sent]['y'])

    Sfix, Efix = fixation_detection(x, y, st)
    Ssac, Esac = saccade_detection(x, y, st)
    scrsize = (2560, 1440)
    print Esac
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



subjects = ['005']
condition= ['vs', 'va']
raw_sent = extract_data_subjects(subjects, condition)
times = extract_data_subjects(subjects, condition, 1)

