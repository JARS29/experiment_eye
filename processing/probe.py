import numpy as np
import os
import csv
from detectors import fixation_detection, saccade_detection
from gazeplotter import draw_fixations, draw_heatmap, draw_scanpath

###deleting reading file (due the append)
try:
    os.remove('reading_data_va.csv')
except OSError:
    pass
try:
    os.remove('reading_data_vs.csv')
except OSError:
    pass
###

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
                eye_data[h]['reading'] = []
                eye_data[h]['reading'].append(i)
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
                            #If the three first saccades are in the center (due to the recall time)
                            if (Efix[0][3]<= 1355 and Efix[0][3] >= 1130) and ( Efix[0][4] <= 760 and Efix[0][4] >= 596): #center area
                                Efix=Efix[1:]
                                Esac=Esac[1:]
                                Sfix=Sfix[1:]
                                Ssac=Ssac[1:]
                                ampl=ampl[1:]
                        else:
                            #print(["Wrong data A", j+1])
                            eye_data[h]['reading'].append(0)
                            continue

                        if len(Efix) is not 0:
                            #If the three first saccades are in the center (due to the recall time)
                            if (Efix[0][3]<= 1355 and Efix[0][3] >= 1130) and ( Efix[0][4] <= 760 and Efix[0][4] >= 596): #center area
                                Efix=Efix[1:]
                                Esac=Esac[1:]
                                Sfix=Sfix[1:]
                                Ssac=Ssac[1:]
                                ampl=ampl[1:]
                        else:
                            #print(["Wrong data B", j+1])
                            eye_data[h]['reading'].append(0)
                            continue

                        if len(Efix) is not 0:
                            #If the three first saccades are in the center (due to the recall time)
                            if (Efix[0][3]<= 1355 and Efix[0][3] >= 1130) and ( Efix[0][4] <= 760 and Efix[0][4] >= 596): #center area
                                Efix=Efix[1:]
                                Esac=Esac[1:]
                                Sfix=Sfix[1:]
                                Ssac=Ssac[1:]
                                ampl=ampl[1:]
                        else:
                            #print(["Wrong data C", j+1])
                            eye_data[h]['reading'].append(0)
                            continue

                        if len(Esac) is not 0:
                            #Double reading and final word saccade detection
                            for ind in range(len(Esac)):
                                if(Esac[ind][3]>=954 and Esac[ind][3]<=1964) and (Esac[ind][4]>=730 and Esac[ind][4]<=850): #final word area
                                    if(Esac[ind][5]>=18 and Esac[ind][5]<=918) and (Esac[ind][6]>=600 and Esac[ind][6]<=720):
                                        if(ind>=3): #Saccades index: After the third saccade

                                            ix=len(Esac)-ind#  difference
                                            if ix<=6:
                                                #print(["Eliminating saccades: ", j + 1, Esac[ind][3:]], len(Esac), ind)
                                                Esac = Esac[:-ix]
                                                Ssac = Ssac[:-ix]
                                                ampl = ampl[:-ix]
                                                if ix > 4:  # Holding the last fixation
                                                    Efix = Efix[:-ix+2]
                                                    Sfix = Sfix[:-ix+2]
                                            break
                        if len(Efix) is not 0:
                            for ind in range(len(Efix)):
                                if (ind <= 3):
                                    if (Efix[ind][3] <= 2200 and Efix[ind][3] >= 400) and (
                                            Efix[ind][4] <= 850 and Efix[ind][4] >= 730):  # Innitial fixation at final word

                                            if (Sfix[ind] > np.mean(Sfix) - np.std(Sfix)):  # is it an aware fixation (longer than the mean of the fixations minus the standart deviation)
                                                # print(["Fixation final word:  ", j+1, Sfix[ind], np.mean(Sfix),  ind])
                                                eye_data[h]['reading'].append(2)
                                                break
                                            else:
                                                if (ind >= 1):  # were multiple short fixations?
                                                    # print(["Fixation final word double:  ", j + 1, Sfix[ind], np.mean(Sfix), ind])
                                                    eye_data[h]['reading'].append(2)

                                                    break
                                                else:  # Elimiting wrong fixations.
                                                    # print(["Wrong final word fixation: ", j+1, Sfix[ind], np.mean(Sfix), ind])#final word wrong (due the last fixation in the previous sentence)
                                                    Efix = Efix[1:]
                                                    Esac = Esac[1:]
                                                    Sfix = Sfix[1:]
                                                    Ssac = Ssac[1:]
                                                    ampl = ampl[1:]
                                                    eye_data[h]['reading'].append(4)


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

