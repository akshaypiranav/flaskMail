from flask import Flask,render_template,request
from flask_mail import Mail,Message
app=Flask(__name__)
app.secret_key='123'
@app.route("/")

def index():
    return render_template("index.htm")

@app.route("/send",methods=['POST','GET'])

def send():
    if request.method=="POST":
        sender=request.form['from']
        receiver=request.form['to']
        password=request.form['password']
        message=request.form['message']
        body=request.form['subject']
        

        app.config['MAIL_SERVER']='smtp.gmail.com'
        app.config['MAIL_PORT']=465
        app.config['MAIL_USERNAME']="akshaypiranavb@gmail.com"
        app.config['MAIL_PASSWORD']="xmzc zcuc gprh dnxi"
        app.config['MAIL_USE_TLS']=False
        app.config['MAIL_USE_SSL']=True
        mail=Mail(app)
        msg=Message(message,sender=sender,recipients=[receiver])
        msg.body=body
        mail.send(msg)
        print("SENT MAIL")
        return render_template("index.htm")

if __name__=="__main__":
    app.run(debug=True)    