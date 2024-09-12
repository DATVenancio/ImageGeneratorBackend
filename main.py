
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,send_file,request
import sqlite3
from tensorflow import keras
import numpy as np
import matplotlib.pylab as plt
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/get_image',methods=['POST'])
def teste():
    data = request.json
    print(data['label'])
    conn = sqlite3.connect('./database/images_db.db')
    cursor = conn.cursor()
    query="SELECT * FROM image_coding WHERE label == ? ORDER BY RANDOM() LIMIT 1"
    cursor.execute(query,data['label'])
    coding_string = cursor.fetchall()[0][0]
    coding = [float(x) for x in coding_string.split(",")]
    coding = np.asarray(coding,dtype=float)
    coding = coding.reshape(1,30)
    conn.close()
    print(type(coding_string))
    model_decoder = keras.models.load_model("decoder.h5")
    model_decoder.compile(optimizer=keras.optimizers.SGD(learning_rate=1.5), loss="binary_crossentropy")
    image = model_decoder.predict(coding)[0]
    image_path = 'images/image_generated.png'
    plt.imshow(image, cmap="binary")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(image_path)
    plt.close()
    response = send_file(image_path, mimetype='image/jpeg')

    @response.call_on_close
    def remove_file():
        os.remove(image_path)
    return response


#___________________________


if __name__ == '__main__':
    app.run(debug=True)