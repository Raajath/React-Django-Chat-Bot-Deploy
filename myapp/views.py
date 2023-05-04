
from django.shortcuts import render
from myapp.my_function import my_function
import json
def my_view(request):
    """
    if request.method == 'POST':
        text = request.POST.get('text')
        result = my_function(text)
        context = {'result': result}
    else:
        context = {}
    """
    return render(request, 'index.html')

from django.http import JsonResponse, HttpResponseBadRequest

from django.views.decorators.csrf import csrf_exempt
from myapp.my_function import my_function


@csrf_exempt
def preprocess_text(request):
    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        input_text = data['input_text']

        # Preprocess the input text
        
        processed_text = my_function(input_text)

        return JsonResponse({'processed_text': processed_text})
    else:
        return HttpResponseBadRequest("Invalid request")



