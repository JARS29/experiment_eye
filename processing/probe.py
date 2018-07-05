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
    # type = 0 returns the sentence data (raw),
    # type = 1 returns the eye and rt (times),
    # type = 2 returns eye data (fixations and saccades) only for the sentences (without wait times),
    # type = 3 returns eye data (fixations and saccades) for all images (with wait times)
    usr_sent = {}
    usr_time={}
    cond= {}
    times = {}
    usr_eye_data={}
    eye_data={}
    #Windows
    #dir= 'C:\Users\JARS\Dropbox'

    #LINUX
    #dir= '/home/jars/Dropbox'

    #PC LAB
    dir = 'C:\Users\CG\Dropbox'
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
                    w = (st_rt[k + 1] - st_rt[k])

                    z = ((raw[k+1]['st'][-1] - raw[k+1]['st'][0]))
                    if rt[k] == 0 and rt[k + 1] == 1:
                        times[h]['time_wait'].append(str(np.round(w,2)).replace('.',','))
                    else:
                        times[h]['time_key'].append(str(np.round(w, 2)).replace('.',','))
                        times[h]['time_eye'].append(str(np.round(z, 2)).replace('.',','))
                ult = (st[-1] - st_rt[-1])
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
                        count_fix = 0
                        #Center wrong fixation detection
                        if len(Efix) is not 0:
                            if (Efix[0][3]<= 1355 and Efix[0][3] >= 1130) and ( Efix[0][4] <= 760 and Efix[0][4] >= 596): #center area
                                Efix=Efix[1:]
                                Esac=Esac[1:]
                                Sfix=Sfix[1:]
                                Ssac=Ssac[1:]
                                ampl=ampl[1:]
                            #Double reading and final word saccade detection
                            for ind in range(len(Esac)):
                                if(Esac[ind][3]>=954 and Esac[ind][3]<=1964) and (Esac[ind][4]>=730 and Esac[ind][4]<=850): #final word area
                                    if(Esac[ind][5]>=18 and Esac[ind][5]<=918) and (Esac[ind][6]>=600 and Esac[ind][6]<=720):
                                        if(ind>=3): #Saccades index: After the third saccade

                                            ix=len(Esac)-ind#  difference
                                            if ix<6:
                                                print(["Eliminating saccades: ", j + 1, Esac[ind][3:]], len(Esac), ind)
                                                Esac = Esac[:-ix]
                                                Ssac = Ssac[:-ix]
                                                ampl = ampl[:-ix]
                                                if ix > 2:  # Holding the last fixation
                                                    Efix = Efix[:-ix]
                                                    Sfix = Sfix[:-ix]
                                            break
                            for ind in range(len(Efix)):
                                if (Efix[ind][3] <= 2200 and Efix[ind][3] >= 400) and (Efix[ind][4] <= 850 and Efix[ind][4] >= 730): #Innitial fixation at final word
                                    if (ind <= 3):
                                        if(Sfix[ind]>np.mean(Sfix)-np.std(Sfix)): #is it an aware fixation (longer than the mean of the fixations minus the standart deviation)
                                            print(["Fixation final word:  ", j+1, Sfix[ind], np.mean(Sfix),  ind])
                                            break
                                        else:
                                            if (ind>=1):  # were multiple short fixations?
                                                print(["Fixation final word double:  ", j + 1, Sfix[ind], np.mean(Sfix), ind])
                                                break
                                            else: # Elimiting wrong fixations at the final word.
                                                print(["Wrong final word fixation: ", j+1, Sfix[ind], np.mean(Sfix), ind])#final word strategy
                                                Efix = Efix[1:]
                                                Esac = Esac[1:]
                                                Sfix = Sfix[1:]
                                                Ssac = Ssac[1:]
                                                ampl = ampl[1:]
                                            break
                                elif (Efix[ind][3] <= 1500 ) and (Efix[ind][4] <= 740 and Efix[ind][4] >= 590): #Innitial fixations at the beginning (normal reading)
                                    if (ind <= len(Efix) / 2):
                                        count_fix = count_fix+1
                                        if((len(Efix)/2)-count_fix<=1):
                                            print(['Normal reading: ', j+1, count_fix, len(Efix)/2])
                                else:
                                    print (['Annormal reading: ', j+1])

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
    #Linux
    #dir='/home/jars/Dropbox/'

    #Windows - Laptop
    #dir= 'C:\Users\JARS\Dropbox'

    ##Windows - PC LAB
    dir = 'C:\Users\CG\Dropbox'

    #Default
    #dir = os.path.dirname('__file__')

    #PC Lab
    dir_s=  'C:\Users\CG\Pictures\exp'

    #dir_s='/home/jars/data_exp/images'
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
        if not os.path.exists(os.path.join(dir_s,condition,'sp',usr)):
            os.makedirs(os.path.join(dir_s,condition,'sp',usr))
        draw_scanpath(Efix, Esac, scrsize, imagefile=dirimage, alpha=0.5,
                      savefilename=os.path.join( dir_s, condition, 'sp', usr, str(sent)))
    elif type == 2:
        if not os.path.exists(os.path.join( dir_s,condition,'hm',usr)):
            os.makedirs(os.path.join(dir_s, condition, 'hm',usr))
        draw_heatmap(Efix, scrsize, imagefile=dirimage, durationweight=True, alpha=0.5,
                     savefilename=os.path.join(dir_s, condition, 'hm', usr, str(sent)))

