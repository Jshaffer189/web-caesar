from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/encrypt" method="POST">
        <label for ="rot">Rotation:</label>
        <input type="text" name="rot" value="0"> </input>
        <textarea name="text">{0}</textarea>
        <input type="submit" />
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']
    the_encryption = rotate_string(text, rot)
    return form.format(the_encryption)

@app.route("/")
def index():
    return form.format("")



app.run()