n=int(input())
l=[]
for i in range(n):
    no=int(input())
    if no in l:
        l.remove(no)
    else:
        l.append(no)
print(l[0])
