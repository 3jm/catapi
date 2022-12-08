from flask import Flask, send_file, make_response
import random

app = Flask(__name__)

@app.route('/style.css')
def get_stylesheet():
    with open('style.css', 'r') as f:
        return send_file(f, mimetype='text/css')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cat')
def get_cat_image():
    # Generate a random number between 1 and 10
    rand_num = random.randint(1, 10)
    
    try:
        # Open the corresponding cat image file
        f = open(f'cat{rand_num}.jpg', 'rb')
        
        # Send the cat image back to the user
        return send_file(f, mimetype='image/jpg')
    except FileNotFoundError:
        # If the image file is not found, return an error response
        error_response = make_response(
            "<body style='background-color: #13131a;'>"
            "<img src='https://cdn.discordapp.com/attachments/939437550907572255/1050219432393326664/A6OgohXCMAAzhYU.jpg' style='display: block; margin: 0 auto; margin-top: 20px; width: 250px; height: 250px;'>"
            "<h1 style='text-align: center; font-size: 32px; margin-top: 50px; color: #ffffff; font-family: sans-serif; font-weight: bold;'>Internal Error: Image not found</h1>"
            "<p style='text-align: center; font-size: 16px; color: #545454; font-family: sans-serif; font-weight: bold;'>The specified cat image could not be found</p>"
            "<p style='text-align: center; font-size: 10px; color: #545454; font-family: sans-serif; font-weight: bold;'>Made by <b style='color: #787878';>Blind</b> & <b style='color: #787878';>ChatGPT</b></p>"
            "</body>",
            500
        )
        return error_response

if __name__ == '__main__':
    app.run(port=80)
