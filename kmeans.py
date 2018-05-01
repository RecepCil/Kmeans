#!/usr/bin/python 
from __future__ import division
import numpy as nm
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")  

from Tkinter import *
pencere = Tk()

#################################################################
#######################		GUI		#############################
#################################################################

##Add Nodes##

nodeX = IntVar()
nodeY = IntVar()

lblNodes = Label(pencere,text="Add Nodes").grid(row=0,column=1)
lblNodeX = Label(pencere,text="X").grid(row=1,column=0)
lblNodeY = Label(pencere,text="Y").grid(row=2,column=0)

e1 = Entry(pencere,textvariable=str(nodeX)).grid(row=1,column=1)
e2 = Entry(pencere,textvariable=str(nodeY)).grid(row=2,column=1)

##Add Cluster##

clusterX = IntVar()
clusterY = IntVar()

lblClusters = Label(pencere,text="Add Cluster").grid(row=3,column=1)
lblClusterX = Label(pencere,text="X").grid(row=4,column=0)
lblClusterY = Label(pencere,text="Y").grid(row=5,column=0)

e3 = Entry(pencere,textvariable=clusterX).grid(row=4,column=1)
e4 = Entry(pencere,textvariable=clusterY).grid(row=5,column=1)
#e3.bind("<FocusIn>", lambda args: e3.delete('0', '0'))

##############################################################
#################		K Means Algorithm		##############
##############################################################

def distanceMeasurement(centerOfClusterList,coordinates):
	DistanceList = []
	GroupList = []
	satir = []
	for i in range(len(centerOfClusterList)):	
		x1 = centerOfClusterList[i][0]
		y1 = centerOfClusterList[i][1]
		for c in range(len(coordinates)):
			x2 = coordinates[c][0]
			y2 = coordinates[c][1]
			dist1 = nm.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
			satir.append(round(dist1,2))
		DistanceList.append(satir)
		satir = []
	print "DistanceList:"+str(DistanceList)
	
	liste = []
	for c in range(len(coordinates)):	
		for i in range(len(DistanceList)):		 
			liste.append(DistanceList[i][c])
		index = liste.index(min(liste))
		for x in range(len(liste)):
			if(x == index):
				liste[x] = 1
			else:
				liste[x] = 0
		GroupList.append(liste)
		liste = []
	print "GroupList: "+str(GroupList)
	return GroupList,DistanceList


def calculateNewClusterPoint(GroupList,coordinates):
	n = 0
	total_x = 0
	total_y = 0
	x_list = []
	y_list = []
	centerOfClusterList = []
	
	for i in range(len(GroupList[0])):						
		for j in range(len(GroupList)):				
			if(GroupList[j][i] == 1):
				total_x += coordinates[j][0]
				total_y += coordinates[j][1]
				n += 1
		if n!=0:
			x = round(total_x/n,2)
			y = round(total_y/n,2)
			print "Cluster "+str(i)+": "+str(x)+" "+str(y)
			centerOfClusterList.append([x,y])
			n = 0
			total_x = 0
			total_y = 0
	return centerOfClusterList
	
##############################################################
##############################################################
##############################################################

listNodes=[]
listClusters=[]

#get Node from User Interface
def addNode():
	listNodes.append([nodeX.get(),nodeY.get()])
	lblShowNodes=Label(pencere,text=listNodes).grid(row=1,column=4)
	print listNodes
	
#get Cluster from User Interface
def addCluster():
	listClusters.append([clusterX.get(),clusterY.get()])
	lblShowClusters=Label(pencere,text=listClusters).grid(row=4,column=4)
	print listClusters

#get Nodes and Cluster automatically
def addAuto():
	listNodes.append([[1,1],[2,1],[4,3],[5,4]])
	listClusters.append([[1,1],[2,1]])
	lblShowNodes=Label(pencere,text=listNodes).grid(row=1,column=4)
	lblShowClusters=Label(pencere,text=listClusters).grid(row=4,column=4)
	print listNodes
	print listClusters

def Kmeans():

	centerOfClusterList = []
	coordinates = []

	##############################################
	#######	getting VALUE from User		##########
	##############################################	
	
	for item in listClusters[0]: centerOfClusterList.append(item)
	for item in listNodes[0]: coordinates.append(item)
	
	print "Center of Cluster List: "
	print centerOfClusterList
	print "coordinates: "
	print coordinates

	##############################################
	##############################################
	##############################################	

	oldGroupList=[[0, 0], [0, 0], [0, 0], [0, 0]]

	while 1:
		print "\nIteration"
		
		#distance measurement
		GroupList,DistanceList=distanceMeasurement(centerOfClusterList,coordinates)
	
		#If there is no differences between oldGroupList and GroupList, break the while loop
		#this means that algorithm is finished
		if oldGroupList == GroupList:
			break;
		
		#if it is not find last points, go on and
		#calculating New Points of Clusters
		centerOfClusterList=calculateNewClusterPoint(GroupList,coordinates)
		oldGroupList=GroupList
	
	print "centers of Clusters: "+str(centerOfClusterList)
	print "\n################### it is done #############################"
	
##Show Nodes

lblShowNodes = Label(pencere,text=".").grid(row=1,column=4)
lblShowClusters = Label(pencere).grid(row=4,column=4)

##Add Buttons

btnAddNode = Button(pencere,text="Add", height=1,command = addNode).grid(row=2,column=2)
btnAddCluster = Button(pencere,text="Add", height=1,command = addCluster).grid(row=5,column=2)
btnAddAuto = Button(pencere,text="Add Automatically", width=15, height=2,command = addAuto).grid(row=7,column=1,padx=20, pady=20)
btnKmeans = Button(pencere,text="K-Means!", width=20, height=2,fg="red",command=Kmeans).grid(row=7,column=4,padx=200, pady=2)

pencere.mainloop()