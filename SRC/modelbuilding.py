df=pd.read_csv(r'C:\Users\PRITI\.cache\kagglehub\datasets\uciml\default-of-credit-card-clients-dataset\versions\1\UCI_Credit_Card.csv')

import pandas as pd
from imblearn.over_sampling import SMOTE

x=df.drop('default.payment.next.month',axis=1)
y=df['default.payment.next.month']

x,y=SMOTE().fit_resample(X=x,y=y)

y.value_counts()


import os
os.makedirs(r'C:\Users\PRITI\Desktop\Credit Card\Data\preprocessdata',exist_ok=True)
x.to_csv(r'C:\Users\PRITI\Desktop\Credit Card\Data\preprocessdata\x.csv',index=False)
y.to_csv(r'C:\Users\PRITI\Desktop\Credit Card\Data\preprocessdata\y.csv',index=False)
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=.3,stratify=y)
x_train.shape,y_train.shape
scaled=StandardScaler()
x_train_scaled=scaled.fit_transform(x_train)
x_test_scaled=scaled.transform(x_test)
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train_scaled,y_train)
predict=lr.predict(x_test_scaled)
from sklearn.metrics import classification_report
print(classification_report(y_test,predict))
from sklearn.tree import DecisionTreeClassifier
ds=LogisticRegression()
ds.fit(x_train_scaled,y_train)
predict=ds.predict(x_test_scaled)
from sklearn.metrics import classification_report
print(classification_report(y_test,predict))

import pickle

with open(r'C:\Users\PRITI\Desktop\Credit Card\Models\model_pkl','wb') as file:
        pickle.dump(lr,file)

with open(r'C:\Users\PRITI\Desktop\Credit Card\Models\model_pkl','rb') as file:
        loaded_model=pickle.load(file)

loaded_model.predict(x_test_scaled)