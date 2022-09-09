def monotinic(A):
    return(all(A[i]<=A[i+1] for i in range(len(A)-1))or all(A[i]>=A[i-+1] for i in range(len(A)-1)))
a=[22,3,32,1]
print(monotinic(a))