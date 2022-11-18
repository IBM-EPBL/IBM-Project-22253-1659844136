from flask import Flask, render_template, request,session
from werkzeug.utils import secure_filename
import os,cv2
import tensorflow as tf
import numpy as np
from loadModel import *
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
# # Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
 
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'selva'
 
@app.route('/')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      uploaded_img = request.files['file']
      # Extracting uploaded data file name
      img_filename = secure_filename(uploaded_img.filename)
      # Upload file to database (defined uploaded folder in static path)
      uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
      # Storing uploaded file path in flask session
      session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
      img_file_path = session.get('uploaded_img_file_path', None)
      test_image=cv2.imread(img_file_path)
      gray=cv2.cvtColor(test_image,cv2.COLOR_BGR2GRAY)
      resized=cv2.resize(gray,(28,28),interpolation=cv2.INTER_AREA)
      new_img=tf.keras.utils.normalize(resized,axis=1)
      new_img=np.array(new_img).reshape(-1,28,28,1)
      model =getModel()
      prediction=model.predict(new_img)
      # print(np.argmax(prediction))
      # f.save(secure_filename(f.filename))
      recognized=str(np.argmax(prediction))
      return render_template('display_predict.html', user_image = img_file_path,recognized=recognized)



if __name__ == '__main__':
   app.run(debug = True)