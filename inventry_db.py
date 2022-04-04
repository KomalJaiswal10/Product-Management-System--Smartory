import pymysql as p

def create_con():
    con=p.connect(host="localhost",user='root',password="dineshkomal@2800",database='pyproject')
    return con


def buy_p(t):
    con=create_con()
    cur=con.cursor()
    q="select pname , pqty , pprice from owner where pid = %s;"
    cur.execute(q,t)
    data=cur.fetchall()
    for i in data:
        print("Your Product : ",i[0])
        print("Price : ",i[2])
        print()


def check_pid():
    con=create_con()
    cur=con.cursor()
    q="select*from owner"
    cur.execute(q)
    data=cur.fetchall()
    Lpid=[]
    for i in data:
        Lpid.append(i[0])
        
    con.close()
    return Lpid
    
        
    
def total_price(t):
    con=create_con()
    cur=con.cursor()
    q="select pname , pqty , pprice from owner where pid = %s;"
    cur.execute(q,t)
    data=cur.fetchall()
    for i in data:
        return data

def cust_table(tt):
    con=create_con()
    cur=con.cursor()
    q="insert into customer values (%s,%s,%s,%s,%s)"
    cur.execute(q,tt)
    con.commit()
    con.close()


def update_qty(ut):
    con=create_con()
    cur=con.cursor()
    q="update customer set pqty = %s , total_price =%s where pid = %s"
    cur.execute(q,ut)
    con.commit()
    con.close()

def delete_cust(t):
    con=create_con()
    cur=con.cursor()
    q="delete from customer where pid = %s"
    cur.execute(q,t)
    con.commit()
    con.close()
    
    


def bill():
    con=create_con()
    cur=con.cursor()
    q="select*from customer"
    cur.execute(q)
    data=cur.fetchall()
    for i in data:
        sid=str(i[0])
        sname=str(i[1])
        sqty=str(i[2])
        sprice=str(i[3])
        total=str(i[4])
        print(sid.rjust(10),sname.rjust(10),sqty.rjust(10),sprice.rjust(10),total.rjust(10),sep="               ")


def ret_bill():
    con=create_con()
    cur=con.cursor()
    q="select*from customer"
    cur.execute(q)
    data=cur.fetchall()
    return data

def update_qty_owner(uto):
    con=create_con()
    cur=con.cursor()
    q="update owner set pqty = %s where pid = %s"
    cur.execute(q,uto)
    con.commit()
    con.close()
            
    

def drop_table():
    con=create_con()
    cur=con.cursor()
    q="truncate table customer"
    cur.execute(q)
    con.commit()
    con.close()


def total_pay():
    con=create_con()
    cur=con.cursor()
    q="select pid ,total_price from customer"
    cur.execute(q)
    data=cur.fetchall()
    TL=[]
    s=0
    for i in data:
        TL.append(i[1])
    for i in TL:
        s+=i
    return s
    
    












































def add_po(t):
    con=create_con()
    cur=con.cursor()
    q="insert into owner(pname,pqty,pprice) values (%s,%s,%s)"
    cur.execute(q,t)
    con.commit()
    print()
    print("Data Inserted")
    con.close()

def display_p():
    con=create_con()
    cur=con.cursor()
    q="select*from owner"
    cur.execute(q)
    data=cur.fetchall()
    Lpn=[]
    for i in data:
        Lpn.append(i[1])
        
    con.close()
    return Lpn

def update_p(t):
    con=create_con()
    cur=con.cursor()
    q="update owner set pqty = %s , pprice = %s where pname = %s;"
    cur.execute(q,t)
    con.commit()
    print()
    print("Data Updated")
    con.close()


def delete_p(t):
    con=create_con()
    cur=con.cursor()
    q="delete from owner where pname = %s;"
    cur.execute(q,t)
    con.commit()
    print()
    print("Data Deleted")
    con.close()



def view_p():
    con=create_con()
    cur=con.cursor()
    q="select*from owner order by pid"
    cur.execute(q)
    data=cur.fetchall()
    for i in data:
        sid=str(i[0])
        sname=str(i[1])
        sqty=str(i[2])
        sprice=str(i[3])
        print(sid.rjust(10),sname.rjust(10),sqty.rjust(10),sprice.rjust(10),sep="               ")


def view_spec_p(t):
    con=create_con()
    cur=con.cursor()
    q="select*from owner where pname = %s"
    cur.execute(q,t)
    data=cur.fetchall()
    for i in data:
        print("Product ID","Product Name","Quantity","Price",sep="               ")
        print("--------------------------------------------------------------------------------------------------")
        print(i[0],i[1],i[2],i[3],sep="                        ")






        
































    
