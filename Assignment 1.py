#Assignment 1
def getcount(a,b):
    x=a.count('Python')
    y=a.count('R')
    z=b[0]*x+b[1]*y
    return(z)
def appDict(emp,cour,cost):
    elst1=[]
    elst2=[]
    applst=[]
    for i in range(0,len(emp)):
        elst1.append(emp[i])
        elst2.append(cour[i])
    TotInv = getcount(elst2,cost)
    if(TotInv>70000):
        for j in range(len(elst1)-1,0,-1):
            elst1.pop(j)
            elst2.pop(j)
            TotInv=getcount(elst2,cost)

            if(TotInv<70000):
                break
    else:
        print("All Courses Approved")


    for k in range(0,len(elst2)):
        applst.append('Yes')
    z = zip(elst1, applst)
    finallst=dict(z)
    print('Total Investment Made',TotInv)
    return(finallst)

fee = {'Python': 15000, 'R': 12000}
n1 = {101:'Python',102:'R',103:'Python',104:'Python',105:'R',106:'Python',107:'R'}
n1emp=n1.keys()
emplst=list(n1emp)
n1course=n1.values()
n1fee=fee.values()
feelst=list(n1fee)
courlst=list(n1course)
a=appDict(emplst, courlst,feelst)
print(a)



