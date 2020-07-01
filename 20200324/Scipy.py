import scipy as sp
data = sp.genfromtxt(r'C:\Users\DK0626\Desktop\web_traffic.tsv', delimiter= "\t")
print(data[:10])
print(data.shape)

x = data[:,0]
y = data[:,1]

#print (x)
#print(y)

print(sp.sum(sp.isnan(y)))

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])


def error(f,x,y):
    return sp.sum((f(x)-y)**2)

fp1,residuals, rank , sv, rcond = sp.polyfit(x,y,1,full = True)

print("Model parameters: %s" % fp1)
print(residuals)
print(rank)
print(sv)
print(rcond)

#f(x) = 2.59619213*x + 989.02487106

fx = sp.linspace(0,x[-1],1000) # generate X-values for plotting

#f0
f0p = sp.polyfit(x,y,0,full = False)
print(f0p)
f0=sp.poly1d(f0p)
print(error(f0,x,y))
plt.plot(fx, f0(fx), 'm-', label = 'd=%i' % f0.order)

#f1
f1 = sp.poly1d(fp1)
print(error(f1,x,y))
plt.plot(fx, f1(fx), 'g-', label = 'd=%i' % f1.order )
#plt.legend(["d=%i" % f1.order], loc = "upper left")

#f2
f2p = sp.polyfit(x,y,2,full = False)
print(f2p)
f2=sp.poly1d(f2p)
print(error(f2,x,y))
plt.plot(fx, f2(fx), 'b--', label = 'd=%i' % f2.order)

#f3
f3p = sp.polyfit(x,y,3,full = False)
print(f3p)
f3=sp.poly1d(f3p)
print(error(f3,x,y))
plt.plot(fx, f3(fx), 'r-', label = 'd=%i' % f3.order)

#f10
f10p = sp.polyfit(x,y,10,full = False)
print(f10p)
f10=sp.poly1d(f10p)
print(error(f10,x,y))
plt.plot(fx, f10(fx), 'y-', label = 'd=%i' % f10.order)

#f100
f100p = sp.polyfit(x,y,100,full = False)
print(f100p)
f100=sp.poly1d(f100p)
print(error(f100,x,y))
plt.plot(fx, f100(fx), 'm-', label = 'd=%i' % f100.order)


plt.legend(loc = "upper left")
plt.autoscale(tight=True)
plt.grid()
plt.show()