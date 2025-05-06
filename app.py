from flask import Flask

app=Flask(__name__)

@app.route('/')

def webout():

<<<<<<< HEAD
 return '<h1>DevOps is so much fun to learn. i love myself Rohit............</h1>'
=======
 return '<h1># Add two numbers

# Input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Add the numbers
sum = num1 + num2

# Display the result
print("The sum is:", sum)
</h1>'
>>>>>>> 08a0ec82c1cc3fb10d5ef4537f568a25cd61440c

app.run(host='0.0.0.0',port=7000)
