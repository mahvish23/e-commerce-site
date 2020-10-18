


from flask import Flask, render_template, request, jsonify,session,redirect,url_for,session

import re
import dbHandle
import json

app = Flask(__name__)

app.config['SECRET_KEY']=   'jjjj'

@app.route('/',methods=['POST','GET'])

def login():
    mssg=""
    if request.method=='POST':
        form_data = request.form.to_dict()
        print(form_data)
        

        session['email'] = form_data['email']
        passwd = form_data['pass']
        emailexp = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    
        if not re.match(str(emailexp), str(session['email'])):
            mssg= "Enter a valid email"
            return render_template('index.html',mssg=mssg)
        elif passwd == '':
            mssg= "Enter your password"
            return render_template('index.html',mssg=mssg)
        #print(email)
        success = dbHandle.login(str(session['email']), passwd)
        print(success)
        if success == -1:
            print("Email id not found")
            mssg= "email id not found please register"
        elif success == 0:
            print("Incorrect password")
            mssg= "incorrect password"
        elif success == 1:
            print("Login Success")
            #session['email'] = email
            #user_info = dbHandle.get_userdetails(email)
        #return jsonify(success=1,user_info=user_info)
            
            return redirect(url_for('dashboard'))
        
    
    return render_template('index.html',mssg=mssg)
    



@app.route('/register',methods=['POST','GET'])
def register():
    mssg=""
    form_data=request.form.to_dict()
    print(form_data)
    if request.method=='POST':
        name=form_data['username']
        session['email']=form_data['email']
        passwd=form_data['password']
        rep_passwd=form_data['repeat-pass']
        emailexp = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(str(emailexp), str(session['email'])):
            mssg= "Enter a valid email"
            return render_template('r.html',mssg=mssg)
        elif passwd=='':
            mssg= "Enter your password"
            return render_template('r.html',mssg=mssg)
        elif rep_passwd=='':
            mssg= "Enter rep_password"
            return render_template('r.html',mssg=mssg)
        elif passwd!=rep_passwd:
            mssg= "Passwords do not match"
            return render_template('r.html',mssg=mssg)
        success=dbHandle.user_registration(name,session['email'],passwd)
        if success==1:
            print("Registration successful")
            #print(email)
            #user_info=dbHandle.get_userdetails(email)
            print(success)
        
            
        
            return redirect(url_for('dashboard'))
        #return jsonify(success=1, user_info=user_info)
        elif success==0:
            mssg= "Email already exists,Please login!!"
    return render_template('r.html',mssg=mssg)
    

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    #email= request.args.get('email')
    if request.method=='POST':
        print("k")
        form_data = request.form.to_dict()
        print(form_data)
        url = form_data['url']
        print(url)
        
        #print(session['email'])
        user_info = dbHandle.get_userdetails(session['email'])
        userid=user_info[0][0]
        
        dbHandle.add_product(str(url),int(userid))
        return redirect(url_for('dashboard'))
    else:#email= request.args.get('email')
        #print(session['email'])
        user_info = dbHandle.get_userdetails(session['email'])
        userid=user_info[0][0]
        print(userid)
    productlist=dbHandle.get_products(userid)
    #print((productlist))
    
    if len(productlist)==0:
        success=""
        return render_template('dashboard.html',user_info=user_info,success=success)
        
    else:
        l=len(productlist)
        return render_template('dashboard.html',user_info=user_info,l=l,productlist=productlist)
        
    



    
    
   
    
#return render_template('dashboard.html',user_info=user_info,)  

        
@app.route('/logout', methods=["POST","GET"])
def logout():
#     user_info = dbHandle.get_userdetails(session['email'])
#     userid=user_info[0][0]
#     dbHandle.delprod(userid)
#     return redirect(url_for('dashboard'))
    session.pop('email', None)
    #print(session['email'])
    return redirect(url_for('login'))

app.run(debug=True)


	


