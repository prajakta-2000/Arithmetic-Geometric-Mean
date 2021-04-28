from math import sqrt
import matplotlib.pyplot as plt
 
def agm(a0, b0, tolerance=1e-5):
    an, bn = (a0 + b0) / 2.0, sqrt(a0 * b0)         #formula for calculating AGM of two numbers a0,b0
    while abs(an - bn) > tolerance:
        an, bn = (an + bn) / 2.0, sqrt(an * bn)           
    return an

def bargraph(pair,agm):
    # creating the bar plot
    plt.bar(pair,agm,color="r",width = 0.8)
    plt.xticks(rotation=75)
    plt.xlabel("Pairs")
    plt.ylabel("Arithmetic Geometric Mean")
    plt.title("AGM")
    plt.savefig("collatz_AGM.png",bbox_inches="tight",dpi=600)
    plt.show()

if __name__=="__main__":
    MAX = 8
    n_list = range(1,MAX+1)     #range for forming pairs
    mean={}             #dictionary for storing each pairs values AGM
    for i in n_list:            #iterating through lists to form pairs and calculate AGM pair-wise
        for j in n_list:
            num=str(i)+","+str(j)
            temp=num[2]+","+num[0]
            if(temp not in mean.keys()):        #Since AGM of x,y=y,x we skip it if it's already calculated
                mean[num]=agm(i,j)
    pair = list(mean.keys())                #x axis
    agm = list(mean.values())               #y axis
    bargraph(pair,agm)                      #to display bargraph