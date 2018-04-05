import numpy as np
import os
import csv
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
        raw_sent[lensent] = data.copy()
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
            raw_sent[lensent] = data.copy()
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
    #dir = os.path.dirname('__file__')
    #dir= 'C:\Users\JARS\Dropbox'
    dir= '/home/jars/Dropbox'
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

                    z = ((raw[k+1]['st'][-1] - raw[k+1]['st'][0]) / 1000)
                    if rt[k] == 0 and rt[k + 1] == 1:
                        times[h]['time_wait'].append(str(np.round(w,2)).replace('.',','))
                    else:
                        times[h]['time_key'].append(str(np.round(w, 2)).replace('.',','))
                        times[h]['time_eye'].append(str(np.round(z, 2)).replace('.',','))
                ult = (st[-1] - st_rt[-1])/1000
                times[h]['time_wait'].append(str(np.round(ult,2)).replace('.',','))
            elif type ==2: #extracting eye data for each sentence (80) Without wait
                eye_data[h]={}
                for j in range(0, len(rt) - 1):
                    if rt[j] == 0 and rt[j + 1] == 1:
                        pass
                    else:
                        k = j+1
                        eye_data[h][k]={}
                        eye_data[h][k]['fixations'] = []
                        eye_data[h][k]['saccades'] = []
                        eye_data[h][k]['dur_fix'] = []
                        eye_data[h][k]['dur_sacc']=[]
                        st = np.array(raw[k]['st'])
                        x = np.array(raw[k]['x'])
                        y = np.array(raw[k]['y'])
                        Sfix, Efix = fixation_detection(x, y, st)
                        Ssac, Esac = saccade_detection(x, y, st)
                        eye_data[h][k]['fixations']=Efix
                        eye_data[h][k]['saccades'] = Esac
                        eye_data[h][k]['dur_fix'] = Sfix
                        eye_data[h][k]['dur_sacc']= Ssac
            elif type == 3: #extracting eye data for all images (sentences + wait time)
                eye_data[h] = {}
                for k in raw:
                    eye_data[h][k] = {}
                    eye_data[h][k]['fixations'] = []
                    eye_data[h][k]['saccades'] = []
                    st = np.array(raw[k]['st'])
                    x = np.array(raw[k]['x'])
                    y = np.array(raw[k]['y'])
                    Sfix, Efix = fixation_detection(x, y, st)
                    Ssac, Esac = saccade_detection(x, y, st)
                    eye_data[h][k]['fixations'] = Efix
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
    elif type==2 or type==3:
        return usr_eye_data

#
## Ploting
def visualization_eye(raw_sent, usr, condition, sent, type=0):  # Type: 0=fixation, 1=scanpath, 2=heatmap

    #dir = os.path.dirname('__file__')
    dir= '/home/jars/Dropbox'
    Efix= raw_sent[usr][condition][sent]['fixations']
    Esac= raw_sent[usr][condition][sent]['saccades']
    scrsize = (2560, 1440)
    #print (Efix)
    #print (len(Efix))
    dirimage = os.path.join(dir, 'data_exp', usr, condition, 'images', str(sent) + '.png')
    if type == 0:
        draw_fixations(Efix, scrsize, imagefile=dirimage, durationsize=True, durationcolour=False, alpha=0.5,
                       savefilename=os.path.join(dir, usr + '_' + condition + '_' + str(sent) + "_fixations"))
    elif type == 1:
        draw_scanpath(Efix, Esac, scrsize, imagefile=dirimage, alpha=0.5,
                      savefilename=os.path.join(dir, usr + '_' + condition + '_' + str(sent) + "_scanpath"))
    elif type == 2:
        draw_heatmap(Efix, scrsize, imagefile=dirimage, durationweight=True, alpha=0.5,
                     savefilename=os.path.join(dir, usr + '_' + condition + '_' + str(sent) + "_heatmap"))


# draw_raw(x,y,scrsize, imagefile='original.jpg', savefilename=os.path.join(os.path.dirname(__file__),"raw_data"))

def writing_data(data, subject, condition, type): ###
    dir= '/home/jars/Dropbox'


    if type == 0: #extracting results from sente, order, times
        filename_ord = os.path.join(dir, 'data_exp', subject, condition, 'order.txt')
        filename_sen = os.path.join(dir, 'data_exp', subject, condition, 'sente.txt')
        order = np.loadtxt(filename_ord, unpack=True)
        sent, anw, word = np.genfromtxt(filename_sen, delimiter=';', dtype='str', unpack=True)
        idx = []
        for i in order:
            for j in range(int(i)):
                idx.append(int(i))
        tim_e=data[subject][condition]['time_eye']
        tim_k=data[subject][condition]['time_key']
        tim_w=data[subject][condition]['time_wait']
        for i in range(len(tim_e)-len(tim_w)):
            tim_w.append(0)
        #print len(tim_w), len(tim_e), len(tim_k), len(anw), len(word), len(idx)
        stack= np.stack((anw, word, idx,tim_e,tim_k,tim_w), axis=-1)
        with open('time_data_' + subject + '_' + condition + '.csv', 'w') as newFile:
            newFileWriter = csv.writer(newFile, delimiter=';')
            newFileWriter.writerow(['answers','words','order','time_eye','time_key','time_wait'])
            for i in stack:
                newFileWriter.writerow(i)
    elif type==1:  #extracting results from eye data
        with open('eye_data_' + subject + '_' + condition + '.csv', 'w') as newFile:
            nfw = csv.writer(newFile, delimiter=';')
            for j in data[subject][condition]:
                fix=data[subject][condition][j]['dur_fix']
                sacc=data[subject][condition][j]['dur_sacc']
                nfw.writerow('0'+str(j))
                for i in fix:
                    nfw.writerow(i)
                nfw.writerow("###")
                for i in sacc:
                    nfw.writerow(i)



subjects = ['002','003','004','005','006','007','009','010',
            '011','012','013','014','015','016','017','018',
            '019','020','021','022','023','024','025','026','027']
condition= [ 'vs', 'va']
#raw_sent = extract_data_subjects(subjects, condition)
times = extract_data_subjects(subjects, condition, 1)
#tim= extract_data_subjects(subjects,condition,1)
#eye_data = extract_data_subjects(['003'], condition, 3)
for i in subjects:
# #     if i=='008':
# #         pass
# #     else:
     #print i
     writing_data(times, i, 'vs', 0)
     writing_data(times, i, 'va', 0)



#writing_data(eye_data,'004','vs',1)


#visualization_eye(eye_data, '004', 'va', 17, 2)




#visualization_eye(eye_data, '002', 'vs', 99, 1)
#visualization_eye(eye_data, '002', 'vs', 98, 1)

#visualization_eye(eye_data, '002', 'vs', 99, 1)
#visualization_eye(eye_data, '003', 'va', 99, 1)
#visualization_eye(eye_data, '003', 'vs', 99, 1)


#visualization_eye(eye_data, '004', 'vs', 24, 2)
