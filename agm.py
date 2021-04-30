from math import sqrt
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def agm(a0, b0, tolerance=1e-5):
    an, bn = (a0 + b0) / 2.0, sqrt(a0 * b0)         #formula for calculating AGM of two numbers a0,b0
    while abs(an - bn) > tolerance:
        an, bn = (an + bn) / 2.0, sqrt(an * bn)           
    return an

# def bargraph(pair,agm):
#     # creating the bar plot
#     plt.bar(pair,agm,color="r",width = 0.8)
#     plt.xticks(rotation=75)
#     plt.xlabel("Pairs")
#     plt.ylabel("Arithmetic Geometric Mean")
#     plt.title("AGM")
#     plt.grid(color = 'grey',linewidth = 0.5)
#     plt.yticks(np.arange(0, max(agm), 0.5))
#     plt.savefig("AGM.png",bbox_inches="tight",dpi=600)
#     plt.show()

def threedim_plot(x1,x2,agm):
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('AGM')
    plt.title("AGM")
    zdata = agm
    xdata = x1
    ydata = x2
    ax.scatter3D(xdata, ydata, zdata, c=zdata)
    plt.savefig("AGM_3D.png",bbox_inches="tight",dpi=600)
    plt.show()

if __name__=="__main__":
    MAX = 100
    n_list = range(1,MAX+1)     #range for forming pairs
    mean={}             #dictionary for storing each pairs values AGM
    for i in n_list:            #iterating through lists to form pairs and calculate AGM pair-wise
        for j in n_list:
            num=(i,j)
            temp=(j,i)
            if(temp not in mean.keys()):        #Since AGM of x,y=y,x we skip it if it's already calculated
                mean[num]=agm(i,j)
    pair = list(mean.keys())                #x axis
    agm = list(mean.values())               #y axis
    x1=[]
    x2=[]
    for i in range(len(pair)):
        x1.append(pair[i][0])
        x2.append(pair[i][1])

    # bargraph(list(map(str,pair)),agm)                      #to display bargraph
    threedim_plot(x1,x2,agm)                      #to display 3D graph
