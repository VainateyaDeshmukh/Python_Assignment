#Assignment 2


def appDict(emp,cost):
    costlst=cost
    emplst=emp
    elst=[]
    Inv=0
    i=0
    TotInv = 0
    while (i < len(emplst)):
        TotInv = costlst[i] + TotInv
        if (TotInv<80000):
            Inv=TotInv
            elst.append('Yes')
        else:
            elst.append('No')
        i=i+1
    print('Total Investment Made',Inv)
    z=zip(emplst,elst)
    finallst=dict(z)
    return(finallst)

cost = {101: 18000, 102: 15000, 103: 18000, 104: 12000, 105: 15000, 106: 15000, 107: 12000}
n1emp=cost.keys()
emplst=list(n1emp)
n1fee=cost.values()
feelst=list(n1fee)
a=appDict(emplst,feelst)
print(a)