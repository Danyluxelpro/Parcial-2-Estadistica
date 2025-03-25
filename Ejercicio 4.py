import numpy as np
from numpy import random as rd
import math
from scipy.stats import pareto
from matplotlib import pyplot as plt
mods=["R","P"]
theta=[2.3,8]
tama=[20,50,200,500,1000]
#tama=[5]
data={}
for th in theta:
    for i in tama:
        data["P"+str(th)+ " "+ str(i)+" Estim_1"]=[]
        data["P"+str(th)+ " "+ str(i)+" Estim_2"]=[]
        data["R"+str(th)+ " "+ str(i)+" Estim_1"]=[]
        data["R"+str(th)+ " "+ str(i)+" Estim_2"]=[]
        j=0
        while j<500:
            x=pareto.rvs(th,size=i)
            ave=sum(x)/i
            estim_1=float(round(ave/(ave-1),6))
            estim_2=float(round(i/(math.log(math.prod(x))),6))
            data["P"+str(th)+ " "+ str(i)+" Estim_1"].append(estim_1)
            data["P"+str(th)+ " "+ str(i)+" Estim_2"].append(estim_2)
            j+=1
        l=0
        while l<500:
            x=rd.rayleigh(th, size=i)
            ave=sum(x)/i
            estim_1=float(round(ave*math.sqrt(2/np.pi),6))
            estim_2=float(round(math.sqrt((sum(o*o for o in x))/(2*i)),6))
            data["R"+str(th)+ " "+ str(i)+" Estim_1"].append(estim_1)
            data["R"+str(th)+ " "+ str(i)+" Estim_2"].append(estim_2)
            l+=1

for mo in mods:
    for th in theta:
        fig, axs= plt.subplots(2,5)
        fig.text(0.8,0.015,mo+" "+str(th))
        for i in range(5):
            axs[0,i].boxplot(data[mo+str(th)+" "+str(tama[i])+" Estim_1"])
            axs[0,i].set_title(str(tama[i])+ " Estim_1")
            axs[1,i].boxplot(data[mo+str(th)+" "+str(tama[i])+" Estim_2"])
            axs[1,i].set_title(str(tama[i])+" Estim_2")
        plt.show()

#Sesgos:
Sesgos={}
Mse={}
            
        
        
