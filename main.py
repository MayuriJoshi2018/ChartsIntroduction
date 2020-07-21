import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax= fig.add_axes([0,0,1,1])
Classes=['Little Coders','IntroductionScratch','Intro to Python','Python with pygame']
student=[500,2000,400,500]
ax.bar(Classes,student)
plt.show()