def writing_data(data, subject, condition, typ): #creates the csv's for processing the results (statistics in R)

    # Linux
    # dir='/home/jars/Dropbox/'

    # Windows - Laptop
    # dir= 'C:\Users\JARS\Dropbox'

    # Default
    # dir = os.path.dirname('__file__')

    # PC Lab
    #dir_s = 'C:\Users\CG\Pictures\exp\csv'

    dir = 'C:\Users\CG\Dropbox'

    if typ == 0: #extracting results from sente, order, times
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
    elif typ == 1:  #extracting results from eye data (saccades and fixations)

        with open('eye_data_' + subject + '_' + condition + '.csv', 'wb') as newFile:
            nfw = csv.writer(newFile, delimiter=';')
            nfw.writerow(['usr','condition','sentence','f/s','duration', 'amplitude'])
            for j in sorted(data[subject][condition]):
                if type(j) == int:
                    fix=data[subject][condition][j]['dur_fix']
                    dur_sac=data[subject][condition][j]['dur_sacc']
                    amp_sac=data[subject][condition][j]['amplitude']
                    if fix==[]:
                        fix=[[0,0,0]]
                    if amp_sac == [] or dur_sac == []:
                        sacc=[[0,0,0]]
                    else:
                        sacc = np.concatenate([dur_sac, amp_sac], axis=1)
                        sacc=sacc.tolist()

                    for i in fix:
                        nfw.writerow([subject, condition, j, 'f'] + i + ['0'])
                    for i in sacc:
                        nfw.writerow([subject, condition, j, 's'] + i)

        if condition == 'va':
            with open('reading_data_va.csv', 'ab+') as readvaFile:
                rvaf = csv.writer(readvaFile, delimiter=';')
                rvaf.writerow(data[subject]['va']['reading'])
        elif condition == 'vs':
            with open('reading_data_vs.csv', 'ab+') as readvsFile:
                rvsf = csv.writer(readvsFile, delimiter=';')
                rvsf.writerow(data[subject]['vs']['reading'])

def visual_inspection(eye_data, subject, condition, sent, fix, sacc):

    if len(fix) !=0:
        eye_data[subject][condition][sent]['fixations'] = eye_data[subject][condition][sent]['fixations'][fix[0]:fix[1]]
        eye_data[subject][condition][sent]['dur_fix'] = eye_data[subject][condition][sent]['dur_fix'][fix[0]:fix[1]]

    if len(sacc) !=0:
        eye_data[subject][condition][sent]['saccades'] = eye_data[subject][condition][sent]['saccades'][sacc[0]:sacc[1]]
        eye_data[subject][condition][sent]['dur_sacc'] = eye_data[subject][condition][sent]['dur_sacc'][sacc[0]:sacc[1]]
        eye_data[subject][condition][sent]['amplitude'] = eye_data[subject][condition][sent]['amplitude'][sacc[0]:sacc[1]]

    return eye_data


subjects = ['004', '005', '007', '009','012','014','015','016','017','018',
            '020','021','022','023','024','027']
condition= ['vs']

#raw_sent = extract_data_subjects(subjects, condition)

