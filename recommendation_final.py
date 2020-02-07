# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:17:40 2020

@author: 91603
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:08:58 2020

@author: 91603
"""

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
plt.style.use(style ="ggplot")
import missingno as msno
import seaborn as sns
sns.set()

df_names=["name",
    	  "taste",
    	  "surroundings",
    	  "price",
    	  "attitude"]

df_star = pd.read_csv("star.csv",names = df_names)
df_mean = df_star.groupby('name').mean()
df_mean.to_csv('mean.csv', encoding='utf_8_sig')


#df = pd.read_csv("mean.csv", names = df_names)
#df_sample = df.sample(n = 50)
#df_sample.to_csv('star_sample.csv')
#f = open('star_sample.csv')
#f.close()
##file_name = 'star_sample.csv'
##f = open(file_name,'w')
##f.writelines(df_sample)
##f.close()
##taste_sample = pd.read_csv('star_sample.csv', usecols[2])
choice = int(input('\n 请输入排序方式 \n 1.口感 \n 2.环境 \n 3.价格 \n 4.服务态度 \n 5.自定义权重 \n 6.默认 \n ==>'))
#df_csv_sample = pd.read_csv("star_sample.csv")
score = []
num = df_mean.shape[0]
taste = df_mean.iloc[:num,0]
surroundings = df_mean.iloc[:num,1]
price = df_mean.iloc[:num,2]
attitude = df_mean.iloc[:num,3]

if choice == 5:
##    taste_sample = df_sample.iloc[:50,1]
##    surroundings_sample = df_sample.iloc[:50,2]
##    price_sample = df_sample.iloc[:50,3]
##    attitude_sample = df_sample.iloc[:50,4]


    taste_weigh = float(input('\n 输入口感所占权重并回车 \n 0.1 or 0.2 or 0.3 or 0.4 \n ==>'))
    surroundings_weigh = float(input('\n 输入环境所占权重并回车 \n 0.1 or 0.2 or 0.3 or 0.4 \n ==>'))
    price_weigh = float(input('\n 输入价格所占权重并回车 \n 0.1 or 0.2 or 0.3 or 0.4 \n ==>'))
    attitude_weigh = float(input('\n 输入服务态度所占权重并回车 \n 0.1 or 0.2 or 0.3 or 0.4 \n ==>'))
    for i in range(0,num):
        star = taste.iloc[i]*taste_weigh+surroundings.iloc[i]*surroundings_weigh+price.iloc[i]*price_weigh+attitude.iloc[i]*attitude_weigh
        score.append(star)

##    df_csv_sample['star1'] = star1
##    df_csv_sample.to_csv('star_sample.csv')
##    df_csv_sample.sort_values(by='star1',ascending= False,inplace=True)
##    df_csv_sample.to_csv('star_sample.csv')
elif choice == 1:
    for i in range(0,num):
        star = taste.iloc[i]
        score.append(star)
        
elif choice == 2:
    for i in range(0,num):
        star = surroundings.iloc[i]
        score.append(star)
        
elif choice == 3:
    for i in range(0,num):
        star = price.iloc[i]
        score.append(star)
        
elif choice == 4:
    for i in range(0,num):
        star = attitude.iloc[i]
        score.append(star)

elif choice == 6:
    for i in range(0,num):
        star = pow(taste.iloc[i]*surroundings.iloc[i]*price.iloc[i]*attitude.iloc[i] , 1/4)
        score.append(star)

df_mean['score'] = score
#df_mean.to_csv('mean.csv', encoding='utf_8_sig')
df_mean.sort_values(by='score',ascending= False,inplace=True)
df_mean.to_csv('mean.csv', encoding='utf_8_sig')
df = pd.read_csv('mean.csv')
print(df.iloc[:5,0])