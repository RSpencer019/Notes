#------------------------------------------------------------------------------
# Name:        Network Paths & Edge Weights Generator
# Description: Educational
#
# Author:      Robert S. Spencer
#
# Created:     4/23/2016
# Copyright:   (c) Robert S. Spencer 2016
# Python:      3.5
#------------------------------------------------------------------------------


links = [	[0,1,0,0,1],		### <<<<<<<<------- INPUT ADJACENCY MATRIX ###
			[0,0,1,1,0],
			[0,1,0,1,0],
			[0,1,1,0,1],
			[1,0,0,0,0]
		]

Edges = []
for i in range(len(links)):
	for j in range(len(links)):
		if links[i][j] == 1:
			Edges.append(int(str(i+1)+str(j+1)))

Current_Paths = [1,2,3,4,5]		### <<<<<<<<------- INPUT NETWORK NODES ###
All_Paths = []

print ("Nodes:			",Current_Paths)


for i in range(len(links)-1):
	New_Paths = []
	
	for j in range(len(Current_Paths)):
		n = 0
		
		for k in range(len(links)):
			if links[(Current_Paths[j]%10)-1][k] == 1 and str(k+1) not in str(Current_Paths[j]):
				New_Paths.append(int(str(Current_Paths[j]) + str(k+1)))
				n+=1
		if n == 0:
			New_Paths.append(Current_Paths[j])
	
	Current_Paths = New_Paths
	
	for i in range(len(New_Paths)):
		if New_Paths[i] not in All_Paths:
			All_Paths.append(New_Paths[i])
	
	del New_Paths

print ("Longest Paths:	",Current_Paths)
print ("All Paths:		",All_Paths)
print ("# Paths:		", len(All_Paths),"\n")

Edge_Weights = []
for k in range(len(Edges)):
	t = 0
	for i in range(len(All_Paths)):
		if str(Edges[k]) in str(All_Paths[i]):
			t += 1
	Edge_Weights.append(t)
print ("Edges:			",Edges)
print ("Edge Weights:	",Edge_Weights,"\n")
