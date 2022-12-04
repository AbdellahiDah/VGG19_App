from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def index(request):
    return render(request, '../templates/index.html')


def imporet(request):
    
    template = loader.get_template('app_VGGA9/index.html')
    context = {
        'latest_question_list': [12,12],
    }
    return HttpResponse(template.render(context, request))

def import_img(request):
    print(3)
    if request.method == 'POST' :

        imported_data = request.POST['file']
        print(imported_data)
        return render(request, '../templates/index.html')

        