import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#  PLOTDATA: plots a line and saves
#  it as a png image ...
#
def plotData(x,y,name):
    plt.clf()
    plt.plot(x,y,'k.')
    plt.title('Raw Data')
    plt.savefig(name)

#  ------------------------------------------------------
#  PLOTFIT: plots line AND data and saves it as a png
#
#
def plotFit(x,y,z,name):
    plt.clf()
    plt.plot(x,y,'k.')
    plt.plot(x,z,'k-')
    plt.title('Fit to Data')
    plt.savefig(name)

#  ------------------------------------------------------
#  GRABDATA
#    Pulls data from file and stores it in x,y
#
def grabData():
    dat=np.genfromtxt('linFit.txt')
    x=dat[:,0]
    y=dat[:,1]

    return (x,y)



#  ------------------------------------------------------
# Step 3: Given list of x return list of h0*x
def hubble(x,h0):
    return [h0*i for i in x]


#     Given data lists x and y, this function
#     finds how well a line, hubble(x) = h0*x fits
#     by calculating the sum of the square of
#     the residuals
#

#Step 5:
def SSR(x,y,h0):
    z=hubble(x,h0)
    SSR=0
    for i in range(len(x)):
        residuals=(z[i]-y[i])**2 
        SSR = SSR + residuals
    return SSR
    


#
#  Step 2: Get data, plot it
#

(x, y)=grabData()
plotData(x,y,'rawData.png')

#   Step 4: Plot example function
#
h0=10
z=hubble(x,h0)
print z
plotFit(x,y,z,"badFit.png")

#
#  Step 6: Find SSR for poor fit from example function
#
h0=10
f=SSR(x,y,h0)
print f

#
#   list for possible slopes. 
#

h0s=np.arange(0.,100.,0.1)

#
#  Step 7: Find slope and intercept that minimize
#              the RSS
#
best_h0 = 0.
min_ssr = np.inf
for h0 in h0s:
    g=SSR(x,y,h0)
    if g < min_ssr:
        min_ssr=g
        best_h0=h0
print best_h0

#
#   Step 8: Plot Result
#
#


#
#   Step 9: Plot Residuals