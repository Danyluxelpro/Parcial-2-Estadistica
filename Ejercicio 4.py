import numpy as np
from numpy import random as rd
import math
from scipy.stats import pareto
from matplotlib import pyplot as plt
mods=["R","P"]
theta=[2.3,8]
tama=[20,50,200,500,1000]

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
#Sesgos:
Sesgos={}
Mse={}
Effis={}
for mo in mods:
    for th in theta:
        Effis[mo+str(th)]={}
        for i in range(5):
            exp1=sum(data[mo+str(th)+" "+str(tama[i])+" Estim_1"])/500
            var1=sum((a-exp1)**2 for a in data[mo+str(th)+" "+str(tama[i])+" Estim_1"])/499
            
            Sesgos[mo+str(th)+" "+str(tama[i])+" Sesgo_E1"]=exp1-th
            Mse[mo+str(th)+" "+str(tama[i])+" Mse_E1"]=var1+(exp1-th)**2

            exp2=sum(data[mo+str(th)+" "+str(tama[i])+" Estim_2"])/500
            var2=sum((a-exp2)**2 for a in data[mo+str(th)+" "+str(tama[i])+" Estim_2"])/499
            
            Sesgos[mo+str(th)+" "+str(tama[i])+" Sesgo_E2"]=exp2-th
            Mse[mo+str(th)+" "+str(tama[i])+" Mse_E2"]=var2+(exp2-th)**2
            eff=(var2+(exp2-th)**2)/(var1+(exp1-th)**2)
            Effis[mo+str(th)][tama[i]]=eff

for mo in mods:
    for th in theta:
        fig,axs=plt.subplots()
        fig.text(0.8,0.015,mo+str(th))
        axs.plot(Effis[mo+str(th)].keys(),Effis[mo+str(th)].values())
        plt.show()


        
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
