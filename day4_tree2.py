def tree_2(file, right,down):
	line=[]
	tree =0
	i=0
	line_number =0
	f = open(file, "r")	
	line.append(f.read())
	values=line[0].split("\n")
	for value in values[::down]:
		if value != values[-1]:
			print("i",i)
			line_number +=1
			if value[i] == "#":
				tree +=1
				print("tree=",tree)
			if  i+right >len(value)-1:
				print("starting a new pattern from i =",i,line_number)
				i-=len(value)
				i+=right
			else:
				i+=right	
		else:
		 	break

	return (tree)
		
print(tree_2("tree.txt", 1,1))
print(tree_2("tree.txt", 3,1))
print(tree_2("tree.txt", 5,1))
print(tree_2("tree.txt", 7,1))
print(tree_2("tree.txt", 1,2))
result  = tree_2("tree.txt", 1,1)*tree_2("tree.txt", 3,1)*tree_2("tree.txt", 5,1) *tree_2("tree.txt", 7,1) *tree_2("tree.txt", 1,2)
print(result)
#Right 1, down 1.
#Right 3, down 1. (This is the slope you already checked.)
#Right 5, down 1.
#Right 7, down 1.
#Right 1, down 2.
