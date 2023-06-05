m,n = input().split()
m,n=int(m),int(n)
if n>m:
    print("NO")
elif m==n:
    print("YES")
elif m%2!=0 and n%2==0:
    print("NO")
else:
    print("YES")