#times = extract_data_subjects(subjects, condition, 1)
eye_data = extract_data_subjects(subjects, condition, 2) #Use: eye_data['number of subject']['condition'][number of sentence] (view keys for the options)


#################################
####   Visual inspection     ####
#################################

#Double reading: DR
#Final fixation error: FFE

####004

# eye_data= visual_inspection(eye_data, '004', 'va', 1, [1,17], [1,-5]) #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 2, [0,11], [0,-1]) #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 7, [0,6], [0,-4])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 10, [0,12], [0,-4])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 14, [0,13], [0,-4])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 15, [0,13], [0,-4])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 20, [0,15], [0,-6])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 24, [0,14], [0,-1])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 28, [0,15], [0,-4])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 29, [1,15], [2,-1])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 32, [1,14], [0,-3])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 33, [0,14],[])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 35, [1,14],[2,-1])  #FFE
# eye_data= visual_inspection(eye_data, '004', 'va', 37, [0,11],[0,-4])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 38, [0,12],[1,-3])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 39, [],[0,-2])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 42, [1,12],[2,-1])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 44, [0,15],[0,-4])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 45, [0,11],[])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 46, [0,11],[0,-5])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 48, [0,13],[0,-3])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 51, [1,16],[4,1111])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 53, [1,14],[2,-1])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 59, [0,16],[0,-5])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 61, [0,11],[0,-3])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 62, [0,12],[0,-2])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 63, [1,18],[2,1111])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 67, [1,15],[1,1111])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 69, [1,15],[1,-1])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 72, [0,15],[1,1234])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 73, [0,11],[])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 74, [0,12],[0,-1])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 76, [0,11],[0,-2])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 77, [0,17],[])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 78, [0,26],[])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 80, [1,12],[3,-4])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 82, [0,8],[0,-2])  #DR **
# eye_data= visual_inspection(eye_data, '004', 'va', 83, [0,15],[])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 85, [0,11],[0,1111])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 87, [1,14],[1,-1])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 88, [1,11],[1,-1])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 89, [1,14],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 93, [0,10],[])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 95, [1,12],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '004', 'va', 98, [0,19],[])  #DR

#
# eye_data= visual_inspection(eye_data, '004', 'vs', 14, [1,24],[3,-2])
# eye_data= visual_inspection(eye_data, '004', 'vs', 17, [1,24],[1,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 20, [1,24],[2,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 23, [0,-1],[])
# eye_data= visual_inspection(eye_data, '004', 'vs', 27, [0,-1],[0,-3])
# eye_data= visual_inspection(eye_data, '004', 'vs', 30, [],[2,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 32, [1,111],[1,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 34, [1,111],[2,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 36, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '004', 'vs', 37, [1,111],[2,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 39, [1,111],[2,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 40, [1,111],[1,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 41, [1,111],[1,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 45, [1,111],[1,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 48, [1,111],[2,-2])
# eye_data= visual_inspection(eye_data, '004', 'vs', 49, [1,111],[1,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 57, [1,111],[3,-2])
# eye_data= visual_inspection(eye_data, '004', 'vs', 59, [1,111],[1,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 62, [1,111],[2,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 63, [1,111],[3,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 68, [1,111],[2,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 72, [],[1,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 74, [1,111],[3,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 76, [1,111],[2,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 77, [1,111],[2,111])
# eye_data= visual_inspection(eye_data, '004', 'vs', 82, [],[1,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 83, [],[3,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 84, [1,111],[1,-1])
# eye_data= visual_inspection(eye_data, '004', 'vs', 88, [1,12],[2,111])



####005
# eye_data= visual_inspection(eye_data, '005', 'va', 2, [0,15],[0,-1])  #DR
# eye_data= visual_inspection(eye_data, '005', 'va', 3, [],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'va', 4, [1,15],[1,-1])  #DR
# eye_data= visual_inspection(eye_data, '005', 'va', 59, [1,12],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'va', 87, [],[0,-1])  #DR
# eye_data= visual_inspection(eye_data, '005', 'va', 94, [],[0,-1])  #DR


