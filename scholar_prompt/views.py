from django.shortcuts import render
from .forms import PromptForm
from .scholar import Gscholar
# Create your views here.
form = PromptForm()
def index(request): 
    form = PromptForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            query = form.cleaned_data['scholar_query']
            S = Gscholar(query)
            authors = next(S)
            return render(request,'scholar_prompt/scholars.html',{'authors':authors}) 

    else:
        return render(request,'scholar_prompt/index.html',{'form':form})