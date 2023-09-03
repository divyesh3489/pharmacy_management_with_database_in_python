import mysql.connector as my
from datetime import *
connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
# Checks if customer exists or not
def c_check_name(name):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q="select * from customer"
    cur.execute(q)
    for i in cur:
        if i[0]==name:
            return True
    return False
# Checks if card exists or not
def card_name(name):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q="select * from card"
    cur.execute(q)
    for i in cur:
        if i[0]==name:
            return True
    return False
# Checks card no
def c_check_no(number):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur1=connect.cursor()
    q=f"select * from customer"
    cur1.execute(q)
    for i in cur1:
        if i[2]==number:
            return True
    return False
# Insert customer's data
def c_insert(name,email,number):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q=f"insert into customer values('{name}','{email}',{number},100)"
    cur.execute(q)
    connect.commit()

# Returns Credit
def c_check_cridit(name):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q=f"select * from customer where c_username='{name}'"
    cur.execute(q)
    for i in cur:
        return i[3]
    
#Update credit
def cridit_update(name,cradit1):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q=f"update customer set cradit=cradit+{cradit1} where c_username='{name}'"
    cur.execute(q)
    connect.commit()
def check_card_name(name):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q=f"select * from card where username='{name}'"
    cur.execute()
    for i in cur:
        if name==i[0]:
            return True    
    return False
def check_card_no(name,card_no,cvv):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q=f"select * from card where username='{name}'"
    cur.execute(q)
    for i in cur:
        if str(card_no)==i[1][12:] and i[2]==cvv:
            return True
    else:
        return False
def check_card_no1(card_no):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q=f"select * from card"
    cur.execute(q)
    for i in cur:
        if str(card_no) == i[1]:
            return False
    return True
def insert_card(name,card_no,cvv):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    card_no=str(card_no)
    q=f"insert into card values('{name}','{card_no}',{cvv})"
    cur.execute(q)
    connect.commit()
def insertsale(name,total):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    day=datetime.now().strftime("%A")
    q=f"insert into sales values('{name}','{day}',{total})"
    cur.execute(q)   
    connect.commit()
def chart():
    d1={'Sunday':[],'Monday':[],'Tuesday':[],'Wednesday':[],'Thursday':[],'Friday':[],'Saturday':[]}
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q="select * from sales"
    cur.execute(q)
    for i in cur:
        d1[i[1]].append(i[2])
    return d1
def check_mo(name,mo_number):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q=f"select * from customer where c_username='{name}'"
    cur.execute(q)
    for i in cur:
        if i[2]==mo_number:
            return True
    return False
