a=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
b=[31, 19, 11, 99, 41, 49, 61, 69, 91, 79]
# n=0
# for i in a :
# 	n=n+i 
# m=0
# for i in b :
# 	m=m+i 
# x = sum(i for i in b[:1])
bs=[0]
for ai in range(len(a)):
    for bi in range(len(b)):
        if abs(a[ai]-sum(i for i in bs) + b[bi]) + \
		    abs(sum(i for i in a[ai+1:])-sum(i for i in b[bi+1:])) < \
		    abs(a[ai]-sum(i for i in bs)) + \
		    abs(sum(i for i in a[ai:])-sum(i for i in b[bi:])):
		    
		    bs.append(b[bi])
        else:
        	bs.append(0)

	print bs	    