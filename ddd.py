from flask import Flask, render_template
import os
app = Flask(__name__)


IMG_FOLDER = os.path.join("static", "IMG")

app.config["UPLOAD_FOLDER"] = IMG_FOLDER

@app.route('/')
def qunava():
    ledibag = os.path.join(app.config["UPLOAD_FOLDER"], "llkk.jpg")
    cat = os.path.join(app.config["UPLOAD_FOLDER"], "kot.jpg")
    lila = os.path.join(app.config["UPLOAD_FOLDER"], "lila.jpg")
    agrest = os.path.join(app.config["UPLOAD_FOLDER"], "agro.jpg")
    return render_template('index.html', user_image=ledibag, cat=cat, lila=lila, agro=agrest)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')