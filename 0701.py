import pandas as pd 
import numpy as np
import os 
path = r"C:\Users\User\Desktop\070" 
files= os.listdir(path) #得到資料夾下的所有檔名稱 
p=[]
for x in files:
    p.append(path+"\\"+str(x))
test=open(p[0])
df= pd.read_csv(test)
test.close()

close=df["收盤價(元)_月"]
vol=df['成交值(百萬元)_月']

returns=df['報酬率％_月']
returns_ln=df['報酬率-Ln_月']
rl=returns[1::].tolist()
volr=vol[1::].tolist()
MILLIQm=[]
for i in range(len(rl)):
    value=abs(float(rl[i]))/float(volr[i])
    MILLIQm.append(value)
MILLIQm
p

