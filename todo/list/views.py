from multiprocessing import context
from django.shortcuts import render,redirect
from .models import List

# Create your views here.

# data = [

#     {
#         'content': 'The quick brown fox jumps over the lazy dogs'
#     },

#       {
#         'content': 'The quick brown fox jumps over the lazy dogs'
#     },

#       {
#         'content': 'The quick brown fox jumps over the lazy dogs'
#     }
# ]



def home(request):
    
    context = {

        'contents' : reversed(List.objects.all())
    }

    if request.method == 'POST':

        content = request.POST['content']
        list = List(content = content)
        list.save()

        return redirect('list-home')

    elif request.method == 'DELETE':

        content = request.POST['content']
        list = List(content = content)
        list.delete()

    return render(request, 'list/home.html', context)