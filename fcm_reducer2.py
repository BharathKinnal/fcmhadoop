#!/usr/bin/python
import sys
import os

ownership0=0.0
ownership1=0.0
newc1=[0]*44
newc2=[0]*44
def readData():
	centre=[]
	f = open(os.path.join('/home/training/FCM','SPECTF_New.csv'),'r')
	for line in f:
		line = line.strip().split(",")
		del line[-1]
		centre.append([float(x) for x in line])
	return centre
	
def writeCentres(filename,centre):
	f = open(os.path.join('/home/training/FCM',filename),'w')
	f.writelines(["%s\n" % str(item)  for item in centre])

#points=readData()
denom1=[0]*44
denom2=[0]*44
tp=0
tn=0
fp=0
fn=0
i=0	
for line in sys.stdin:
	#pt=points[i]	
	
	data=line.strip().split("\t")
	#if(len(data)!=2):
	#	continue	
	dat,dat2,ptdat,class_label=data
	ptdat=ptdat.strip().split("|")
	pt=[float(i) for i in ptdat]
	#print data
	# For cluster center 0	
	vals=dat.strip().split("|")
	vals1=[float(i) for i in vals]
	#vals1=vals[0:44]
	#pt=vals[44:]
	for i in range(44):
		newc1[i]+=(vals1[i]**2 * pt[i])
		denom1[i]+=vals1[i]**2
	#ownership0+=float(osums)
	
	# For cluster center 1
	vals2=dat2.strip().split("|")
	vals2=[float(i) for i in vals2]
	
	for i in range(44):
		newc2[i]+=(vals2[i]**2 * pt[i])
		denom2[i]+=vals2[i]**2
	#ownership1+=float(osums2)

	#sum2=sum(vals)
	#osum1=1-osum
	#print vals, "\t", osums
	#print newc1,"\t",Hello
	
	if(vals1[i]>vals2[i]):
		cluster_label=1
	else:
		cluster_label=0
        if cluster_label == 1 and class_label == 'Yes':
            tp = tp + 1
        if cluster_label == 0 and class_label == 'No':
            tn = tn + 1
        if cluster_label == 1 and class_label == 'No':
            fp = fp + 1
        if cluster_label == 0 and class_label == 'Yes':
            fn = fn + 1


newc1=[float(i)/j for i,j in zip(newc1,denom1)]	
newc2=[float(i)/j for i,j in zip(newc2,denom2)]
accuracy = float(tp+tn)/(tp+tn+fp+fn)
ac1=float(fp+fn)/(tp+tn+fp+fn) 
accuracy=max(accuracy,ac1)

writeCentres('centre1.txt',newc1)
writeCentres('centre2.txt',newc2)
print newc1, "\t", "Cluster0"
print newc2, "\t", "Cluster1"
print '\n','Accuracy = ',accuracy,'\n'