# eye_data= visual_inspection(eye_data, '005', 'vs', 4, [1,111],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 10, [2,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 16, [1,111],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 20, [1,111],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 21, [1,111],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 24, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 38, [2,111],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 58, [3,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 64, [1,111],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 65, [],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 70, [],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 77, [2,111],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 79, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 80, [1,111],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 83, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '005', 'vs', 88, [1,111],[1,111])  #DR



####007 check double reading in vs (up  boundary)
# eye_data= visual_inspection(eye_data, '007', 'va', 13, [0,12],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 23, [1,13],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 24, [1,8],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 27, [1,13],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 35, [1,17],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 39, [1,17],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 49, [1,17],[])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 64, [1,17],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 70, [1,8],[1,-3])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 81, [1,9],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 94, [1,9],[])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 99, [1,14],[1,111])  #DR

# eye_data= visual_inspection(eye_data, '007', 'va', 1, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 3, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 5, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 12, [3,111],[5,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 13, [1,111],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 14, [1,111],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 15, [1,111],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 18, [1,111],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 26, [],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 30, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 33, [1,111],[4,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 37, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 38, [1,111],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 51, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 56, [1,111],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 58, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 60, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 64, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 65, [1,111],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '007', 'va', 72, [1,111],[3,111])  #DR


####009

# eye_data= visual_inspection(eye_data, '009', 'va', 2, [0,17],[])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 6, [1,15],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 9, [2,21],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 18, [1,17],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 19, [2,17],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 24, [1,14],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 26, [1,12],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 27, [2,18],[3,-1])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 48, [1,20],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 57, [1,15],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 58, [1,10],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 83, [1,18],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 88, [1,18],[2,-1])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 95, [3,18],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 96, [1,15],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '009', 'va', 99, [1,15],[2,111])  #DR

#### 012

# eye_data= visual_inspection(eye_data, '012', 'va', 3, [1,14],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 12, [1,22],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 13, [1,14],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 17, [1,20],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 22, [0,10],[])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 27, [1,18],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 33, [1,18],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 37, [1,17],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 44, [1,15],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 63, [2,19],[4,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 78, [1,12],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 82, [1,22],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 86, [],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 87, [1,21],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 89, [1,18],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '012', 'va', 95, [1,18],[2,111])  #DR

####014

# eye_data= visual_inspection(eye_data, '014', 'va', 4, [],[0,-2])  #DR **
# eye_data= visual_inspection(eye_data, '014', 'va', 7, [1,15],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 8, [1,13],[1,-1])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 13, [1,15],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 19, [1,22],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 24, [2,15],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 29, [1,16],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 51, [],[5,111])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 70, [1,14],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 73, [],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 80, [1,15],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 82, [3,20],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '014', 'va', 93, [1,19],[4,111])  #DR


####015

# eye_data= visual_inspection(eye_data, '015', 'va', 11, [1,18],[2,111])
# eye_data= visual_inspection(eye_data, '015', 'va', 15, [1,15],[2,111])
# eye_data= visual_inspection(eye_data, '015', 'va', 21, [1,17],[2,111])
# eye_data= visual_inspection(eye_data, '015', 'va', 23, [1,14],[2,111])
# eye_data= visual_inspection(eye_data, '015', 'va', 24, [1,15],[1,111])
# eye_data= visual_inspection(eye_data, '015', 'va', 27, [2,20],[2,111])
# eye_data= visual_inspection(eye_data, '015', 'va', 30, [1,20],[1,111])
# eye_data= visual_inspection(eye_data, '015', 'va', 31, [1,15],[1,111])
# eye_data= visual_inspection(eye_data, '015', 'va', 35, [1,18],[1,111])
# eye_data= visual_inspection(eye_data, '015', 'va', 40, [0,12],[1,-6]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 42, [0,17],[]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 54, [1,17],[1,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 63, [1,17],[2,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 67, [1,19],[2,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 70, [1,19],[1,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 71, [1,19],[3,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 72, [1,24],[4,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 73, [1,24],[5,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 74, [],[1,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 78, [1,13],[1,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 84, [1,13],[2,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 91, [2,15],[3,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 95, [2,17],[2,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 98, [2,19],[3,111]) ###
# eye_data= visual_inspection(eye_data, '015', 'va', 99, [2,19],[]) ###

