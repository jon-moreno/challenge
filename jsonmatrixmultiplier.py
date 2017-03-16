'''In this challenge, pick the 11 scholarships that give you the most money! You can only pick sequential scholarships and the product of all scholarships you pick is how much money you'll be awarded! (this school is very cheap, so you only need a few dollars... scholarships are in the range 0-100).

The number of scholarships n is such that n >= 100.

build a small REST API that takes in the nxn matrix of scholarships given and returns your selections

API Specs:
POST /max_scholarship
'Content-Type: application/json'
'''
#matrix size n>=100
	#>=10*10
	#>=100*1
#Numbs in matrix 0-100
##Ignore any cases with zero

#Start at 1,1
#Look at all possible combinations
##[{"horizontal": 6, "vertical": 3, "diagonal": 5}]

#Store the largest sum & sequence
#ex store first pair always
##best_product={"sequence": [5,9,25], "total": 1125}
#if total of next calc > best_product: 
	#store the new sequence & total

#~~~~~~~~~~~~~~~~~~~~~~~#
#		definitions		#
#~~~~~~~~~~~~~~~~~~~~~~~#


def find_matrix_size(matrix):
	X_MAX=0
	Y_MAX=0

	for row in matrix:
		Y_MAX+=1
		for datum in row:
			if X_MAX < len(row):
				X_MAX+=1
	return X_MAX, Y_MAX

def store_coordinate_values(matrix):
	y_coordinate = 0
	x_coordinate = 0
	coordinate_values={}

	for row in matrix:
		y_coordinate+=1
		for datum in row:
			if x_coordinate < len(row):
				x_coordinate+=1
			else:
				x_coordinate=1
			coordinate_values[x_coordinate, y_coordinate]=datum
	return coordinate_values	

#~~~~~~~~~~~~~~~~~~~#
#		"main"		#
#~~~~~~~~~~~~~~~~~~~#

#data={"data": [[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]}
#matrix=[[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]
matrix=[

		[1,2,3,4,5],
		[1,1,2,3,5],
		[3,4,5,5,5],
		[3,4,5,9,5]

		]
UPPER_LIMIT=11

X_MAX, Y_MAX = find_matrix_size(matrix)
coordinate_values = store_coordinate_values(matrix)

print(
		X_MAX,
		Y_MAX,
		coordinate_values
	)
#Stores the x,y coordinate & corresponding value in a dictionary


#for 1,1 we want to calculate
#hori= 1,1 * 2,1 * 3,1 *... 11,1
#vert= 1,1 * 1,2 * 1,3 *... 1,11
#diag= 1,1 * 2,2 * 3,3 *... 11,11
#
#Which is to say that we want
#hori= n,n * n+1,n * n+2,n *... n+10,n
#vert= n,n * n,n+1 * n,n+2 *... n,n+10
#diag= n,n * n+1,n+1 * n+2,n+2 *... n+10,n+10 #Thank God it's sequential
#ASSUMING we can go up to 11 (ha ha)

for a in range(1,X_MAX):
	x_coordinate = 1
	y_coordinate = a
	counter = 0
	horizontal = 1

	while(counter < X_MAX):
		#if counter < lim
		horizontal *= coordinate_values[x_coordinate+counter, y_coordinate]
		counter+=1
	print(horizontal)
	a+=1

#So far I have all the horizontal values. I still need...
#Horizontal values to stop grouping at eleven
#Move to the next item and keep grouping in elevens
#all da otha values
#compare them
#Almost done
#JSON parsing
#Actually done