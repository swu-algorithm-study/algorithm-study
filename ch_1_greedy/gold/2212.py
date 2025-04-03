import sys
input=sys.stdin.readline()

n=int(input)
k=int(input)
m=list(map(int,input.split()))
dist=[]
m.sort()
for i in range(1,n):
    diff=m[i+1]-m[i]
    dist.append(diff)
dist.sort(reverse=True)

print((sum(dist[k-1:])))