####016

# eye_data= visual_inspection(eye_data, '016', 'va', 1, [1,20],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 4, [1,20],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 5, [1,16],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 7, [1,19],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 8, [1,15],[4,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 9, [1,15],[4,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 10, [1,10],[3,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 11, [1,15],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 12, [2,15],[5,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 14, [2,18],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 17, [1,111],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 20, [1,111],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 27, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 31, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 32, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 33, [1,111],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 36, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 37, [1,111],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 40, [1,111],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 41, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 42, [1,111],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 44, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 51, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 52, [1,111],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 53, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 56, [1,111],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 59, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 64, [1,111],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 67, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 70, [1,111],[]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 74, [1,111],[2,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 84, [1,111],[3,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 87, [1,111],[1,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 97, [1,111],[3,111]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 98, [0,11],[]) ###
# eye_data= visual_inspection(eye_data, '016', 'va', 99, [1,11],[2,111]) ###


####017

# eye_data= visual_inspection(eye_data, '017', 'va', 1, [1,13],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '017', 'va', 14, [2,13],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '017', 'va', 23, [],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '017', 'va', 33, [1,19],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '017', 'va', 36, [1,17],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '017', 'va', 46, [1,19],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '017', 'va', 55, [],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '017', 'va', 73, [1,18],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '017', 'va', 84, [1,16],[1,111])  #DR

####018
# eye_data= visual_inspection(eye_data, '018', 'va', 22, [1,14],[3,111])  #DR
# eye_data= visual_inspection(eye_data, '018', 'va', 24, [1,14],[1,111])  #DR
# eye_data= visual_inspection(eye_data, '018', 'va', 29, [2,16],[2,111])  #DR
# eye_data= visual_inspection(eye_data, '018', 'va', 59, [1,14],[1,111])  #DR *

####020

# eye_data= visual_inspection(eye_data, '020', 'va', 1, [1,111],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 14, [0,10],[])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 16, [1,10],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 21, [1,13],[1,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 22, [1,22],[2,-4])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 23, [1,22],[3,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 24, [1,21],[1,-1])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 26, [1,18],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 27, [1,16],[1,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 30, [0,13],[0,-5])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 31, [0,16],[0,-1])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 34, [1,14],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 36, [2,18],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 38, [1,15],[1,-5])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 39, [2,15],[1,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 40, [0,22],[0,-4])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 48, [1,13],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 53, [1,14],[1,-1])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 57, [1,24],[2,-3])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 65, [1,14],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 66, [1,15],[1,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 83, [1,13],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 86, [0,16],[0,-6])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 87, [1,21],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 88, [1,19],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 89, [0,14],[0,-5])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 93, [0,18],[])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 94, [1,15],[1,-4])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 95, [0,15],[])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 97, [1,16],[2,111])  #
# eye_data= visual_inspection(eye_data, '020', 'va', 99, [1,17],[1,-1])  #


####021

