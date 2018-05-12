from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
  return "It works! Hello world :)"

if __name == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)

