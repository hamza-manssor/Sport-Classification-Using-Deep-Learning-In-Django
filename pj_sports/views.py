from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import tensorflow as tf
from tensorflow.keras.models import Model
import json
import numpy as np
# Create your views here.

with open('model/labels.json','r') as f:
    labelInfo = f.read()
labelInfo = json.loads(labelInfo)

def load_images(filename):
    img = image.load_img(filename, target_size=(244,244))
    img = image.img_to_array(img)/255.0
    img = np.expand_dims(img, axis=0)
    return img


def home(request):
    return render(request,'home.html')

def process(request):
    labels = None
    context = {}
    if request.method == 'POST':
        fileObj = request.FILES['filePath']
        fileObj_name = fileObj.name
        fileObj_name = fileObj_name.replace(" ", "_")
        fs = FileSystemStorage()
        filePathName = fs.save(fileObj_name,fileObj)
        url = fs.url(filePathName)
        url_img = '.'+url
        img_pre = load_images(url_img)
        model = load_model('model/sport_classification.h5')
        feature = model.predict(img_pre)
        label=labelInfo[str(np.argmax(feature[0]))]
        context = {'url':url,'label':label}

    return render(request,'process.html',context)