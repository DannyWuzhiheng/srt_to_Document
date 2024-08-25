p1=r"E:\影像库\man.txt"
p2=r"E:\吴执恒\观鸟课\yjg.docx"
c=[]
with open(p1,"r",encoding='utf-8') as f:
    b = []
    a=f.read()
    a=a.split('\n')
iter = 0 
for i in a: 
    if  '-->' in i:
        b.append(iter)
    try:
        int(i)
        b.append(iter)
    except:
        pass
    if i == '':
        b.append(iter)
    iter += 1
print(b[len(b)-1])
print(len(a)-1)
iter = 0
for i in b:
    a.pop(i-iter)
    iter += 1
for i in a:
    c.append(i)
with open(p2,"w",encoding='utf-8') as f1:
    for i in c:
        f1.write(f'{i}\n')


