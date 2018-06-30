# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:25:57 2018

@author: Lenovo 
"""

from ham_spam import ham
import subprocess
subprocess.call(["python", "ham_spam.py"])

from flask import Flask, request
app = Flask(__name__)


      
#call your method to check entered text is spam or ham
@app.route('/check',methods = ['POST','GET'])
def check():
    
     if request.method == 'POST':
        user = request.form['text_name']
        resp = ham(user)
        #check_spam_ham(user)
        #print(resp)
        
        return resp



   
 


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000,debug=False) 
    
    