def writing_data(data, subject, condition, type): #creates the csv's for processing the results (statistics in R)

    # Linux
    # dir='/home/jars/Dropbox/'

    # Windows - Laptop
    # dir= 'C:\Users\JARS\Dropbox'

    # Default
    # dir = os.path.dirname('__file__')

    # PC Lab
    #dir_s = 'C:\Users\CG\Pictures\exp\csv'

    dir = 'C:\Users\CG\Dropbox'

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
        with open('time_data_' + subject + '_' + condition + '.csv', 'wb') as newFile:
            newFileWriter = csv.writer(newFile, delimiter=';')
            newFileWriter.writerow(['answers','words','order','time_eye','time_key','time_wait'])
            for i in stack:
                newFileWriter.writerow(i)
    elif type==1:  #extracting results from eye data (saccades and fixations)

        with open('eye_data_' + subject + '_' + condition + '.csv', 'wb') as newFile:
            nfw = csv.writer(newFile, delimiter=';')
            nfw.writerow(['usr','condition','sentence','f/s','start','end','duration', 'amplitude'])
            for j in data[subject][condition]:
                fix=data[subject][condition][j]['dur_fix']
                sacc=np.hstack((data[subject][condition][j]['dur_sacc'],data[subject][condition][j]['amplitude']))
                sacc=sacc.tolist()
                if fix==[]:
                    fix=[[0,0,0]]
                if sacc==[]:
                    sacc=[[0,0,0]]
                for i in fix:
                    nfw.writerow([subject, condition, j, 'f'] + i + ['0'])
                for i in sacc:
                    nfw.writerow([subject, condition, j, 's'] + i)


subjects = ['005']#['004','005','006','007','009','010','011','012',
#'013','014','015','016','017','018','019','020','021','022','023','024','025','026','027']
condition= ['va']

raw_sent = extract_data_subjects(subjects, condition)
#times = extract_data_subjects(subjects, condition, 1)
eye_data = extract_data_subjects(subjects, condition, 2) #Use: eye_data['number of subject']['condition'][number of sentence] (view keys for the options)
#visualization_eye(eye_data,'003', 'va', 1, 1)
#visualization_eye(eye_data,'003', 'vs', 1, 1)
#visualization_eye(eye_data,'014', 'va', 6, 1)
#visualization_eye(eye_data,'022', 'vs', 17, 1)



# for i in subjects:
#    for j in condition:
#         #writing_data(eye_data,i,j,1)
#        for k in eye_data[i][j]:
#            visualization_eye(eye_data,i, j, k, 1)
           #visualization_eye(eye_data, i, j, k, 2)


####Center fixation filtering
