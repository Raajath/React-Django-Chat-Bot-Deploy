
from django.shortcuts import render
from myapp.my_function import my_function

def my_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        result = my_function(text)
        context = {'result': result}
    else:
        context = {}
    return render(request, 'myapp/index.html', context)
