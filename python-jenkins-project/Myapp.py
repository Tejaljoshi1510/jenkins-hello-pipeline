from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, World!"

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		return "Error: Division by zero"
	return a / b

if __name__ == "__main__":
	print("2 + 3 =", add(2, 3))
	print("5 - 2 =", subtract(5, 2))
	print("4 * 3 =", multiply(4, 3))
	print("8 / 2 =", divide(8, 2))
	app.run(host="0.0.0.0", port=5000)
