import database as db
import customer as cu
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
#for payment method cash and card
class Payment:
    def p_menu(self, name, l_cart):
        n = int(input("1.For Cash Payment\n2.For Card Payment\n"))
        if n == 1:
            self.display(l_cart, name)
            self.cash()
        elif n == 2:
            self.display(l_cart, name)
            self.card_payment()
        else:
            print("\nInvalid Choice\n")
            pass
# To display cart
    def display(self, l_cart, name):
        date = datetime.now() # Current time and date
        print(f'Username:{name}\t Date:{date.strftime("%d/%m/%Y")}\t time:{date.strftime("%H:%M:%S")}')
        self.total = 0
        self.l_cart = l_cart
        self.name = name
        print("MedicinName\tPrice\t\tQuantity\tTotal")
        print()
        for i in self.l_cart:
            print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t{i[1]*i[2]}")
            self.total += (i[1]*i[2])
        if cu.c_check_cridit(name) >= 1000:
            discount = self.total*0.15
            self.total -= discount
        else:
            discount = self.total*0.05
            self.total -= discount
        print(f"Discount\t\t\t\t{discount}")
        print()
        print(f"Total\t\t\t\t\t{self.total}\n")

# Cash Method
    def cash(self):
        self.p_cash = int(input("Enter Cash Value:"))
        if self.p_cash >= self.total:
            print("Thank You For Purchase")
            print(f"Your Change:{round(self.p_cash-self.total)}\n")
            cu.insertsale(self.name, self.total)
            self.update()
        else:
            print("\nInsufficient Cash\n")
            self.cash()

# Update credit of customer
    def update(self):
        for i in self.l_cart:
            db.q_update(i[0], i[2])
        if cu.c_check_cridit(self.name) >= 1000:
            cu.cridit_update(self.name, -1000)
        else:
            cu.cridit_update(self.name, self.total)

# Card payment
    def card_payment(self):
        if cu.card_name(self.name): # Checks if card exists or not
            self.card_number = int(
                input("Enter your last 4 digit of your card:"))
            self.card_cvv = int(input("Enter your card cvv:"))
            if cu.check_card_no(self.name, self.card_number, self.card_cvv):
                print("\nPayment Successful\n")
                print("\nThank You For Purchase\n")
                self.update()
            else:
                print("card number not found or Enter cvv not match with your card number\n")
                c = True
                while c == True:
                    n = int(
                        input("1.For Enter Again CardNumber\n2.For Add NewCard\n3.For Cash\n4.main menu\n"))
                    if n == 1:
                        self.card_payment()
                        c = False
                    elif n == 2:
                        self.add_card()
                        c = False
                    elif n == 3:
                        self.cash()
                        c = False
                    elif n==4:
                        c=False                    
                    else:
                        print("\nEnter Valid Choise\n")
        else:
            self.add_card()

#Add new Card
    def add_card(self):
        self.card_number = int(input("Enter Your Card Number:"))
        self.card_cvv = int(input("Enter your card cvv:"))
        if cu.check_card_no1(self.card_number) and len(str(self.card_number)) == 16 and len(str(self.card_cvv))== 3:
            cu.insert_card(self.name, self.card_number, self.card_cvv)
            print("\nPayment Successful\n")
            print("\nThank You For Purchase\n")
            self.update()
        else:
            print("\nEnter Card Number Is All Redy Exits Or Invalid Card number Or Invalid CVV\n")
            c = True
            while c == True:
                n = int(input("1.For Enter Again CardNumber\n2.For Cash\n"))
                if n == 1:
                    self.add_card()
                    c = False
                elif n == 2:
                    self.cash()
                    c = False
                else:
                    print("\nEnter Valid Choise\n")

# Create Cart for Customer
class Cart(Payment):
    def addto_cart(self, name): # Adds in cart
        n = int(input("Enter Number Medicine You Want To Buy:"))
        self.l_cart = []
        for i in range(n):
            self.M_name = input("Enter Medicine Name:").upper()
            if db.check_name(self.M_name):
                self.quntity = int(input("Enter Qauntity of Medicin:"))
                if self.quntity <= db.check_quntity(self.M_name) and self.quntity > 0:
                    self.l_cart.append(
                        [self.M_name, db.price(self.M_name), self.quntity])
                elif self.quntity <= 0:
                    print("\nPlz enter Qauntity In Positive Number\n")
                else:
                    print(f"\nWe have Only {db.check_quntity(self.M_name)} Left of This {self.M_name} or Medicine Out of Stock\n")
            else:
                print(f"\nWe Don't Have Madicine {self.M_name}\n")
        if len(self.l_cart) != 0:
            self.p_menu(name, self.l_cart)
        else:
            print("\ncart is empty\n")