# eye_data= visual_inspection(eye_data, '021', 'va', 6, [1,21],[3,111])
# eye_data= visual_inspection(eye_data, '021', 'va', 8, [0,20],[])
# eye_data= visual_inspection(eye_data, '021', 'va', 10, [1,23],[3,111])
# eye_data= visual_inspection(eye_data, '021', 'va', 11, [1,23],[2,111])
# eye_data= visual_inspection(eye_data, '021', 'va', 14, [1,17],[2,111]) #*
# eye_data= visual_inspection(eye_data, '021', 'va', 16, [1,21],[2,111]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 17, [1,21],[1,111]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 21, [0,21],[0,-1]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 24, [1,21],[2,111]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 26, [0,17],[0,-3]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 27, [0,15],[0,-3]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 32, [0,13],[0,-4]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 35, [0,23],[0,-3]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 36, [0,16],[3,111]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 39, [0,20],[0,-3]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 40, [0,18],[0,-2]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 42, [0,17],[0,-1]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 44, [],[1,111]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 51, [0,17],[0,-2]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 52, [1,17],[1,-3]) #*
# eye_data= visual_inspection(eye_data, '021', 'va', 58, [0,17],[0,-5]) #*
# eye_data= visual_inspection(eye_data, '021', 'va', 60, [1,18],[1,111]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 74, [1,11],[3,111]) #
# eye_data= visual_inspection(eye_data, '021', 'va', 88, [0,20],[0,-3]) #*
# eye_data= visual_inspection(eye_data, '021', 'va', 91, [2,22],[3,-2]) #

###022
# eye_data= visual_inspection(eye_data, '022', 'va', 1, [0,20],[0,-4]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 2, [0,17],[0,-7]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 3, [2,24],[2,-3]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 4, [0,18],[0,-8]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 5, [0,19],[0,-8]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 7, [0,21],[0,-6]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 8, [1,19],[2,-3]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 9, [0,18],[2,-3]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 12, [0,16],[0,-8]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 14, [0,15],[0,-9]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 16, [0,15],[0,-6]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 17, [0,20],[0,-3]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 20, [0,20],[0,-7]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 21, [1,21],[3,-7]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 23, [0,19],[0,-7]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 33, [0,16],[0,-7]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 34, [1,15],[1,-9]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 35, [1,18],[1,-4]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 36, [0,16],[]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 42, [1,18],[2,-1]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 46, [1,16],[1,111]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 52, [1,17],[2,111]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 53, [1,19],[2,-1]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 58, [1,15],[2,-1]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 61, [1,17],[2,-1]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 62, [1,17],[1,-1]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 65, [1,20],[2,-1]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 67, [1,15],[2,-1]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 68, [1,15],[1,-1]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 69, [0,13],[0,-3]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 70, [1,12],[2,-2]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 72, [],[1,111]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 73, [1,13],[4,111]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 79, [2,13],[2,111]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 81, [],[1,111]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 82, [1,15],[3,111]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 83, [1,11],[2,111]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 84, [1,11],[2,-3]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 86, [1,14],[4,-1]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 88, [1,14],[2,-1]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 90, [1,14],[1,111]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 92, [1,15],[2,111]) #
# eye_data= visual_inspection(eye_data, '022', 'va', 99, [],[1,111]) #

####023

