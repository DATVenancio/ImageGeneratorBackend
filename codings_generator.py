from tensorflow import keras
import sqlite3
from data_manipulation import coding_to_string



connexion = sqlite3.connect("images_db.db")
cursor = connexion.cursor()

fashion_mnist = keras.datasets.fashion_mnist
(images,labels),(_,_) = fashion_mnist.load_data()
images=images/255.0

model_encoder = keras.models.load_model("encoder.h5")

codings= model_encoder.predict(images)

codings_data =[]
for coding in codings:
    coding_string = coding_to_string(coding)
    codings_data.append(coding_string)



query_data=[]

for count,value in enumerate(codings_data):
    query_data.append((value,str(labels[count])))


query ='''
INSERT INTO image_coding(code,label) VALUES (?,?)
'''
cursor.executemany(query,query_data)
    
connexion.commit()
connexion.close()


