from django.shortcuts import render, redirect
from django.views import View
from .models import Todolist
from .form import TodolistForm

# Create your views here.

class TodoView(View):
    def get(self, request):
        todolist = [1,2,3]
        query = Todolist.objects.all()
        print(query)
        return render(self.request, 'todolist/todolist.html', {'form' : TodolistForm, 'query' : query})
    
    def post(self, request):
        title = request.POST.get('title', None)
        completeid = request.POST.get('completeid', None)
        deleteid = request.POST.get('deleteid', None)
        if title is not None:
            Todolist.objects.create(title=title)
        elif completeid is not None:
            query = Todolist.objects.get(id=completeid)
            if query.complete is True:
                query.complete = False
            else:
                query.complete = True
            query.save()
        elif deleteid is not None:
            query = Todolist.objects.get(id=deleteid)
            query.delete()
        return redirect('todolist')
    
