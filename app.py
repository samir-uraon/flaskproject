from flask import Flask,request,redirect,render_template
from flask_mysqldb import MySQL
import smtplib
import os
import random
import string
import datetime
from time import sleep

data=False
data1=False
app=Flask(__name__)


picfolder=os.path.join('static','pics')
app.config["UPLOAD_FOLDER"]=picfolder







@app.route("/")
def welcome():
  sleep(2)
  return render_template("welcome.html")
 

 
 
 
@app.route("/about")
def ab():
  sleep(2)
  return render_template("ab.html")
 
 
 
@app.route("/contect")
def co():
  sleep(2)
  time=int(datetime.datetime.now().strftime("%H"))
  t="day"
  if 4<=time<12:
     t="Morning"
  if 12<=time<=14:
     t="Afternoon"
  if 15<=time<=20:
     t="Evening"
  if 21<=time<=3:
     t="Night"
  
  return render_template("cont.html",text=t)



if __name__=="__main__":
  app.run(debug=True,port=3000,host="127.0.0.2")

 