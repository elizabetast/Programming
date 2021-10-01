s=0
sp=0
so=0
a=1
while a!=0:
    a=input()
    if ord('0')<=ord(a[0])<=ord('9') or ord(a[0])==ord('-'):
        fl=1
        for i in range(1,len(a)):
            if ord('0')<=ord(a[i])<=ord('9'):
                fl=1
            else: fl=0
        if fl==1:
            a=int(a)
            s+=a
            if a>0:sp+=a
            else:so+=a
print(s,sp,so)
