import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv('data1.csv')
ids=data['Responder_id']
age=data['Age']

bins=[10,20,30,40,50,60,70,80,90]
plt.hist(age,bins=bins,edgecolor='black',log=True)
plt.title("Histogram")
plt.xlabel('age')
plt.ylabel("Total response")
plt.tight_layout()
plt.show()
