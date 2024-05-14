from flask import Flask
from threading import Thread

# Configure flask server
app = Flask('')

@app.route('/')
def home() :
    return "Celestial Alert Server Running, Status: Ok(200)"

def run():
    # app.debug = True 
    app.run(host='0.0.0.0', port=8000)

# Keep the server alive
def keep_alive(): 
    t = Thread(target=run)
    t.start()
