import pandas as pd
data=pd.read_csv(r"C:\Users\User\Desktop\52&max_data.csv",encoding="ANSI")
name=data["簡稱"]
data.iloc[0]
x=[]
space=pd.DataFrame(x)
for i in range(len(name)):
    if name[i]=="塑膠工業類指數":
        x.append(data.iloc[i])
space=space.sort_values('年月日',ascending=True)
space.to_csv(r"C:\Users\User\Desktop\plastic_test.csv",encoding="ANSI")