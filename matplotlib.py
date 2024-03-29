# -*- coding: utf-8 -*-
"""Matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VQZ8XPs6CePse4lloqqevj98xnyLi-ye
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
plt.plot([2,3,4,5])
plt.xlabel('Actual birth weight')
plt.ylabel('Estimated birth weight')
plt.show()

plt.plot([2,3,4,5],[3,8,10,12])
plt.show()

"""### Formatting your pyplot"""

plt.plot([2,3,4,5],[3,8,10,12],'gs')
plt.axis([0,7,0,21])
plt.show()

t=np.arange(0,5,0.2)
plt.plot(t,t,'r--',t,t**3,'b^',t,t**2,'gs')

"""### Matplot Keyword Settings"""

data={'a':np.arange(50),
'c':np.random.randint(0,50,50),
'd':np.random.randn(50)}
data['b']=data['a']+10*np.random.randn(50)
data['d']=np.abs(data['d'])*100
plt.scatter('a','b',c='c',s='d',data=data)

"""### Categorical Variables to Python Plotting"""

names=["Dingos","Wild Cats","Tigers"]
values=[1,11,111]
plt.figure(1,figsize=(9,3))
plt.subplot(131)
plt.bar(names,values)

plt.scatter(names,values)
plt.show()

plt.plot(names,values)
plt.suptitle('Varsity')
plt.show()

"""### Line Properties of Matplotlib"""

plt.plot([1,2,3],[2,4,9],linewidth=4.0)
plt.show()

#alpha channel to create prettier plots by softening colors
plt.plot([1,2,3],[2,4,9],alpha=5.5)
plt.show()

#Antialiased- If you’ll look closely, the lines look quite smooth. 
#But we can turn antialiasing off- this will show us the aliasing in the lines
plt.plot([1,2,3],[2,4,9],antialiased=True)
plt.show()

#Color
plt.plot([1,2,3],[2,4,9],color='Chartreuse')
plt.show()

#Dashes
plt.plot([1,2,3],[2,4,9],dashes=[1,2,4,4])
plt.show()

#Linestyle
plt.plot([1,2,3],[2,4,9],linestyle='steps')
plt.show()

plt.plot([1,2,3],[2,4,9],linestyle=':')
plt.show()

#Marker
plt.plot([1,2,3],[2,4,9],marker='+')
plt.show()

#MarkerEdgeColor
plt.plot([1,2,3],[2,4,9],marker='+',markeredgecolor='brown')
plt.show()

#MarkerEdgeWidth
plt.plot([1,2,3],[2,4,9],marker='+',markeredgewidth=0.4)
plt.show()

#MarkerFaceColor
plt.plot([1,2,3],[2,4,9],marker='.',markerfacecolor='orange',markersize=13.0)
plt.show()

#MarkEvery
plt.plot([1,2,3],[2,4,9],marker='.',markerfacecolor='orange',markersize=13.0,markevery=2)
plt.show()

#Zorder - which in front and which at back
plt.plot([1,2,3],[2,4,9],zorder=1,linewidth=4)
plt.plot([1,2,6,9],[2,4,9,10],zorder=2,linewidth=4)
plt.show()

#Showing a grid in Python Plot
plt.grid(True)
plt.plot([1,2,6,9],[2,4,9,10],zorder=2,linewidth=4)
plt.show()

