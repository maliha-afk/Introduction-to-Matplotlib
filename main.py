import matplotlib 
import matplotlib.pyplot as plt
import numpy as np



name=np.array(["atiya","ryan","zaheen","tahmid"])
marks=np.array([70,80,65,90])

plt.plot(name,marks)
plt.title("name & marks")
plt.xlabel("name")
plt.ylabel("marks")
plt.show()
