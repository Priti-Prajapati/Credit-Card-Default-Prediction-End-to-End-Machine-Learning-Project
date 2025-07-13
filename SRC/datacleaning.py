import pandas as pd
df=pd.read_csv(r'C:\Users\PRITI\Desktop\Credit Card\Data\rowdata.csv')
import os
os.makedirs(r'C:\Users\PRITI\Desktop\Credit Card\Data\cleandata',exist_ok=True)
df.to_csv(r'C:\Users\PRITI\Desktop\Credit Card\Data\cleandata\clean.csv',index=False)