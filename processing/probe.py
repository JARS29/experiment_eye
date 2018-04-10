import numpy as np
import os
import csv
from detectors import fixation_detection, saccade_detection
from gazeplotter import draw_fixations, draw_heatmap, draw_scanpath


def import_eyedata(filename): #import the eye-tracking data
    st, x, y = np.loadtxt(filename, delimiter=';', unpack=True)
    return st, x, y


def import_rtdata(filename): #import the reaction time data
    st_rt, rt = np.loadtxt(filename, delimiter=';', unpack=True)
    st_rt = st_rt.tolist()
    rt = rt.tolist()
    return st_rt, rt


def extracting_eye(st, x, y, st_rt, rt): #creates the dictionary of the raw data (RT and eye)
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

def extract_data_subjects(subjects, condition, type=0): #Extract the data for n number de subjects and condition (silently or aloudly)
    # both lists of subjects and conditions  must be string,
    # type = 0 returns the sentence data (raw), type=1 returns the eye and rt time
    # type = 2 returns eye data (fixations and saccades) only for the sentences (without wait times),
    # type = 3 returns eye data (fixations and saccades) for all images (with wait times)
    usr_sent = {}
    usr_time={}
    cond= {}
    times = {}
    usr_eye_data={}
    eye_data={}
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
            if type == 1: #extracting the time data (eye and rt)
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
                        eye_data[h][j+1]={}
                        eye_data[h][j+1]['fixations'] = []
                        eye_data[h][j+1]['saccades'] = []
                        eye_data[h][j+1]['dur_fix'] = []
                        eye_data[h][j+1]['dur_sacc']=[]
                        eye_data[h][j+1]['amplitude'] = []
                        st = np.array(raw[j+1]['st'])
                        x = np.array(raw[j+1]['x'])
                        y = np.array(raw[j+1]['y'])
                        Sfix, Efix = fixation_detection(x, y, st)
                        Ssac, Esac, ampl = saccade_detection(x, y, st)
                        eye_data[h][j+1]['fixations']=Efix
                        eye_data[h][j+1]['saccades'] = Esac
                        eye_data[h][j+1]['dur_fix'] = Sfix
                        eye_data[h][j+1]['dur_sacc']= Ssac
                        eye_data[h][j+1]['amplitude'] = ampl

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
                    Ssac, Esac, ampl = saccade_detection(x, y, st)
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

def visualization_eye(raw_sent, usr, condition, sent, type=0):  # Export the heapmaps and scanpaths. Type: 0=fixation, 1=scanpath, 2=heatmap
    dir='/home/jars/Dropbox/'
    #dir = os.path.dirname('__file__')
    dir_s='data_exp/images'
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
        if not os.path.exists(os.path.join(dir, dir_s,condition,'sp',usr)):
            os.makedirs(os.path.join(dir, dir_s,condition,'sp',usr))
        draw_scanpath(Efix, Esac, scrsize, imagefile=dirimage, alpha=0.5,
                      savefilename=os.path.join(dir, dir_s, condition, 'sp', usr, str(sent)))
    elif type == 2:
        if not os.path.exists(os.path.join(dir, dir_s,condition,'hm',usr)):
            os.makedirs(os.path.join(dir,dir_s, condition, 'hm',usr))
        draw_heatmap(Efix, scrsize, imagefile=dirimage, durationweight=True, alpha=0.5,
                     savefilename=os.path.join(dir,dir_s, condition, 'hm', usr, str(sent)))

def writing_data(data, subject, condition, type): #creates the csv's for processing the results (statistics in R)
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
        stack= np.stack((anw, word, idx,tim_e,tim_k,tim_w), axis=-1)
        with open('time_data_' + subject + '_' + condition + '.csv', 'w') as newFile:
            newFileWriter = csv.writer(newFile, delimiter=';')
            newFileWriter.writerow(['answers','words','order','time_eye','time_key','time_wait'])
            for i in stack:
                newFileWriter.writerow(i)
    elif type==1:  #extracting results from eye data (saccades and fixations)

        with open('eye_data_' + subject + '_' + condition + '.csv', 'w') as newFile:
            nfw = csv.writer(newFile, delimiter=';')
            nfw.writerow(['usr','condition','sentence','f/s','start','end','duration', 'amplitude', 'saccade'])
            for j in data[subject][condition]:
                fix=data[subject][condition][j]['dur_fix']
                sacc=data[subject][condition][j]['dur_sacc']
                ampl=data[subject][condition][j]['amplitude']
                if fix==[]:
                    fix=[[0,0,0]]
                if sacc==[]:
                    sacc=[[0,0,0]]
                for i in fix:
                    nfw.writerow([subject, condition, j, 'f'] + i + ['0','0'])
                for i,k in sacc, ampl:
                    nfw.writerow([subject, condition, j, 's'] + i + k)



subjects = ['002']#,'003','004','005','006','007','009','010',
            #'011','012','013','014','015','016','017','018',
            #'019','020','021','022','023','024','025','026','027']
condition= [ 'vs', 'va']

#raw_sent = extract_data_subjects(subjects, condition)
#times = extract_data_subjects(subjects, condition, 1)
eye_data = extract_data_subjects(subjects, condition, 2)

for i in subjects:
    for j in condition:
        writing_data(eye_data,i,j,1)
#          for k in eye_data[i][j]:
# #             print k
#             print (i, j, k)
#             visualization_eye(eye_data,i, j, k, 2)
#             visualization_eye(eye_data, i, j, k, 1)
