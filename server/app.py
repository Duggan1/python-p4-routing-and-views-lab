#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

#index()
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

#print_string
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

#count 
@app.route('/count/<int:parameter>')
def count(parameter):
    countTotal = ''
    for n in range(parameter):
        countTotal += f"{n}\n"
    return countTotal

#math
@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1,operation,num2):
    switch = {
        "+":f"{num1 + num2}",
        "-":f"{num1 - num2}",
        "*":f"{num1 * num2}",
        "div":f"{num1 / num2}",
        "%":f"{num1 % num2}"
    }
    return switch.get(operation)




if __name__ == '__main__':
    app.run(port=5555, debug=True)


