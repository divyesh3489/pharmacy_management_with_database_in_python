import mysql.connector as my
connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
#Show inventory in terminal
def select1():
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q="select * from inventry"
    cur.execute(q)
    row=cur.fetchall()
    print(("id","name","price","quntity"))
    count=1
    for i in row:
        print('\n\nMedicine',count)
        # print(f"id\tname\tprice\tquantity")
        print("Id:-",i[0])
        print("Name:-",i[1])
        print("Price:-",i[2])
        print("Quantity:-",i[3])
        count+=1
        print("")
# Returns list of inventory
def select():
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q="select * from inventry"
    cur.execute(q)
    m_name=[]
    quantity=[]
    m_price=[]
    for i in cur:
        m_name.append(i[1])
        quantity.append(i[3])
        m_price.append(i[2])
    return m_name,m_price,quantity
try:
    def M_add(id,name,price,amount): # Adds Medicine
            connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
            cur=connect.cursor()
            q=f"insert into inventry values({id},'{name}',{price},{amount})"
            cur.execute(q)
            connect.commit()
            print("Medicine Add Succesful")
except Exception as e:
    print(Exception)
try:
    def M_update(name,price,amount): # Updates Medicine
        connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
        if check_name(name):
            cur=connect.cursor()
            q=f"update inventry set price={price},amount=amount+{amount} where item_name='{name}'"
            cur.execute(q)
            connect.commit()
            print("Medicine Update Succesful")
        else:
             print("Medicine Record not found")
except Exception as e:
    print(Exception)
try:
    def M_Remove(name): # Remove medicine
        connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
        if check_name(name):
            cur=connect.cursor()
            q=f"delete from inventry where item_name='{name}'"
            cur.execute(q)
            connect.commit()
            print("Medicine remove Succesful")
        else:
            print("Medicine Record not found")
except:
    print(Exception)
def check_name(name):#check medicine name exists or not
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q="select * from inventry"
    cur.execute(q)
    m_name=[]
    for i in cur:
        m_name.append(i[1])
    if name in m_name:
        return True
    else:
        return False
# Returns quantity of medicine
def check_quntity(name):
    connect=my.connect(host="localhost",port="3306",user='root',password="*Dvg2004#",database='project')
    cur=connect.cursor()
    q=f"select * from inventry where item_name='{name}'"
    cur.execute(q)
    for i in cur:
        return i[3]
# Returns price of medicine
def price(name):
    cur=connect.cursor()
    q=f"select * from inventry where item_name='{name}'"
    cur.execute(q)
    for i in cur:
        return i[2]
    
# Updates quantity
def q_update(name,quntity):
    cur=connect.cursor()
    q=f"update inventry set amount=amount-{quntity} where item_name='{name}'"
    cur.execute(q)
    connect.commit()