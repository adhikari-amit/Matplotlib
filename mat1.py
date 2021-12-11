from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use('seaborn-dark')

dev_x=[25,26,27,28,29,30,31,32,34,35]
dev_y=[38496,42000,49320,53200,56000,62316,64928,67317,68748,73752]
py_dev_y=[45372,48876,53850,57287,63016,65998,70009,70000,71496,75370]
js_dev_y=[37852,45000,49520,51245,57123,63485,67145,69785,70145,74156]

plt.xlabel("Age")
plt.ylabel("Salery")
plt.title('Salary(USD) by age')

plt.plot(dev_x,dev_y,'k--',label="all devs")  #k-- is a format string k means coloure is black and -- mean its a dashed line
plt.plot(dev_x,py_dev_y,color='#ad3b3d',linestyle='dashdot' ,marker='o',label="pydev")
plt.plot(dev_x,js_dev_y,'r',label="jsdev")
# plt.legend(['all devs','pydev'])
plt.legend()

plt.grid(True)
# plt.tight_layout()
plt.show()
