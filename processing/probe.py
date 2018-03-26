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
def extract_data_subjects(subjects, condition, type=0):  # both lists of subjects and conditions  must be string,
    # type (sentence data) = 0, type (eye and key time) =1,  type (fixations and saccades data) = 2
    usr_sent = {}
    usr_time={}
    cond= {}
    times = {}
    usr_eye_data={}
    eye_data={}
    dir = os.path.dirname('__file__')
    #dir= 'C:\Users\JARS\Dropbox'
    for i in subjects:
        for h in condition:
            filename_eye = os.path.join(dir, 'data_exp', str(i), str(h), 'raw_eye.txt')
            filename_rt = os.path.join(dir, 'data_exp', str(i), str(h), 'rt.txt')
            st, x, y = import_eyedata(filename_eye)
            st_rt, rt = import_rtdata(filename_rt)
            raw = extracting_eye(st, x, y, st_rt, rt)
            cond[h] = raw.copy()
            if type == 1:
                times[h] = {}
                times[h]['time_eye']=[]
                times[h]['time_wait']=[]
                times[h]['time_key']=[]
                for k in range(0, len(rt) - 1):
                    w = (st_rt[k + 1] - st_rt[k]) / 1000
                    z = ((raw['sent_' + str(k+1)]['st'][-1] - raw['sent_' + str(k+1)]['st'][0]) / 1000)
                    if rt[k] == 0 and rt[k + 1] == 1:
                        times[h]['time_wait'].append(np.round(w,2))
                    else:
                        times[h]['time_key'].append(np.round(w, 2))
                        times[h]['time_eye'].append(np.round(z, 2))


            elif type ==2:
                eye_data[h]={}
                for k in raw:
                    eye_data[h][k]={}
                    eye_data[h][k]['fixations'] = []
                    eye_data[h][k]['saccades'] = []
                    st = np.array(raw[k]['st'])
                    x = np.array(raw[k]['x'])
                    y = np.array(raw[k]['y'])
                    Sfix, Efix = fixation_detection(x, y, st)
                    Ssac, Esac = saccade_detection(x, y, st)
                    eye_data[h][k]['fixations']=Efix
                    eye_data[h][k]['saccades'] = Esac
        usr_eye_data[i]=eye_data.copy()
        eye_data.clear()
        usr_time[i]=times.copy()
        times.clear()
        usr_sent[i]=cond.copy()
        cond.clear()
    if type==0:
        return usr_sent
    elif type==1:
        return usr_time
    elif type==2:
        return usr_eye_data

#
## Ploting
def visualization_eye(raw_sent, usr, condition, sent, type=0):  # Type: 0=fixation, 1=scanpath, 2=heatmap

    dir = os.path.dirname('__file__')
    Efix= raw_sent[usr][condition]['sent_'+sent]['fixations']
    Esac= raw_sent[usr][condition]['sent_'+sent]['saccades']
    scrsize = (2560, 1440)
    #print (Efix)
    #print (len(Efix))
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



subjects = ['004']
condition= ['vs', 'va']
#raw_sent = extract_data_subjects(subjects, condition)
times = extract_data_subjects(subjects, condition, 1)
#eye_data = extract_data_subjects(subjects, condition, 2)

#visualization_eye(eye_data, '014', 'vs', '99', 1)
#visualization_eye(raw_sent, '014', 'va', '99', 1)
#visualization_eye(raw_sent, '014', 'vs', '99', 2)
#visualization_eye(raw_sent, '014', 'va', '99', 2)
#visualization_eye(raw_sent, '010', 'vs', '40', 2)

# visualization_eye(raw_sent, '010', 'vs', '2', 1)
# visualization_eye(raw_sent, '010', 'vs', '2', 2)
#
# visualization_eye(raw_sent, '010', 'vs', '70', 1)
# visualization_eye(raw_sent, '010', 'vs', '70', 2)


