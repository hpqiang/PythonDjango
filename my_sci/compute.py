# refer to http://hplgit.github.io/web4sciapps/doc/pub/._web4sa_django006.html

#Question: Why pyplot would fail if plotting the 'compute' button is clicked again???
#Answer: Because don't include 'if __name__=='__main__' stuff?

from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob
#import gc

#first = True
#plotfile = None

def dampled_vibrations(t,A,b,w):
	return A*exp(-b*t)*cos(w*t)

def compute(A,b,w,T,resolution=500):
	""" Return filename of plot of dampled_vibrations function """
	print os.getcwd()

	if not os.path.isdir('static'):
		print("removing static???")
		os.mkdir('static')
	else:
		for filename in glob.glob(os.path.join('static','*.png')):
			print("removing file: {}".format(filename))
			os.remove(filename)

	#plt.ion()
	#global first
	#global plotfile
	#if first is True:
	t = linspace(0,T,resolution)
	y = dampled_vibrations(t,A,b,w)
	#print("in compute: y={}".format(y))
	# f = plt.figure()
	# print("f={}".format(f))
	# print("in compute: figure")
	
	plt.plot(t,y)
	print("in compute: plot")
	plt.title('A=%g,b=%g,w=%g' % (A,b,w))
	print("in compute: title")

	plotfile = os.path.join('static',str(time.time())+'.png')
	print("savming file: {}".format(plotfile))
	plt.savefig(plotfile)
	#plt.show()

	#f.clf()
	#if(f): del f
	#del y
	#plt.close() # Need to close it before return
	# gc.c

	#	first = False

	return plotfile

# if __name__ == '__main__':
# 	for x in range(2):
# 		print("x={}".format(x))
# 		print compute(1,0+x,1,20)