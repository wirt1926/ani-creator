from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def hello():
  return "It works! Hello world :)"

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)

@app.route("/order-animation")
def order_animation():
  return render_template("order_animation.html", invitation= "Welcome on ani creator")

@app.route("/upload")
def upload():
  if 'my_file' not in request.files[]:
    return "not yet"
  upl_file = request.files[my_file]
  storage.save('CustomerFiles', upl_file)
