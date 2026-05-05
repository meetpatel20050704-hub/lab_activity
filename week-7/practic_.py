i=[]
while True:
    x=input("Price or done: ")
    if x=="done": break
    i.append(x)

t=0
for n in i: t+=n

while True:
    print("Total:",t)
    print("Approved" if 500>t else "Not Approved")
    break