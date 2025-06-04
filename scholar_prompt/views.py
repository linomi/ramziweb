from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .forms import PromptForm
from .scholar import Gscholar
from django.views import View
from pypdf import PdfReader

# Create your views here.
form = PromptForm()

def process_cv(cv_file):
    """Helper function to process CV file and extract text"""
    pdf_reader = PdfReader(cv_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

class scholar_view(View):
    def get(self, request):
        if 'cv' in request.session:
            return render(request, 'scholar_prompt/index.html', {
                'form': form,
                'cv': request.session['cv']
            })
        return render(request, 'scholar_prompt/index.html', {
            'form': form,
            'cv': False
        })

    def post(self, request):
        form = PromptForm(request.POST, request.FILES)
        if form.is_valid():
            query = form.cleaned_data['scholar_query']
            cv_file = form.cleaned_data.get('CV')

            # Get authors from Google Scholar
            scholar = Gscholar(query)
            authors = scholar.get()

            # Store query and authors in session
            request.session['query'] = query
            request.session['authors'] = authors

            # Process CV if provided
            if cv_file:
                cv_text = process_cv(cv_file)
                request.session['cv'] = cv_text
                request.session['cv_name'] = cv_file.name
                return render(request, 'scholar_prompt/scholars.html', {
                    'authors': authors,
                    'cv': True,
                    'cv_name': cv_file.name,
                    'query': query
                })

            # If CV exists in session, use that
            elif 'cv' in request.session:
                return render(request, 'scholar_prompt/scholars.html', {
                    'authors': authors,
                    'cv': True,
                    'cv_name': request.session.get('cv_name'),
                    'query': query
                })

            # No CV provided or in session
            return render(request, 'scholar_prompt/scholars.html', {
                'authors': authors,
                'cv': False,
                'query': query
            })

        return render(request, 'scholar_prompt/index.html', {'form': form})

def change_cv(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Invalid request method")

    if 'CV' not in request.FILES:
        return HttpResponseBadRequest("No file uploaded")

    cv_file = request.FILES['CV']
    if not cv_file.name.lower().endswith('.pdf'):
        return HttpResponseBadRequest("Only PDF files are allowed")

    # Process the new CV
    cv_text = process_cv(cv_file)
    request.session['cv'] = cv_text
    request.session['cv_name'] = cv_file.name

    # Redirect back to search results if query exists
    if 'query' in request.session and 'authors' in request.session:
        return render(request, 'scholar_prompt/scholars.html', {
            'authors': request.session['authors'],
            'cv': True,
            'cv_name': cv_file.name,
            'query': request.session['query']
        })

    # Otherwise redirect to index
    return redirect('scholar_prompt:index')

def get_author(authors:list,author_id:str): 
    for author in authors: 
        if author['scholar_id'] ==author_id: 
            return author

class AuthorView(View): 
    def get(self,request,slug): 
        author = get_author(request.session.get('authors'),slug)

        S = Gscholar(request.session.get('query'))
        S.set_author(author=author)
        publications = S.get_publications(10)

        return render(request,'scholar_prompt/scholar.html',{'publications':publications})