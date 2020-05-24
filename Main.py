#Library
import matplotlib.pyplot as plt
import matplotlib as mpl

#TypePlot
mpl.rcParams['font.family'] = 'fantasy'

#ApproximationFunction
def mnkGP(x,y):
    n = len(x)
    s = sum(y)

    #KoefficientsForA&B
    s1 = sum([1/x[i] for i in  range(0,n)])
    s2 = sum([(1/x[i])**2 for i in  range(0,n)])
    s3 = sum([y[i]/x[i]  for i in range(0,n)])

    #MainKoefficients
    a = round((s*s2-s1*s3)/(n*s2-s1**2),3)
    b = round((n*s3-s1*s)/(n*s2-s1**2),3)

    #CheckError
    s4 = [a+b/x[i] for i in range(0,n)]
    so = round(sum([abs(y[i]-s4[i]) for i in range(0,n)])/(n*sum(y))*100,3)

    #CreateGraph
    plt.title('Hiperbola Approximation Y='+str(a)+'+'+str(b)+'/x\n Medial error--'+str(so)+'%',size=14)
    plt.xlabel('Coordinate X', size = 14)
    plt.ylabel('Coordinate Y', size = 14)
    plt.plot(x, y, color='r', linestyle = ' ', marker='o', label='Data(x,y)')
    plt.plot(x, s4, color='g', linewidth = 2, label='Data(x,f(x)=a+b/x')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

#Data
x = [10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86]
y = [0.1, 0.0714, 0.0556, 0.0455, 0.0385, 0.0333, 0.0294, 0.0263, 0.0238, 0.0217,
   0.02, 0.0185, 0.0172, 0.0161, 0.0152, 0.0143, 0.0135, 0.0128, 0.0122, 0.0116]

#DrawGraph
mnkGP(x,y)

