from flask import Flask, jsonify, send_file
import random, os

app = Flask(__name__)

@app.errorhandler(500)
def handle_error(e):
  response = {
    "status": "error",
    "message": str(e)
  }
  return jsonify(response), 500

@app.route('/cat')
def get_cat():
    # Get a list of all the cat images in the directory
    cat_images = [f for f in os.listdir('./static/cats') if f.endswith('.jpg')]
    # Select a random image from the list
    random_cat = random.choice(cat_images)
    response = {
      "status": "success",
      "cat_image_url": "https://3jm.github.io/catapi/" + random_cat
    }
    return jsonify(response)

@app.route('/random-cat')
def random_cat():
    # Get a list of all the cat images in the directory
    cat_images = [f for f in os.listdir('./static/cats') if f.endswith('.jpg')]
    # Select a random image from the list
    random_cat = random.choice(cat_images)
    # Serve the random cat image to the user
    return send_file('./static/cats/' + random_cat)

if __name__ == '__main__':
  app.run(port=80)
