



def visual_inspection(eye_data, subject, condition, sent, fix, sacc):

    if len(fix) !=0:
        eye_data[subject][condition][sent]['fixations'] = eye_data[subject][condition][sent]['fixations'][fix[0]:fix[1]]
        eye_data[subject][condition][sent]['dur_fix'] = eye_data[subject][condition][sent]['dur_fix'][fix[0]:fix[1]]

    if len(sacc) !=0:
        eye_data[subject][condition][sent]['saccades'] = eye_data[subject][condition][sent]['saccades'][sacc[0]:sacc[1]]
        eye_data[subject][condition][sent]['dur_sacc'] = eye_data[subject][condition][sent]['dur_sacc'][sacc[0]:sacc[1]]
        eye_data[subject][condition][sent]['amplitude'] = eye_data[subject][condition][sent]['amplitude'][sacc[0]:sacc[1]]

    return eye_data


def data_inspection(eye_data, subjects, condition):

    #004
    if '004' in subjects:
        if 'va' in condition:
            eye_data = visual_inspection(eye_data, '004', 'va', 1, [1, 17], [1, -5])  # DR
            eye_data= visual_inspection(eye_data, '004', 'va', 2, [0,11], [0,-1]) #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 7, [0,6], [0,-4])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 10, [0,12], [0,-4])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 14, [0,13], [0,-4])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 15, [0,13], [0,-4])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 20, [0,15], [0,-6])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 24, [0,14], [0,-1])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 28, [0,15], [0,-4])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 29, [1,15], [2,-1])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 32, [1,14], [0,-3])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 33, [0,14],[])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 35, [1,14],[2,-1])  #FFE
            eye_data= visual_inspection(eye_data, '004', 'va', 37, [0,11],[0,-4])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 38, [0,12],[1,-3])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 39, [],[0,-2])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 42, [1,12],[2,-1])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 44, [0,15],[0,-4])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 45, [0,11],[])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 46, [0,11],[0,-5])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 48, [0,13],[0,-3])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 51, [1,16],[4,1111])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 53, [1,14],[2,-1])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 59, [0,16],[0,-5])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 61, [0,11],[0,-3])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 62, [0,12],[0,-2])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 63, [1,18],[2,1111])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 67, [1,15],[1,1111])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 69, [1,15],[1,-1])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 72, [0,15],[1,1234])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 73, [0,11],[])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 74, [0,12],[0,-1])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 76, [0,11],[0,-2])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 77, [0,17],[])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 78, [0,26],[])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 80, [1,12],[3,-4])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 82, [0,8],[0,-2])  #DR **
            eye_data= visual_inspection(eye_data, '004', 'va', 83, [0,15],[])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 85, [0,11],[0,1111])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 87, [1,14],[1,-1])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 88, [1,11],[1,-1])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 89, [1,14],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 93, [0,10],[])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 95, [1,12],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '004', 'va', 98, [0,19],[])  #DR

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '004', 'vs', 14, [1,24],[3,-2])
            eye_data= visual_inspection(eye_data, '004', 'vs', 17, [1,24],[1,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 20, [1,24],[2,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 23, [0,-1],[])
            eye_data= visual_inspection(eye_data, '004', 'vs', 27, [0,-1],[0,-3])
            eye_data= visual_inspection(eye_data, '004', 'vs', 30, [],[2,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 32, [1,111],[1,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 34, [1,111],[2,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 36, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '004', 'vs', 37, [1,111],[2,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 39, [1,111],[2,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 40, [1,111],[1,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 41, [1,111],[1,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 45, [1,111],[1,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 48, [1,111],[2,-2])
            eye_data= visual_inspection(eye_data, '004', 'vs', 49, [1,111],[1,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 57, [1,111],[3,-2])
            eye_data= visual_inspection(eye_data, '004', 'vs', 59, [1,111],[1,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 62, [1,111],[2,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 63, [1,111],[3,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 68, [1,111],[2,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 72, [],[1,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 74, [1,111],[3,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 76, [1,111],[2,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 77, [1,111],[2,111])
            eye_data= visual_inspection(eye_data, '004', 'vs', 82, [],[1,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 83, [],[3,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 84, [1,111],[1,-1])
            eye_data= visual_inspection(eye_data, '004', 'vs', 88, [1,12],[2,111])

    ###005
    if '005' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '005', 'va', 2, [0,15],[0,-1])  #DR
            eye_data= visual_inspection(eye_data, '005', 'va', 3, [],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'va', 4, [1,15],[1,-1])  #DR
            eye_data= visual_inspection(eye_data, '005', 'va', 15, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'va', 49, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'va', 58, [2,12],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'va', 59, [1,12],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'va', 73, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'va', 87, [],[0,-1])  #DR
            eye_data= visual_inspection(eye_data, '005', 'va', 94, [],[0,-1])  #DR
            eye_data= visual_inspection(eye_data, '005', 'va', 98, [1,111],[2,111])  #DR

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '005', 'vs', 4, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 10, [2,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 16, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 20, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 21, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 24, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 38, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 58, [3,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 64, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 65, [],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 70, [],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 77, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 79, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 80, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 83, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '005', 'vs', 88, [1,111],[1,111])  #DR

    if '007' in subjects:
    ###007 check double reading in vs (up  boundary)
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '007', 'va', 13, [0,12],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 23, [1,13],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 24, [1,8],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 27, [1,13],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 35, [1,17],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 39, [1,17],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 49, [1,17],[])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 64, [1,17],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 70, [1,8],[1,-3])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 81, [1,9],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 94, [1,9],[])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 99, [1,14],[1,111])  #DR

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '007', 'va', 1, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 4, [],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 5, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 12, [3,111],[5,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 13, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 14, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 15, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 18, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 26, [],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 33, [1,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 37, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 38, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 51, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 56, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 58, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 60, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 64, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '007', 'va', 72, [1,111],[3,111])  #DR

    ###009
    if '009' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '009', 'va', 2, [0,17],[])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 6, [1,15],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 9, [2,21],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 18, [1,17],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 19, [2,17],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 24, [1,14],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 26, [1,12],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 27, [2,18],[3,-1])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 48, [1,20],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 57, [1,15],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 58, [1,10],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 83, [1,18],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 88, [1,18],[2,-1])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 95, [3,18],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 96, [1,15],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'va', 99, [1,15],[2,111])  #DR

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '009', 'vs', 5, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'vs', 9, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'vs', 11, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'vs', 12, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '009', 'vs', 18, [1,111],[2,111])  #DR

    ###010

    if '010' in subjects:
        if 'va' in condition:
            eye_data = visual_inspection(eye_data, '010', 'va', 1, [], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 2, [], [0, -2])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 6, [1, 12], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 7, [1, 20], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 8, [1, 21], [1, -2])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 10, [1, 18], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 11, [1, 18], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 12, [3, 18], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 13, [2, 18], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 14, [1, 18], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 15, [4, 18], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 17, [0, -2], [])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 20, [2, -2], [5, -5])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 21, [1, 16], [4, -1])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 24, [1, 16], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 28, [1, 111], [4, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 32, [2, 111], [6, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 33, [2, 111], [5, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 35, [1, 111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 37, [1, -1], [1, -3])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 39, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 43, [], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 44, [1, 15], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 46, [1, 15], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 49, [1, 15], [2, -2])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 52, [1, 16], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 54, [1, 111], [0, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 55, [1, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 56, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 57, [3, 111], [4, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 61, [3, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 62, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 65, [1, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 66, [1, 111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 67, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 68, [3, 111], [4, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 69, [2, 111], [4, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 71, [1, 111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 72, [3, 111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 74, [1, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 76, [1, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 77, [1, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 78, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 80, [2, 111], [5, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 81, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 83, [1, -2], [3, -3])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 84, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 86, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 87, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 88, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 89, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 90, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 93, [2, -7], [4, -8])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 94, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 96, [3, 111], [5, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'va', 99, [2, 111], [3, 111])  # DR


        elif 'vs' in condition:
            eye_data = visual_inspection(eye_data, '010', 'vs', 1, [1,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 2, [2,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 4, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 5, [1,-1], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 6, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 7, [3,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 9, [2,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 11, [2,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 13, [2,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 14, [2,111], [5, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 17, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 26, [0,-6], [0, -7])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 30, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 33, [1,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 34, [], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 59, [1,111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 60, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 62, [0,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 63, [1,111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 65, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 73, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 74, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 76, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 78, [1,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 80, [1,111], [4, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 81, [1,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 85, [2,111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 98, [3,111], [1, 111])  # DR

    ###011

    if '011' in subjects:
        if 'va' in condition:
            eye_data = visual_inspection(eye_data, '011', 'va', 1, [2,-6], [3, -8])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 2, [2,-1], [3, -1])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 6, [1, 111], [])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 7, [1, -3], [0,-3])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 9, [0, -2], [0,-2])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 11, [1, 112], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 14, [2, 112], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 15, [1, 112], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 16, [2, 112], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 21, [2, 112], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 22, [], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 23, [1,111], [3,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 27, [0,-2], [1,-3])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 29, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 32, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 33, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 34, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 35, [1,111], [3,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 36, [1,-1], [3,-2])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 37, [1,111], [1,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 41, [2,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 44, [3,111], [4,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 47, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 48, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 49, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 52, [2,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 53, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 55, [2,111], [3,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 58, [1,111], [1,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 59, [1,111], [3,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 61, [1,111], [4,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 66, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 67, [2,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 68, [1,111], [4,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 69, [2,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 74, [1,111], [1,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 80, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 81, [1,111], [1,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 82, [1,111], [1,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 84, [2,111], [1,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 88, [2,111], [1,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 92, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 93, [1,111], [2,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 94, [3,111], [1,111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'va', 98, [2,111], [1,111])  # DR


        elif 'vs' in condition:
            eye_data = visual_inspection(eye_data, '011', 'vs', 1, [0, -1], [1, -1])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 2, [1, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 4, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 8, [0, -4], [0, -6])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 10, [1,111 ], [1, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 17, [1,111 ], [1, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 18, [1,111 ], [3, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 21, [1,111 ], [2, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 22, [1,111 ], [1, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 23, [3,111 ], [2, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 24, [2,111 ], [2, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 27, [2,111 ], [3, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 28, [2,111 ], [3, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 29, [2,111 ], [2, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 32, [1,111 ], [1, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 33, [1,111 ], [1, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 34, [1,111 ], [2, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 35, [1,111 ], [2, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 40, [1,111 ], [1, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 43, [1,111 ], [1, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 46, [2,111 ], [4, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 47, [], [1, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 48, [1,111], [2, 116])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 51, [1,-1], [0, -1])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 52, [1,111], [2, -1])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 53, [1,111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 54, [1,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 56, [], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 57, [], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 59, [2,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 60, [1,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 62, [1,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 63, [2,111], [5, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 64, [1,111], [4, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 65, [2,111], [4, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 67, [1,111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 70, [3,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 79, [2,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 80, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 82, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 88, [1,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 91, [1,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 92, [2,111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 93, [], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 94, [1,111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 95, [1,111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 98, [1,111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '011', 'vs', 99, [2,111], [3, 111])  # DR

            eye_data = visual_inspection(eye_data, '010', 'vs', 2, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 4, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 5, [1, -1], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 6, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 7, [3, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 9, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 11, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 13, [2, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 14, [2, 111], [5, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 17, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 26, [0, -6], [0, -7])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 30, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 33, [1, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 34, [], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 59, [1, 111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 60, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 62, [0, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 63, [1, 111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 65, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 73, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 74, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 76, [2, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 78, [1, 111], [3, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 80, [1, 111], [4, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 81, [1, 111], [2, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 85, [2, 111], [1, 111])  # DR
            eye_data = visual_inspection(eye_data, '010', 'vs', 98, [3, 111], [1, 111])  # DR

    ### 012
    if '012' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '012', 'va', 3, [1,14],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 12, [1,22],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 13, [1,14],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 17, [1,20],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 22, [0,10],[])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 27, [1,18],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 33, [1,18],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 37, [1,17],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 44, [1,15],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 63, [2,19],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 78, [1,12],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 82, [1,22],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 86, [],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 87, [1,21],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 89, [1,18],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'va', 95, [1,18],[2,111])  #DR

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '012', 'vs', 7, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 8, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 9, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 12, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 13, [2,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 14, [2,111],[5,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 18, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 19, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 22, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 23, [1,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 24, [1,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 27, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 28, [2,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 31, [1,111],[6,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 34, [],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 39, [2,111],[5,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 40, [1,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 41, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 45, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 48, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 53, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 54, [1,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 65, [3,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 68, [1,-2],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 79, [2,112],[6,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 80, [2,112],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 82, [1,112],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 87, [1,112],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 90, [],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 91, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 92, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 94, [2,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 95, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 97, [1,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '012', 'vs', 98, [1,111],[3,111])  #DR

    ###014

    if '014' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '014', 'va', 4, [],[0,-2])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'va', 7, [1,15],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 8, [1,13],[1,-1])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 13, [1,15],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 19, [1,22],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 24, [2,15],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 29, [1,16],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 51, [],[5,111])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 70, [1,14],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 73, [],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 80, [1,15],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 82, [3,20],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '014', 'va', 93, [1,19],[4,111])  #DR

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '014', 'vs', 1, [1,111],[1,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 2, [1,111],[2,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 3, [],[2,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 8, [0,-1],[0,-1])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 9, [1,111],[1,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 13, [1,111],[1,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 16, [1,111],[2,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 20, [1,111],[1,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 21, [1,111],[2,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 22, [2,111],[3,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 28, [1,111],[1,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 29, [1,111],[3,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 30, [1,111],[3,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 31, [2,111],[3,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 34, [1,111],[2,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 35, [],[1,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 43, [],[2,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 46, [1,111],[1,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 51, [1,111],[2,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 53, [2,111],[4,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 54, [1,111],[1,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 61, [1,111],[1,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 66, [2,111],[3,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 70, [1,111],[2,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 71, [1,111],[2,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 84, [1,111],[1,111])  #DR **
            eye_data= visual_inspection(eye_data, '014', 'vs', 89, [1,111],[2,111])  #DR **
    ###015
    if '015' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '015', 'va', 11, [1,18],[2,111])
            eye_data= visual_inspection(eye_data, '015', 'va', 15, [1,15],[2,111])
            eye_data= visual_inspection(eye_data, '015', 'va', 21, [1,17],[2,111])
            eye_data= visual_inspection(eye_data, '015', 'va', 23, [1,14],[2,111])
            eye_data= visual_inspection(eye_data, '015', 'va', 24, [1,15],[1,111])
            eye_data= visual_inspection(eye_data, '015', 'va', 27, [2,20],[2,111])
            eye_data= visual_inspection(eye_data, '015', 'va', 30, [1,20],[1,111])
            eye_data= visual_inspection(eye_data, '015', 'va', 31, [1,15],[1,111])
            eye_data= visual_inspection(eye_data, '015', 'va', 35, [1,18],[1,111])
            eye_data= visual_inspection(eye_data, '015', 'va', 40, [0,12],[1,-6]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 42, [0,17],[]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 54, [1,17],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 63, [1,17],[2,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 67, [1,19],[2,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 70, [1,19],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 71, [1,19],[3,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 72, [1,24],[4,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 73, [1,24],[5,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 74, [],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 78, [1,13],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 84, [1,13],[2,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 91, [2,15],[3,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 95, [2,17],[2,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 98, [2,19],[3,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'va', 99, [2,19],[]) ###

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '015', 'vs', 5, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 6, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 9, [2,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 10, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 24, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 27, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 28, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 31, [],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 32, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 40, [],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 46, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 47, [2,111],[4,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 53, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 56, [2,111],[3,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 60, [2,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 66, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 69, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 73, [1,111],[3,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 79, [1,111],[3,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 80, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 84, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 85, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 89, [2,111],[3,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 90, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '015', 'vs', 96, [1,111],[3,111]) ###

    ###016

    if '016' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '016', 'va', 1, [1,20],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 4, [1,20],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 5, [1,16],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 7, [1,19],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 8, [1,15],[4,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 9, [1,15],[4,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 10, [1,10],[3,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 11, [1,15],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 12, [2,15],[5,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 14, [2,18],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 17, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 20, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 27, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 31, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 32, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 33, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 36, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 37, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 40, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 41, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 42, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 44, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 51, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 52, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 53, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 56, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 59, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 64, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 67, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 70, [1,111],[]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 74, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 84, [1,111],[3,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 87, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 97, [1,111],[3,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 98, [0,11],[]) ###
            eye_data= visual_inspection(eye_data, '016', 'va', 99, [1,11],[2,111]) ###

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '016', 'vs', 17, [1,111],[4,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 18, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 19, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 23, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 27, [1,111],[3,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 28, [1,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 49, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 52, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 55, [2,111],[2,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 64, [1,111],[5,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 73, [1,111],[5,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 89, [1,111],[1,111]) ###
            eye_data= visual_inspection(eye_data, '016', 'vs', 94, [1,111],[4,111]) ##
            eye_data= visual_inspection(eye_data, '016', 'vs', 97, [1,111],[]) ##
            eye_data= visual_inspection(eye_data, '016', 'vs', 99, [2,111],[3,111]) ##

    ###017

    if '017' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '017', 'va', 1, [1,13],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 14, [2,13],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 23, [],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 31, [1,119],[])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 33, [1,19],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 36, [1,17],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 46, [1,19],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 49, [1,191],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 51, [1,191],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 55, [],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 68, [3,18],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 73, [1,18],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 84, [1,16],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 88, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'va', 95, [1,111],[1,111])  #DR

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '017', 'vs', 3, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 9, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 13, [],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 21, [2,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 22, [2,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 24, [1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 29, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 30, [4,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 32, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 35, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 37, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 47, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 51, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 52, [],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 54, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 59, [2,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 63, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 69, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 71, [3,111],[5,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 76, [2,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 87, [3,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 88, [2,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 90, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 91, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 93, [3,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '017', 'vs', 96, [2,111],[3,111])  #DR

    ###018

    if '018' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '018', 'va', 16, [1,14],[2,111])  #DR *
            eye_data= visual_inspection(eye_data, '018', 'va', 18, [2,14],[2,111])  #DR *
            eye_data= visual_inspection(eye_data, '018', 'va', 22, [1,14],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'va', 23, [1,114],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'va', 24, [1,114],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'va', 29, [2,116],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'va', 40, [1,114],[2,111])  #DR *
            eye_data= visual_inspection(eye_data, '018', 'va', 46, [1,114],[2,111])  #DR *
            eye_data= visual_inspection(eye_data, '018', 'va', 49, [2,114],[3,111])  #DR *
            eye_data= visual_inspection(eye_data, '018', 'va', 59, [1,114],[1,111])  #DR *
            eye_data= visual_inspection(eye_data, '018', 'va', 64, [2,114],[1,111])  #DR *
            eye_data= visual_inspection(eye_data, '018', 'va', 66, [2,114],[2,111])  #DR *
            eye_data= visual_inspection(eye_data, '018', 'va', 95, [1,114],[1,111])  #DR *
            eye_data= visual_inspection(eye_data, '018', 'va', 98, [1,114],[1,111])  #DR *

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '018', 'vs', 1, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 2,[2,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 5, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 6, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 19, [],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 30, [1,111],[4,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 43, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 71, [4,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 85,[1,111],[3,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 92,[],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 93, [1,111],[2,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 95, [1,111],[1,111])  #DR
            eye_data= visual_inspection(eye_data, '018', 'vs', 96, [2,111],[2,111])  #DR

    ###020

    if '020' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '020', 'va', 1, [1,111],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 14, [0,10],[])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 16, [1,10],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 21, [1,13],[1,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 22, [1,22],[2,-4])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 23, [1,22],[3,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 24, [1,21],[1,-1])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 26, [1,18],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 27, [1,16],[1,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 30, [0,13],[0,-5])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 31, [0,16],[0,-1])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 34, [1,14],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 36, [2,18],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 38, [1,15],[1,-5])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 39, [2,15],[1,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 40, [0,22],[0,-4])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 48, [1,13],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 53, [1,14],[1,-1])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 57, [1,24],[2,-3])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 65, [1,14],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 66, [1,15],[1,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 83, [1,13],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 86, [0,16],[0,-6])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 87, [1,21],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 88, [1,19],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 89, [0,14],[0,-5])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 93, [0,18],[])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 94, [1,15],[1,-4])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 96, [0,15],[])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 97, [1,16],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'va', 99, [1,17],[1,-1])  #

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '020', 'vs', 1, [1,111],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 5, [1,111],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 10, [1,111],[1,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 14, [2,111],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 15, [1,111],[1,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 17, [2,111],[3,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 19, [1,111],[3,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 27, [2,111],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 33, [2,111],[4,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 34, [1,111],[4,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 38, [1,111],[3,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 41, [2,111],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 42, [3,111],[4,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 48, [3,111],[4,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 51, [2,111],[1,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 62, [3,111],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 74, [2,111],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 77, [2,111],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 83, [1,111],[2,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 84, [2,111],[4,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 96, [2,111],[3,111])  #
            eye_data= visual_inspection(eye_data, '020', 'vs', 99, [1,111],[3,111])  #

    ###021

    if '021' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '021', 'va', 6, [1,21],[3,111])
            eye_data= visual_inspection(eye_data, '021', 'va', 8, [0,20],[])
            eye_data= visual_inspection(eye_data, '021', 'va', 10, [1,23],[3,111])
            eye_data= visual_inspection(eye_data, '021', 'va', 11, [1,23],[2,111])
            eye_data= visual_inspection(eye_data, '021', 'va', 14, [1,17],[2,111]) #*
            eye_data= visual_inspection(eye_data, '021', 'va', 16, [1,21],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 17, [1,21],[1,111]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 21, [0,21],[0,-1]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 24, [1,21],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 26, [0,17],[0,-3]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 27, [0,15],[0,-3]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 32, [0,13],[0,-4]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 35, [0,23],[0,-3]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 36, [0,16],[3,111]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 39, [0,20],[0,-3]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 40, [0,18],[0,-2]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 42, [0,17],[0,-1]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 44, [],[1,111]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 51, [0,17],[0,-2]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 52, [1,17],[1,-3]) #*
            eye_data= visual_inspection(eye_data, '021', 'va', 58, [0,17],[0,-5]) #*
            eye_data= visual_inspection(eye_data, '021', 'va', 60, [1,18],[1,111]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 74, [1,11],[3,111]) #
            eye_data= visual_inspection(eye_data, '021', 'va', 88, [0,20],[0,-3]) #*
            eye_data= visual_inspection(eye_data, '021', 'va', 91, [2,22],[3,-2]) #

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '021', 'vs', 1, [2,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 9, [],[1,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 17, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 59, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 60, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 61, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 62, [3,111],[4,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 66, [2,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 69, [2,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 71, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 72, [3,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 74, [2,111],[4,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 79, [2,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 81, [1,111],[1,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 92, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 94, [1,111],[1,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 95, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 98, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '021', 'vs', 99, [2,111],[2,111]) #

    ##022

    if '022' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '022', 'va', 1, [0,20],[0,-4]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 2, [0,17],[0,-7]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 3, [2,24],[2,-3]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 4, [0,18],[0,-8]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 5, [0,19],[0,-8]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 7, [0,21],[0,-6]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 8, [1,19],[2,-3]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 9, [0,18],[2,-3]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 12, [0,16],[0,-8]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 14, [0,15],[0,-9]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 16, [0,15],[0,-6]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 17, [0,20],[0,-3]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 20, [0,20],[0,-7]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 21, [1,21],[3,-7]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 23, [0,19],[0,-7]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 33, [0,16],[0,-7]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 34, [1,15],[1,-9]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 35, [1,18],[1,-4]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 36, [0,16],[]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 42, [1,18],[2,-1]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 46, [1,16],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 52, [1,17],[2,111]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 53, [1,19],[2,-1]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 58, [1,15],[2,-1]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 61, [1,17],[2,-1]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 62, [1,17],[1,-1]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 65, [1,20],[2,-1]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 67, [1,15],[2,-1]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 68, [1,15],[1,-1]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 69, [0,13],[0,-3]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 70, [1,12],[2,-2]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 72, [],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 73, [1,13],[4,111]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 79, [2,13],[2,111]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 81, [],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 82, [1,15],[3,111]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 83, [1,11],[2,111]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 84, [1,11],[2,-3]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 86, [1,14],[4,-1]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 88, [1,14],[2,-1]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 90, [1,14],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 92, [1,15],[2,111]) #
            eye_data= visual_inspection(eye_data, '022', 'va', 99, [],[1,111]) #

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '022', 'vs', 1, [],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 3, [1,111],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 9, [1,111],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 11, [1,111],[4,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 13, [1,111],[3,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 24, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 30, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 37, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 42, [1,111],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 43, [1,111],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 52, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 55, [1,111],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 57, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 63, [1,111],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 68, [1,111],[1,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 72, [1,111],[4,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 77, [2,111],[3,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 79, [1,111],[2,111]) #
            eye_data= visual_inspection(eye_data, '022', 'vs', 84, [1,111],[1,111]) #

    ###023

    if '023' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '023', 'va', 1, [1,16],[1,111]) #
            eye_data= visual_inspection(eye_data, '023', 'va', 2, [1,24],[1,-3]) #
            eye_data= visual_inspection(eye_data, '023', 'va', 4, [0,21],[0,-5]) #
            eye_data= visual_inspection(eye_data, '023', 'va', 5, [2,21],[2,-5]) #
            eye_data= visual_inspection(eye_data, '023', 'va', 6, [0,21],[0,-3]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 7, [0,16],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 8, [1,20],[2,-4]) #
            eye_data= visual_inspection(eye_data, '023', 'va', 9, [0,20],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 11, [0,21],[0,-5]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 12, [1,20],[2,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 13, [0,21],[0,-5]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 14, [0,20],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 16, [0,22],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 17, [1,22],[2,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 19, [0,23],[0,-8]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 20, [0,20],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 22, [0,26],[0,-3]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 23, [1,23],[2,-3]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 26, [0,22],[0,-5]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 27, [2,24],[2,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 29, [0,20],[0,-3]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 30, [1,19],[2,-8]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 31, [0,20],[0,-5]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 34, [1,20],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 38, [1,22],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 40, [0,11],[1,-10]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 41, [2,21],[3,-8]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 42, [1,25],[3,-2]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 43, [0,24],[0,-5]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 45, [0,26],[0,-4]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 47, [0,13],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 48, [0,22],[0,-4]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 49, [0,23],[0,-5]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 51, [0,19],[0,-2]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 52, [3,22],[3,-5]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 53, [0,23],[0,-3]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 54, [0,20],[0,-2]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 55, [0,23],[0,-4]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 56, [0,17],[0,-5]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 58, [0,23],[0,-5]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 59, [1,24],[2,-4]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 60, [2,25],[2,-5]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 61, [1,23],[1,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 64, [1,26],[2,-3]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 65, [0,19],[0,-8]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 68, [0,23],[1,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 69, [0,21],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 70, [2,27],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 71, [0,22],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 73, [0,23],[0,-4]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 74, [2,23],[0,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 79, [0,20],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 80, [0,22],[]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 81, [1,24],[1,-4]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 82, [1,23],[2,-7]) #**
            eye_data= visual_inspection(eye_data, '023', 'va', 83, [3,20],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 85, [0,25],[0,-3]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 86, [2,20],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 87, [2,26],[4,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 90, [0,21],[0,-3]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 92, [0,20],[0,-8]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 95, [2,23],[4,-6]) #*
            eye_data= visual_inspection(eye_data, '023', 'va', 98, [0,18],[0,-6]) #*

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '023', 'vs', 2, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 3, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 8, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 12, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 14, [2,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 15, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 17, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 20, [],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 29, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 35, [1,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 38, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 41, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 42, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 43, [1,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 44, [0,-1],[1,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 47, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 49, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 51, [2,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 56, [2,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 58, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 69, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 71, [1,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 72, [],[2,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 73, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '023', 'vs', 88, [4,111],[5,111]) #*

    ###024

    if '024' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '024', 'va', 1, [1,25],[2,-3]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 2, [0,20],[0,-7]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 4, [0,16],[2,-7]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 5, [0,18],[0,-6]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 9, [1,18],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 11, [1,17],[3,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 13, [2,112],[3,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 14, [1,112],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 17, [1,112],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 21, [1,112],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 22, [2,112],[3,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 23, [1,112],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 24, [2,112],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 27, [1,112],[3,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 28, [2,112],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 30, [1,112],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 33, [1,112],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 38, [1,112],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 39, [1,112],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 42, [4,112],[3,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 52, [2,112],[3,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 54, [1,112],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 56, [],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 62, [],[3,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 67, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 68, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 69, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 73, [],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 77, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 91, [2,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'va', 94, [1,111],[2,111]) #*

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '024', 'vs', 3, [2,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'vs', 19, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'vs', 24, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'vs', 27, [],[4,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'vs', 30, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'vs', 34, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'vs', 36, [1,111],[4,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'vs', 46, [],[3,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'vs', 47, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'vs', 54, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '024', 'vs', 84, [1,111],[1,111]) #*

    ###027

    if '027' in subjects:
        if 'va' in condition:
            eye_data= visual_inspection(eye_data, '027', 'va', 1, [0,22],[0,-1]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 3, [1,15],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 8, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 9, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 11, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 12, [1,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 15, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 17, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 21, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 22, [1,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 24, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 30, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 36, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 42, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 47, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 48, [3,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 49, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 55, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 58, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 59, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 60, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 62, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 67, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 71, [1,16],[]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 72, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 76, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 81, [1,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 82, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 90, [1,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 91, [2,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 94, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'va', 99, [1,111],[3,111]) #*

        elif 'vs' in condition:
            eye_data= visual_inspection(eye_data, '027', 'vs', 12, [],[3,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 15, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 16, [1,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 24, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 28, [1,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 29, [2,111],[3,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 42, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 47, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 48, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 60, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 61, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 62, [2,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 66, [1,111],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 69, [],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 77, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 81, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 95, [],[1,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 96, [1,111],[2,111]) #*
            eye_data= visual_inspection(eye_data, '027', 'vs', 97, [2,111],[2,111]) #*


    return eye_data