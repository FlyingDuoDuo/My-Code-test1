n=int(input('Enter the number of students'))
data={}
subjects=('physics','maths','history')
for i in range(0,n):
	name=input('enter the name of the student {}:'.format(i+1))
	marks = []
	for x in subjects:
		marks.append(int(input('Enter marks of {}'.format(x))))
	data[name]=marks
for x,y in data.items():
	total=sum(y)
	print("{}'s total marks {}".format(x,total))
	if total<120:
		print(x,"failed :(")
	else:
		print(x,"passed :)")
