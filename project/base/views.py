from django.shortcuts import render
from django.core.paginator import Paginator
from base.models import ToDo

# Create your views here.
def index(request):
    alltodo = ToDo.objects.all() #Fetch all todos
    paginator = Paginator(alltodo,3,1) #Set per items page 
    page = request.GET.get('page') #request every page 
    todos = paginator.get_page(page) #get page
    context = {'todos':todos, 'alltodo':alltodo}
    return render(request, 'index.html', context)