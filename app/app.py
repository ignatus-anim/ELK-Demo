from flask import Flask, request
import logging

app = Flask(__name__)

# Set up logging
logger = logging.getLogger('flask_app')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('/app/logs/app.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/')
def index():
    logger.info(f"GET request from {request.remote_addr}")
    return "Hello, ELK!"

@app.route('/error')
def error():
    logger.error("This is a test error log.")
    return "Something went wrong!", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