# eye_data= visual_inspection(eye_data, '023', 'va', 1, [1,16],[1,111]) #
# eye_data= visual_inspection(eye_data, '023', 'va', 2, [1,24],[1,-3]) #
# eye_data= visual_inspection(eye_data, '023', 'va', 4, [0,21],[0,-5]) #
# eye_data= visual_inspection(eye_data, '023', 'va', 5, [2,21],[2,-5]) #
# eye_data= visual_inspection(eye_data, '023', 'va', 6, [0,21],[0,-3]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 7, [0,16],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 8, [1,20],[2,-4]) #
# eye_data= visual_inspection(eye_data, '023', 'va', 9, [0,20],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 11, [0,21],[0,-5]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 12, [1,20],[2,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 13, [0,21],[0,-5]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 14, [0,20],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 16, [0,22],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 17, [1,22],[2,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 19, [0,23],[0,-8]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 20, [0,20],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 22, [0,26],[0,-3]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 23, [1,23],[2,-3]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 26, [0,22],[0,-5]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 27, [2,24],[2,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 29, [0,20],[0,-3]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 30, [1,19],[2,-8]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 31, [0,20],[0,-5]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 34, [1,20],[2,111]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 38, [1,22],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 40, [0,11],[1,-10]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 41, [2,21],[3,-8]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 42, [1,25],[3,-2]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 43, [0,24],[0,-5]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 45, [0,26],[0,-4]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 47, [0,13],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 48, [0,22],[0,-4]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 49, [0,23],[0,-5]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 51, [0,19],[0,-2]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 52, [3,22],[3,-5]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 53, [0,23],[0,-3]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 54, [0,20],[0,-2]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 55, [0,23],[0,-4]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 56, [0,17],[0,-5]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 58, [0,23],[0,-5]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 59, [1,24],[2,-4]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 60, [2,25],[2,-5]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 61, [1,23],[1,111]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 64, [1,26],[2,-3]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 65, [0,19],[0,-8]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 68, [0,23],[1,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 69, [0,21],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 70, [2,27],[2,111]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 71, [0,22],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 73, [0,23],[0,-4]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 74, [2,23],[0,111]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 79, [0,20],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 80, [0,22],[]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 81, [1,24],[1,-4]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 82, [1,23],[2,-7]) #**
# eye_data= visual_inspection(eye_data, '023', 'va', 83, [3,20],[2,111]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 85, [0,25],[0,-3]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 86, [2,20],[2,111]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 87, [2,26],[4,111]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 90, [0,21],[0,-3]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 92, [0,20],[0,-8]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 95, [2,23],[4,-6]) #*
# eye_data= visual_inspection(eye_data, '023', 'va', 98, [0,18],[0,-6]) #*


####024

# eye_data= visual_inspection(eye_data, '024', 'va', 1, [1,25],[2,-3]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 2, [0,20],[0,-7]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 4, [0,16],[2,-7]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 5, [0,18],[0,-6]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 9, [1,18],[2,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 11, [1,17],[3,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 13, [2,112],[3,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 14, [1,112],[1,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 17, [1,112],[2,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 21, [1,112],[2,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 22, [2,112],[3,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 23, [1,112],[1,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 24, [2,112],[2,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 27, [1,112],[3,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 28, [2,112],[1,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 30, [1,112],[1,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 33, [1,112],[1,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 38, [1,112],[1,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 39, [1,112],[1,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 42, [4,112],[3,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 52, [2,112],[3,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 54, [1,112],[2,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 56, [],[2,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 62, [],[3,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 67, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 68, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 69, [1,111],[1,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 73, [],[2,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 77, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 91, [2,111],[3,111]) #*
# eye_data= visual_inspection(eye_data, '024', 'va', 94, [1,111],[2,111]) #*

####027

# eye_data= visual_inspection(eye_data, '027', 'va', 1, [0,22],[0,-1]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 3, [1,15],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 8, [],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 9, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 11, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 12, [1,111],[3,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 15, [1,111],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 17, [],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 21, [],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 22, [1,111],[3,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 24, [],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 30, [],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 36, [1,111],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 42, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 47, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 48, [3,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 49, [],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 55, [1,111],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 58, [],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 59, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 60, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 62, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 67, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 71, [1,16],[]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 72, [],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 76, [],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 81, [1,111],[3,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 82, [1,111],[2,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 90, [1,111],[3,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 91, [2,111],[3,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 94, [1,111],[1,111]) #*
# eye_data= visual_inspection(eye_data, '027', 'va', 99, [1,111],[3,111]) #*


for i in subjects:
   for j in condition:
        #writing_data(eye_data,i,j,1)
        for k in eye_data[i][j]:
            if type(k) == int:
                #print ([i, " ", j, " ", k])
                visualization_eye(eye_data,i, j, k, 1)
           #visualization_eye(eye_data, i, j, k, 2)

