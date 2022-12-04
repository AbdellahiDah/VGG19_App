from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import base_img

import tensorflow as tf  #Line 1
VGG_19_pre_trained= tf.keras.applications.VGG19( include_top=True, weights="imagenet", input_tensor=None,input_shape=(224, 224, 3), pooling="max", classes=1000,classifier_activation="softmax") #Line 1

   


def index(request):

    return render(request, '../templates/index.html')


def imporet(request):
    
    template = loader.get_template('app_VGGA9/index.html')
    context = {
        'latest_question_list': [12,12],
    }
    return HttpResponse(template.render(context, request))

def import_img(request):
    print(333333333333333)
    Database_delete  = base_img.objects.all().delete()

    if request.method == 'POST' :

        #imported_img = request.POST['file'] 
        imported_img = "arash-af10.jpg"
        #obj= base_img.objects.create(photo= imported_img)

        #DB=base_img.objects.all()
        #img = DB.photo.all()

        image = tf.keras.preprocessing.image.load_img(imported_img, target_size=(224, 224))  #Line 2
        image = tf.keras.preprocessing.image.img_to_array(image) #Line 3
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2])) #Line 4
        image = tf.keras.applications.vgg19.preprocess_input(image) #Line 5



        VGG_19_prediction = VGG_19_pre_trained.predict(image) #Line 3
        Top_predictions = tf.keras.applications.vgg19.decode_predictions(VGG_19_prediction , top=5) #Line 4
        type_predic_1 = Top_predictions[0][0][1]
        prob_predic_1 = Top_predictions[0][0][2]

        type_predic_1 = Top_predictions[0][1][1]
        prob_predic_1 = Top_predictions[0][1][2]

        print(333333333333333)
        return render(request, '../templates/index.html',{'type_predic_1':type_predic_1,'prob_predic_1':prob_predic_1})

        