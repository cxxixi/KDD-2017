# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import re

weather_data = pd.read_csv('YOUR_DIR+weather (table 7)_training.csv',header=0,sep=',')
volume_data = pd.read_csv('YOUR_DIR+volume(table 6)_training.csv',header=0,sep=',')#,usecol=) #volume(table 6)_training.csv')
trajectory_data = pd.read_csv('YOUR_DIR+trajectories(table 5)_training.csv',header=0)
routes = pd.read_csv('YOUR_DIR+routes (table 4).csv',header=0)
links = pd.read_csv('YOUR_DIR+links (table 3).csv',header=0)
output_path = 'YOUR_DIR+data.csv'

data = trajectory_data

#提取date hour
# get date
f1 = lambda x: x.split()[0].strip().replace('/','-')
_date = data['starting_time'].apply(f1)
data['date'] = _date

#get hour
f2 = lambda x: x.split()[1].split(':')[0]
f3 = lambda x: int(x)//3*3
_hour = data['starting_time'].apply(f2)
_hour = _hour.apply(f3)
data['hour'] = _hour

#合并weather data
data = pd.merge(data,weather_data,on=['date','hour'],how='inner')

#合并routes
#给每个route一个标签

routes['route'] = [i for i in xrange(1,7)]
routes['route_length'] = [len(seq.split()) for seq in routes['link_seq']]

for i in xrange(100,124):
    for j in xrange(0,6):
        if str(i) in routes.loc[j,'link_seq']:
            routes.loc[j,str(i)] = 1
        else:
            routes.loc[j,str(i)] = 0

#把routes上哑变量以及路径的编号合并到data
# data = pd.merge(data,routes,on=['intersection_id','tollgate_id'])#,how='inner')

# 把seq里头的时间清洗出来，生成新的列用于存放在某条路上行驶的时间
f4 = lambda x:[seq.split('#')[2] for seq in x.split(';')]
f5 = lambda x:[seq.split('#')[0] for seq in x.split(';')]
data['seq_time'] = data['travel_seq'].apply(f4)
data['seq'] = data['travel_seq'].apply(f5)

for i in xrange(100,124):
    data['T_'+str(i)] = 0

for j in range(len(data['travel_seq'])):
    print len(data.ix[j,'seq']),data.ix[j,'seq']
    for i in range(len(data.ix[j,'seq'])):
        label = data.ix[j,'seq'][i]
        print i,label
        # print label

        value = data.ix[j,'seq_time'][i]
        print 'T'+label,value
        data.ix[j,'T_'+label] = value
        # print data.ix[j,'T'+label]

##计算一些新特征
#一条路径上的直接汇入路有几条
f6 = lambda x: len(str(x))//3
links['flux_in'] = links['in_top'].apply(f6)
links['flux_out'] = links['out_top'].apply(f6)
f7 = lambda seq: [links[links['link_id']==int(x)]['flux_in'] for x in seq.split()]
f8 = lambda list: np.sum([value.values for value in list])
f9 = lambda seq: [links[links['link_id']==int(x)]['flux_out'] for x in seq.split()]
routes['total_in_dir'] = routes['link_seq'].apply(f7)
routes['total_in_dir'] = routes['total_in_dir'].apply(f8)
routes['total_out_dir'] = routes['link_seq'].apply(f9)
routes['total_out_dir'] = routes['total_out_dir'].apply(f8)

routes['total_in_indir'] = [5,7,13,7,13,7]

data = pd.merge(data,routes,on=['intersection_id','tollgate_id'])#,how='inner')

data.to_csv(output_path)
