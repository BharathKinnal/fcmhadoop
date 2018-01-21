#!/usr/bin/python

import sys
import os

def readCentres(filename):
	'''with open(filename,'r') as f:
		content=f.readlines()
	centre=[int(x.strip()) for x in content]'''
	centre=[]
	f = open(os.path.join('/home/training/FCM',filename),'r')
	for line in f:
		line = line.strip()
		centre.append(float(line))
	return centre

def check(tup1,tup2):
	if(len(tup1)!=len(tup2)):
		return 0
	else:
		for i in range(len(tup1)):
			if(tup1[i]!=tup2[i]):
				return 0;
	return 1;

centre1=readCentres("centre1.txt")
centre2=readCentres("centre2.txt")
#centre1 = [68.0 for i in range(44)]
#centre2 = [80.0 for i in range(44)]
for line in sys.stdin:
	data=line.strip().split(",")
	lab=data[-1]
	del data[-1]
	dat=[float(i) for i in data]
	
	oxtup0=[]
	oxtup1=[]
	for j in range(44):
		if(dat[j] - centre2[j] == 0) :
			osum0=0
		else :
			osum0 = 1 / (1 + (((dat[j]-centre1[j])/float(dat[j] - centre2[j]))**2))
		if(dat[j]-centre1[j]==0) :
			osum1=0
		else :	
			osum1 = 1 / (1 + (((dat[j]-centre2[j])/float(dat[j] - centre1[j]))**2))
		oxtup0.append(osum0)
		oxtup1.append(osum1)
			
		
	strg=str(oxtup0[0])
	for d in range(44):
		if(d == 0):
			continue
		else:
			strg+=("|"+str(oxtup0[d]))
	stre=str(dat[0]) 
	for da in range(44):
	#strg+=("|"+str(osum0))
		if(da == 0):
			continue
		else:
			stre+=("|"+str(dat[da]))
	strd=str(oxtup1[0])
	for d in range(44):
		if(d == 0):
			continue
		else:
			strd+=("|"+str(oxtup1[d])) 
	#strd+=("|"+str(osum1))
	
	
	print "{0}\t{1}\t{2}\t{3}".format(strg,strd,stre,lab)
	
	
		



