import mysql.connector
import getting_the_price


def connect():
    try :
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mahiyami2308',
            database='smart',
        )
    except():
        connect()
    return mydb


def user_registration(username: str, emailid: str, passwd: str):
    mydb = connect()
    mycursor = mydb.cursor()
    #hassedPasswd = bcrypt.hashpw(passwd.encode("utf-8"), bcrypt.gensalt())
    try:
        insertFn = "INSERT INTO user_info (username,emailid,password) VALUES (%s, %s, %s)"
        registration_info = (username, emailid, passwd)
        mycursor.execute(insertFn, registration_info)
        mydb.commit()
        return 1
    except :
        return 0 #email exists


def login(emailid: str, passwd: str):
    mydb = connect()
    mycursor = mydb.cursor()
    print(emailid)
    mycursor.execute("SELECT password from user_info where emailid = \""+emailid+"\"")
    fetched_list = mycursor.fetchall()
    if(len(fetched_list)==0):
        return -1   #email id not found

    else:
        hassedPasswd = fetched_list[0][0]
        if (passwd== hassedPasswd):
            return 1  #login success
        else :
            return 0  #incorrect password

def get_userdetails(email: str):
    mydb = connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from user_info where emailid = \"" + email + "\"")
    fetched_list = mycursor.fetchall()
    le = len(fetched_list)
    print(fetched_list)
    if le == 0:
        return -1  # no such user found
    else:
        # user_info= {"userid": fetched_list[0][0],

        #             "username": fetched_list[0][1],
        #             "emailid": fetched_list[0][2]
                    
                    
        return fetched_list

    
def add_product(url: str, userid: int):
    try:
        price = getting_the_price.get_price(url)
        print(price)
        
    except():
        return -1 #price could not be fetched for item (site is still not added)
    mydb = connect()
    mycursor = mydb.cursor()
    
        # if product don't exists in the database
    print(price[0])
    try:
        insertFn = "INSERT INTO product (url,price,prodname) VALUES (%s,%s,%s)"
        product = (url,price[0],price[1])
        mycursor.execute(insertFn, product)
        mydb.commit()
        mycursor.execute("SELECT * from product")
        l=mycursor.fetchall()
        
        mydb.commit()
    
    except:
    # #     # if the product is in database
    # #     print("error")
          pass
    mycursor.execute("SELECT productid from product where url = \"" + url + "\"")
    product_id = int(mycursor.fetchall()[0][0])
    # mapping product with user id
    insertFn = "INSERT INTO maping (user_id, product_id) VALUES (%s, %s)"
    mapping_info = (userid, product_id)
    mycursor.execute(insertFn, mapping_info)
    mydb.commit()

def get_products(userid: int):
    mydb = connect()
    mycursor = mydb.cursor()
    productlist = []
    print(userid)
    mycursor.execute("SELECT product_id from maping where user_id ="+str(userid) )
    fetched_list = mycursor.fetchall()
    #print(fetched_list)
    #productid=int(fetched_list)
    le = len(fetched_list)
    if le == 0:
        return productlist  #no products register
    else:
        for i in range(le):
            p=(fetched_list[i][0])
            #print(productid)
            mycursor.execute("select * from product where productid =" +str(p))
            l = mycursor.fetchall()
            
            
            tempdict = {"product_id": l[0][0],
                             "url": l[0][1],
                             "price_init": l[0][2],
                             
                             "product_name": l[0][3][0:21]}
            # else:
            #     tempdict = {"product_id": list[0][0],
            #                 "aff_url": list[0][2],
            #                 "price_init": list[0][3],
            #                 "price_update": list[0][4],
            #                 "product_name": list[0][5][0:20]}
            productlist.append(tempdict)
        productlist=notify(productlist)
        print(productlist)
        return productlist

def notify(productlist):
    print(productlist)
    le=len(productlist)
    print(le)
    for i in range(le):
         price=getting_the_price.get_price(productlist[i]['url'])
         
          
         if int(price[0])<int(productlist[i]['price_init']):
             productlist[i]['price_init']=price[0]

    return productlist

# def delprod(email):
#     mycursor.execute("SELECT product_id from maping where user_id = user_id ")
#     fetched_list = mycursor.fetchall()
#     mycursor.execute("")            
