N=10
count=0
sum=0
print('enter 10 numbers:')
while count<10:
	number=float(input())
	sum=sum+number
	count+=1
print('amount:{} sum:{}'.format(count,sum))
print('average:{:.2f}'.format(sum/count))