# Customer class
class Customer(Cart):
    def new_custmor(self): # Adds new customer
        self.c_username = input("Enter Your Name:").lower()
        self.c_email = input("Enter Email Address:")
        self.c_Mobileno = int(input("Enter your Mobile Number:"))
        if cu.c_check_name(self.c_username) != True:
            if cu.c_check_no(self.c_Mobileno) != True:
                if len(str(self.c_Mobileno)) == 10 and self.c_Mobileno > 0:
                    cu.c_insert(self.c_username, self.c_email, self.c_Mobileno)
                    self.addto_cart(self.c_username)
                else:
                    print("\nInvaild Mobile Number\n")
            else:
                print("\nEnter Mobile Number Is Exist\n")
        else:
            print("\nUser name is Exist\n")

    def exist_custmor(self): #Checks if customer exiss or not
        self.c_username = input("Enter User Name:").lower()
        self.c_Mobileno = int(input("Enter Mobile number:"))
        if cu.c_check_name(self.c_username) and cu.check_mo(self.c_username,self.c_Mobileno):
            self.addto_cart(self.c_username)
        else:
            print("\nEnter Number or Username not Vaild\n")

# Inventory Class-> Manage Inventory
class Inventory:
    def i_menu(self):
        n = int(input("1.show Inventory\n2.Add Medicine\n3.Update Medicine\n4.Remove Medicine\n5.For Show Sale On DayWise\n"))
        if n == 1: # Show inventory 
            n1= int(input("1.Terminal display\n2.Graphical Representation\n"))  
            if n1==1: 
                db.select1()
            elif n1==2: 
                m_name,m_price,m_quantity=db.select()
                plt.figure(figsize=(12,12))
                e_max=max(m_quantity)
                e_index=m_quantity.index(e_max)
                explodes=np.zeros(shape=(len(m_quantity)))
                explodes[e_index]=0.2
                plt.suptitle("Inventory")
                plt.subplot(2,1,1)
                plt.title("Quantity",loc="left")
                plt.pie(m_quantity,labels=m_name,autopct="%1.1f%%",explode=explodes)
                plt.subplot(2,1,2)
                plt.xlabel("Name of Medicine")
                plt.ylabel("Price")
                plt.bar(m_name,m_price)
                plt.show()
            else:
                pass
        elif n == 2: # Add medicine
            self.m_id = abs(int(input("Enter Medicine Id:")))
            self.m_name = input("Enter Medicine Name:").upper()
            while 1:
                self.m_price = int(input("Enter Medicine Price:"))
                if self.m_price <0:
                    print("\nEnter price in positive\n")
                else:
                    break
            while 1:
                self.m_quntity = int(input("Enter Medicine Quantity:"))
                if self.m_quntity <0:
                     print("\nEnter quantity in positive\n")
                else:
                    break
            db.M_add(self.m_id, self.m_name, self.m_price, self.m_quntity)
        elif n == 3: # Update Medicine
            self.M_name = input("Enter Name Of Medicine You Want To Update:").upper()
            while 1:
                self.M_price = int(input("Enter Medicine Price:"))
                if self.M_price <0:
                    print("\nEnter price in positive\n")
                else:
                    break
            while 1:
                self.M_quntity = int(input("Enter Medicine Quantity:"))
                if self.M_quntity<0:
                    print("\nEnter qauntity in positive\n")
                else:
                    break
            db.M_update(self.M_name, self.M_price, self.M_quntity)
        elif n == 4: # Remove medicine
            self.M_name = input("Enter Name Of Medicine You Want To Remove:")
            db.M_Remove(self.M_name)
        elif n == 5: # Shows sales in bar plot
            d = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
            d1 = cu.chart()
            l = []
            for i in d1.values():
                l.append(sum(i))
            plt.bar(d, l)
            plt.xlabel('Day')
            plt.ylabel('Sales')
            plt.title('Sales on each day')
            plt.show()


class Main_Menu(Inventory, Customer):
    def __init__(self) -> None:
        self.I_name = "Manager"
        self.password = 1234
        self.menu()

    def menu(self):
        n = int(
            input("1.For Manage Inventory\n2.For Exist Customer\n3.For New Customer\n4.exit\n"))
        if n == 1:
            name = input("Enter username:")
            password = int(input("Enter Password:"))
            if name == self.I_name and password == self.password:
                self.i_menu()
                self.menu()
            else:
                print("\nUsername or password is invalid\n")
                self.menu()
        if n == 2:
            self.exist_custmor()
            self.menu()
        if n == 3:
            self.new_custmor()
            self.menu()
        if n==4:
            pass
        else:
            print("\nInvalid Input\n")
            self.menu()

try:
    obj = Main_Menu()
except Exception as e:
    print(e)
