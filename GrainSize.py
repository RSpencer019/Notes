#------------------------------------------------------------------------------
# Name:        Sampling Size
# Description: Educational
#
# Author:      Robert S. Spencer
#
# Created:     4/17/2016
# Copyright:   (c) Robert S. Spencer 2016
# Python:      3.5
#------------------------------------------------------------------------------

grainsize = [
3,
3,
3,
3,
3,
3,
3,
3,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4,
4.5,
5,
5,
5,
5,
5,
5,
5,
5,
5,
5,
5,
5,
5,
5,
5,
5,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
6,
7,
7,
7,
7,
7,
7,
7,
7,
7,
7,
8,
8,
8,
8,
8,
8,
8,
8,
8,
8,
8,
9,
9,
9,
9,
9,
9,
9,
9,
9,
9,
9,
9,
9,
9,
10,
10,
10,
10,
10,
10,
10,
10,
10,
11,
11,
11,
11,
11,
11,
11,
11,
12,
12,
12,
12,
12,
12,
13,
13,
13,
13,
13,
13,
13,
13,
13,
13,
14,
14,
14,
14,
15,
15,
15,
16,
16,
16,
17,
18,
18,
19,
19,
19,
19,
19,
20,
20,
20,
20,
21,
21,
22,
22,
22,
22,
24,
24,
25,
30,
30,
31,
34,
36,
38,
45,
45,
47,
47,
52,
102]


from statistics import median, mean
from random import randint

true_median = median(grainsize)
Sample_Size = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 20, 30, 40, 50, 60]
Error = []

print ("Population Median: ", true_median, "\n")
print ("# of Iterations: 10000")

for k in range(len(Sample_Size)):
	
	Sample_Medians = []

	for j in range(10000):
		Sample = []
		
		for i in range(Sample_Size[k]):
			Sample.append(grainsize[randint(0,len(grainsize)-1)])

		Sample_Medians.append(median(Sample))
		del Sample
	
	print ("Sample Size: ", Sample_Size[k])
	print ("Average Sample Median: ", mean(Sample_Medians))
	Error.append(100*(true_median-mean(Sample_Medians))/true_median)
	del Sample_Medians

print ("Error (%): ", Error)

print ("\nSample Size 				Error")
for i in range(0, len(Sample_Size)):
	print (Sample_Size[i], ", ", Error[i])
print ("\n")
