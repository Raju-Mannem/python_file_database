
def fileinsert():
    file=str(input("enter name of the file      "))
    wm=open(file,mode="a")
    nc=int(input("enter no of input fields:   "))
    nr=int(input("enter no of reocrds:   "))
    wm.write('---------------------------------------------------------------------------------------------------------------------------------')
    wm.write('\n')
    wm.write('\t')
    for i in range(nc+1):
        if(i>0):
            print("enter the name of field %d"%i)
            fn=input()
            wm.writelines(fn)
            wm.write('\t')
            wm.write('\t')
    wm.write('\n')
    wm.write('---------------------------------------------------------------------------------------------------------------------------------')
    for i in range(nc+1):
        wm.write('\n')
        if(i>0):
            wm.write(str(i))
            for j in range(nr+1):
                if(j>0 and i>0):
                    wm.write('\t')
                    print("enter the row %d data in the field %d"%(i,j))
                    data=input()
                    wm.writelines(data)
                    wm.write('\t')
            wm.write('\n')
    wm.write('---------------------------------------------------------------------------------------------------------------------------------')
    wm.close()
fileinsert()

def filesearch():
    cnt=0
    file=str(input("enter name of the file      "))
    rm=open(file,mode="r")
    line=rm.readlines()
    search=str(input("enter data for search:    "))
    for sh in line:
        if sh.find(search)!= -1:
            cnt+=1
            print('exist')
            print(sh)
    if cnt==0:
        print("not exist")
    rm.close()
filesearch()
