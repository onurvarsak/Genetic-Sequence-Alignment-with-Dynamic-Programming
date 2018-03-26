import matplotlib.pyplot as plt
#--------------------------------------------------------------------
time_recur = [[15,16,18,20,22],[0.085000038147,0.257999897003,1.43099999428,9.867000103,47.8740000725,]]
time_diyna = [[15,16,18,20,22],[0.000999927520752,0.00100016593933,0.0019998550415,0.00200009346008,0.00300002098083]]
#--------------------------------------------------------------------
plt.subplot(211)
plt.plot(time_diyna[0], time_diyna[1],"-o",label="Dynamic Method",color="r")
plt.ylabel("Y axis (Time)")
plt.legend(loc=4)
#--------------------------------------------------------------------
plt.subplot(212)
plt.plot(time_recur[0],time_recur[1], "-o", label="Recursive Method", color="r")
plt.legend(loc=2)
plt.xlabel("X axis (M+N)")
plt.ylabel("Y axis (Time)")
#--------------------------------------------------------------------
plt.show()