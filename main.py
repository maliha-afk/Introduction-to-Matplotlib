import matplotlib 
import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,10])
ypoints=np.array([5,8])

#plt.plot(xpoints,ypoints)

#plt.show()

xpoints2=np.array([1,5,6,10])
ypoints2=np.array([2,4,6,8])

#plt.plot(xpoints2,ypoints2,"o",mec="r",ms=10)
#plt.show()

name=np.array(["atiya","ryan","zaheen","tahmid"])
marks=np.array([70,80,65,90])

plt.plot(name,marks)
plt.title("name & marks")
plt.xlabel("name")
plt.ylabel("marks")
plt.show()