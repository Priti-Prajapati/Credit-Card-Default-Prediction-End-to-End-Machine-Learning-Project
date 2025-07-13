
import pandas as pd
df=pd.read_csv(r'C:\Users\PRITI\Desktop\Credit Card\Data\cleandata\clean.csv')
df['default.payment.next.month'].value_counts()
df.head()
df[df.duplicated()]
from imblearn.over_sampling import SMOTE
df.drop('ID',axis=1,inplace=True)
x=df.drop('default.payment.next.month',axis=1)
y=df['default.payment.next.month']
x,y=SMOTE().fit_resample(X=x,y=y)
y.value_counts()
