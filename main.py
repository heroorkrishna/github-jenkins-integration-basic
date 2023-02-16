
# Importing flask module in the project is mandatory
from flask import Flask
 
# Flask constructor takes the name of
app = Flask(__name__)
 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World!!'
    return 'First integration!!'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    app.run()
