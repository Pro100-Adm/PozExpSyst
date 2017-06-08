def calc(x):
    ver_var_Sams_A3 = {0:0.1, 1:1, 2:0, 3:0, 6:0, 7:1}
    ver_var_Sams_A5 = {0:0.1, 1:1, 2:0, 3:0, 6:1, 7:1}
    ver_var_Sams_S7 = {0:0.5, 1:1, 2:0, 3:0, 6:0, 7:1}
    ver_var_Sams_S8 = {0:0.3, 1:1, 2:0, 3:0, 6:1, 7:1}
    ver_var_Iphone_6S = {0:0.1, 1:0, 2:1, 3:0, 6:0, 8:1}
    ver_var_Iphone_7 = {0:0.1, 1:0, 2:1, 3:0, 6:1, 8:1}
    ver_var_Len_K5 = {0:0.1, 1:0, 2:0, 3:1, 6:0, 7:1}
    ver_var_Len_K6 = {0:0.1, 1:0, 2:0, 3:1, 6:1, 7:1}
    ver_var_Len_X = {0:0.1, 1:0, 2:0, 3:1, 6:0, 7:1}
    ver_var_Len_Z = {0:0.1, 1:0, 2:0, 3:1, 6:1, 7:1}
    for i in range(0,len(x)-1):
        for j in range(0,len(ver_var_Sams_A3)-1):
            if i==list(ver_var_Sams_A3.keys())[j]:
                Sams_A3 = x[i]*list(ver_var_Sams_A3.values())[j]
        for k in range(0,len(ver_var_Sams_A5)-1):
            if i==list(ver_var_Sams_A5.keys())[k]:
                Sams_A5 = x[i]*list(ver_var_Sams_A5.values())[k]
        for l in range(0,len(ver_var_Sams_S7)-1):
            if i==list(ver_var_Sams_S7.keys())[l]:
                Sams_S7 = x[i]*list(ver_var_Sams_S7.values())[l]
        for m in range(0,len(ver_var_Sams_S8)-1):
            if i==list(ver_var_Sams_S8.keys())[m]:
                Sams_S8 = x[i]*list(ver_var_Sams_S8.values())[m]
        for n in range(0,len(ver_var_Iphone_6S)-1):
            if i==list(ver_var_Iphone_6S.keys())[n]:
                Iphone_6S = x[i]*list(ver_var_Iphone_6S.values())[n]
        for o in range(0,len(ver_var_Iphone_7)-1):
            if i==list(ver_var_Iphone_7.keys())[o]:
                Iphone_7 = x[i]*list(ver_var_Iphone_7.values())[o]
        for p in range(0,len(ver_var_Len_K5)-1):
            if i==list(ver_var_Len_K5.keys())[p]:
                Len_K5 = x[i]*list(ver_var_Len_K5.values())[p]
        for q in range(0,len(ver_var_Len_K6)-1):
            if i==list(ver_var_Len_K6.keys())[q]:
                Len_K6 = x[i]*list(ver_var_Len_K6.values())[q]
        for r in range(0,len(ver_var_Len_X)-1):
            if i==list(ver_var_Len_X.keys())[r]:
                Len_X = x[i]*list(ver_var_Len_X.values())[r]
        for s in range(0,len(ver_var_Len_Z)-1):
            if i==list(ver_var__Len_Z.keys())[s]:
                Len_Z = x[i]*list(ver_var_Len_Z.values())[s]
    y=[str(Sams_A3),str(Sams_A5),str(Sams_S7),str(Sams_S8),str(Iphone_6S),str(Iphone_7),str(Len_K5),str(Len_K6),str(Len_X),str(Len_Z)]
    return y
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
