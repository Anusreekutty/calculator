from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def culculator():

    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def hi():
    if request.method=='POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operation = request.form['operation'] 
        output=cal(num1,num2,operation)
    return render_template('result.html',operation=operation,output=output)
        if operation == 'Addition':
           return(num1+num2)
        elif operation == 'Subtraction':
            return(num1-num2)
        elif operation =='Multiplication':
          return(num1*num2)
        elif operation == 'Division' :
           return(num1/num2)
        elif operation =='square':
           return(num1**num2)
        elif operation == 'modulus':
          return(num1%num2)    
if __name__=='main_':
    app.run()