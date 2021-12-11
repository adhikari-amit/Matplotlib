from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import pandas as pd
import csv
plt.style.use("seaborn-dark")

# with open('data.csv') as csv_file:
#     csv_reader=csv.DictReader(csv_file)
#     language_counter=Counter()

#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))

data=pd.read_csv('data.csv')
ids=data['Responder_id']
lang_response=data['LanguagesWorkedWith']
language_counter=Counter()
for response in lang_response:
    language_counter.update(response.split(';'))


languages=[]
popularity=[]
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(languages,popularity)  
plt.title("Most Popular language")
plt.xlabel("Popularity")
plt.show()              
# dev_x=[25,26,27,28,29,30,31,32,34,35]
# dev_y=[38496,42000,49320,53200,56000,62316,64928,67317,68748,73752]
# py_dev_y=[45372,48876,53850,57287,63016,65998,70009,70000,71496,75370]
# js_dev_y=[37852,45000,49520,51245,57123,63485,67145,69785,70145,74156]

# plt.xlabel("Age")
# plt.ylabel("Salary")

# x_index=np.arange(len(dev_x))
# width=0.25

# plt.bar(x_index - width,dev_y,width=width,color="#444444",label="all dev")
# plt.bar(x_index,py_dev_y,width=width,color="#008fd5",label="pydev")
# plt.bar(x_index + width,js_dev_y,width=width,color="#e5ae38",label="jsdev")

# plt.xticks(ticks=x_index,labels=dev_x)
# plt.legend()
# plt.show()