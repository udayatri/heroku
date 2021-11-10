from flask import Flask

app = Flask(__name__) #create a flask object

@app.route('/')
def index():
  return "helo world"


if __name__ == '__main__':
    app.run(debug= False ) #debug enabled is creating warning and error