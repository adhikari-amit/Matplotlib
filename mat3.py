from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

# slices=[60,40]
# lables=['Sixty','fourty']
# plt.pie(slices,labels=lables,wedgeprops={'edgecolor':'black'})

data=pd.read_csv('data.csv')
ids=data['Responder_id']
lang_response=data['LanguagesWorkedWith']
language_counter=Counter()
for response in lang_response:
    language_counter.update(response.split(';'))


languages=[]
popularity=[]
for item in language_counter.most_common(5):
    languages.append(item[0])
    popularity.append(item[1])

explode=[0,0,0,0.1,0]
plt.pie(popularity,labels=languages, explode=explode)
plt.title("Pie Chart")
plt.tight_layout()
plt.show()