
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

inflection = 3.5 * 7 * 24
xa = x[:3.5 * 7 * 24]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]

fa = sp.poly1d(sp.polyfit(xa,ya,1))
fb = sp.poly1d(sp.polyfit(xb,yb,1))

fa_error = error(fa,xa,ya)
fb_error = error(fb,xb,yb)
print("Error inflection=%f" %(fa_error+fb_error))

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w * 7 * 24 for w in range(10)],['week %i' % w for w in range(10)])


def error(f,x,y):
    return sp.sum((f(x) - y) ** 2)

fp1,residuals, rank , sv, rcond = sp.polyfit(x,y,1,full = True)

#f(x) = 2.59619213*x + 989.02487106
fx = sp.linspace(0,x[-1],1000) # generate X-values for plotting

#f1
f1 = sp.poly1d(fp1)
print(error(f1,x,y))
plt.plot(fx, f1(fx), 'g-', label = 'd=%i' % f1.order)
#plt.legend(["d=%i" % f1.order], loc = "upper left")
plt.legend(loc = "upper left")
plt.autoscale(tight=True)
plt.grid()
plt.show()