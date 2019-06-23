class customer:
    bankname = 'ABC Bank'
    def __init__(self):
        self.custid = '0'
        self.name = ''

    def PrintState(self):
        print('Customer Statement for custid : %i, name : %s'
              %(self.custid,self.name))

class recust(customer):
    def __init__(self):
        super().__init__()
        self.wlimit = 1000

        def balNotify(self,lstbal:list):
            bal = sum(lstbal[-3:])/3
            strmsg = ''
            if bal < 10000:
                strmsg = 'Low Balance Charges willbe 100'
            else:
                strmsg = 'No Charges'
            return strmsg
class goldcust(customer):
    def __init__(self):
        super().__init__()
        self.RM=''
    def balNotify(selfself,lstbal: list):
        bal = sum(lstbal)/len(lstbal)
        strmsg = ''
        if bal<100000:
            strmsg ='Low balance charges willbe 500'
        else:
            strmsg = 'No Charges'
        return strmsg
rc = recust()
rc.custid = '100'
rc.name = 'Customer1'
rc.wlimit = 2000

gc = goldcust()
gc.custid = '100'
gc.name ='Customer 2'
gc.RM = 'Manager'

def notify(cust1,lstbal1):
    msg1=cust1.balNotify(lstbal1)
    return msg1

str = 'G'

if str == 'R':
    mntbal1 = [10000,15000,10000,10000]
    msg2 = notify(rc,mntbal1)

else:
    mntbal2 = [10000,15000,10000,10000]
    msg2 = notify(gc,mntbal2)

print(msg2)