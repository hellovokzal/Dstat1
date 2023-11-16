from flask import Flask

num = 0

app = Flask(__name__)

@app.route("/")

def g():
	global num
	num = num + 1
	return f"Запросов: {num}"
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
