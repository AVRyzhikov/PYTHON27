a=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
b=[31, 19, 11, 99, 41, 49, 61, 69, 91, 79]
# n=0
# for i in a :
# 	n=n+i 
# m=0
# for i in b :
# 	m=m+i 
# x = sum(i for i in b[:1])

for bi in range(len(b)):
	b[bi]=[b[bi]]
	b[bi]=[b[bi]]
	b[bi]=[b[bi]]


for ai in range(len(a)-1):
	# right moving
	xb=b[ai+1]
	b[ai+1]=b[ai]+b[ai+1]
	b[ai]=[] 
	r1=a[ai]

	r2=a[ai+1]
	for i in range(ai+2,len(a)):
		r2=abs(suma[i]-sum(j for j in b[i]))

    # return value
    b[ai]=b[ai+1][0]
    b[ai+1]=b[ai+1][1:]


    # current
	c1=abs(a[ai]-sum(j for j in b[ai]))
	c2=abs(sum(a[i]-sum(j for j in b[i])) for i in range(ai+1,len(a)))
	

	# testing of left moving steps 
	for bi in range(ai+1:len(b)):
	
		l1=abs(a[a1]-sum(sum(j for j in b[i]) for i in range(ai,bi)))
		l2=abs(sum(a[i]-sum(j for j in b[i])) for i in range(bi+1,len(a)))

		# compare
		if l1+l2>=r1+r2 and l1+l2>=c1+c2:
			break
	if bi < len(b):
		# move left 
		for bb in range(ai,bj):	
			bj[i]=b[i]+b[bb]
			b[bb]=[]
	elif r1+r2<c1+c2:
		#  move right
		b[ai+1]=b[ai]+b[ai+1]
		b[ai]=[]
	
	print b 




# 		    abs(sum(i for i in a[ai+1:])-sum(i for i in b[bi+1:])) < \
# 		    abs(a[ai]-sum(i for i in bs)) + \
# 		    abs(sum(i for i in a[ai:])-sum(i for i in b[bi:])):
		    
# 		    bs.append(b[bi])
#         else:
#         	bs.append(0)

# 	print bs	    