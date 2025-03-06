from django.shortcuts import render
from .forms import PromptForm
from .scholar import Gscholar
from django.views import View
# Create your views here.
form = PromptForm()
class scholar_view(View):
    def get(self, request):
        form = PromptForm()
        return render(request, 'scholar_prompt/index.html', {'form': form})

    def post(self, request):
        form = PromptForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['scholar_query']
            scholar = Gscholar(query)
            authors = next(scholar)
            return render(request, 'scholar_prompt/scholars.html', {'authors': authors})
        return render(request, 'scholar_prompt/index.html', {'form': form})