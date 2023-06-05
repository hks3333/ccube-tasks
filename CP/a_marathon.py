d,a = input().split()
d,a = int(d), int(a)
x=d*a
if a==0:
    x=d
if x>=45:
    print(3)
elif x>=35:
    print(2)
elif x>=15:
    print(1)
else:
    print(-1)
