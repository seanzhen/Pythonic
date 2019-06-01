# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:33:00 2019

@author: Sean Zhen
"""

import pandas as pd
import numpy as np

data = pd.read_csv('./Test_Data.csv')

data_1 = data
res = []
col_name_1 = []
for i in data_1:
    try:
        if data_1[i].value_counts()[1]/len(data) > 0.1:
            col_name_1.append(i)
    except:
        pass

data_1 = data_1[col_name_1]
#A->Label类关联规则
for i in data_1:
    if i != 'Label':
        XY_1 = data_1.loc[(data_1[i]==1)&(data_1['Label']==True)].count()[0]
        X = data_1[i].value_counts()[1]
        XY_2 = data_1.loc[(data_1[i]==1)&(data_1['Label']==False)].count()[0]
        if  XY_1/len(data) > 0.1 and XY_1/X>0.7:
            res.append(i+' --> Label=True')
            print(i+ ' --> Label=True')
        elif XY_2/len(data) > 0.1 and XY_2/X>0.7:
            res.append(i+' --> Label=False')
            print(i + ' --> Label=False')

#BC -> label类关联规则
name_list = [i for i in data_1.drop('Label',axis=1)]
for i in range(len(name_list)):
    for j in range(i+1,len(name_list)):
#         try:
#         print(name_list[i],name_list[j])
        try:
            i_j= data_1.groupby([name_list[i],name_list[j]], as_index=False).count()
            i_j_label = data_1.groupby([name_list[i],name_list[j],'Label'], as_index=False).count()
            X = np.array(i_j.loc[(i_j[name_list[i]]==1) & (i_j[name_list[j]]==1)]).flatten()[2]
            try:
                XY_1 = np.array(i_j_label.loc[(i_j_label[name_list[i]]==1)&(i_j_label[name_list[j]]==1)&(i_j_label['Label']==True)]).flatten()[3]
                # print(XY_1/len(data),XY_1/X)
                if XY_1/len(data)>0.1 and XY_1/X > 0.7 :
                    res.append(str((name_list[i],name_list[j]))+' --> Label=True')
                    print(str((name_list[i],name_list[j]))+' --> Label=True')
            except Exception as e1:
                pass
#                 print(e1)
            try:
                XY_2 = np.array(i_j_label.loc[(i_j_label[name_list[i]]==1)&(i_j_label[name_list[j]]==1)&(i_j_label['Label']==False)]).flatten()[3]
                # print(XY_2/len(data),XY_2/X)
                if XY_2/len(data)>0.1 and XY_2/X >0.7:
                    res.append(str((name_list[i],name_list[j]))+' --> Label=False')
                    print(str((name_list[i],name_list[j]))+' --> Label=False')
            except Exception as e2:
                pass
#                 print(e2)
        except Exception as e:
            pass
print(len(res))
with open('./result.txt','w') as f:
    for line in res:
        f.write(line+'\n')