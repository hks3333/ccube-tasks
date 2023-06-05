x,y,k= input().split()
x,y,k= int(x),int(y),int(k)
if x%k!=0 or y%k!=0:
    print("NO")
else:
    print("YES")
