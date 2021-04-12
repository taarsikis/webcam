""" GitHub """

import cv2
import time
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def index():
    """
    Opens start page.
    """
    return render_template("index.html")

def take_photo(name):
    cap = cv2.VideoCapture(0)

    for i in range(30):
        cap.read()

    # Делаем снимок
    ret, frame = cap.read()

    # Записываем в файл
    # cv2.imwrite(f'{name}.png', frame)
    time.sleep(1)

    # Отключаем камеру
    cap.release()


@app.route("/register", methods=['POST'])
def register():
    """
    Checks requests and generates map.
    """
    nickname = request.form.get("Nickname")
    if not nickname:
        return render_template("failure.html")
    take_photo(nickname)
    return render_template("nice.html")

if __name__ == "__main__":
    app.run(debug=False)