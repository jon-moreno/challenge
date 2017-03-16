'''In this challenge, pick the 11 scholarships that give you the most money! You can only pick sequential scholarships and the product of all scholarships you pick is how much money you'll be awarded! (this school is very cheap, so you only need a few dollars... scholarships are in the range 0-100).

The number of scholarships n is such that n >= 100.

build a small REST API that takes in the nxn matrix of scholarships given and returns your selections

API Specs:
POST /max_scholarship
'Content-Type: application/json'
'''
#Grid size n>=100
	#>=10*10
	#>=100*1
#Numbs in grid 0-100
##Ignore any cases with zero

#Start at 1,1
#Look at all possible combinations
##[{"horizontal": 6, "vertical": 3, "diagonal": 5}]

#Store the largest sum & sequence
#ex store first pair always
##best_product={"sequence": [5,9,25], "total": 1125}
#if total of next calc > best_product: 
	#store the new sequence & total

#~~~~~~~~~~#
#  "main"  #
#~~~~~~~~~~#

#data={"data": [[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]}
grid=[[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]

#Stores the x,y position and corresponding value in a dictionary
position={}
row_num = 0
column_num = 0

for row in grid:
	row_num+=1
	for datum in row:
		if column_num < len(row):
			column_num+=1
		else:
			column_num=1
		position[row_num, column_num]=datum
		print(position)