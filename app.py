from flask import Flask

app=Flask(__name__)

@app.route('/')

def webout():

 return '<h1># Add two numbers

# Input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Add the numbers
sum = num1 + num2

# Display the result
print("The sum is:", sum)
</h1>'

app.run(host='0.0.0.0',port=7000)
