#------------------------------------------------------------------------------
# Name:        Network Paths & Edge Weights
# Description: Educational
#
# Author:      Robert S. Spencer
#
# Created:     4/23/2016
# Python:      3.5
#------------------------------------------------------------------------------

						### INPUT - ADJACENCY MATRIX ###
#------------------------------------------------------------------------------
links = [	
			[0,1,0,0,1],
			[0,0,1,1,0],
			[0,1,0,1,0],
			[0,1,1,0,1],
			[1,0,0,0,0]
		]
#------------------------------------------------------------------------------


# Nodes & Edges
Nodes = []
Edges = []
for i in range(len(links)):
	Nodes.append(i+1)
	for j in range(len(links)):
		if links[i][j] == 1:
			Edges.append(int(str(i+1)+str(j+1)))

# Paths
All_Paths = []
Current_Paths = Nodes
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

# Edge Weights
Edge_Weights = []
for k in range(len(Edges)):
	t = 0
	for i in range(len(All_Paths)):
		if str(Edges[k]) in str(All_Paths[i]):
			t += 1
	Edge_Weights.append(t)

# Output
print ("Nodes:			",str(Nodes).strip('[]'))
print ("Longest Paths:	",str(Current_Paths).strip('[]'))
print ("All Paths:		",str(All_Paths).strip('[]'))
print ("# Paths:		",len(All_Paths))
print ("Edges:			",str(Edges).strip('[]'))
print ("Edge Weights:	",str(Edge_Weights).strip('[]'),"\n")
