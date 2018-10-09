from django.shortcuts import render

def index(request):
	context = {
		'tab_browser_title': 'desainmarket',
		'header_title': 'desainmarket',
	}
	return render(request, 'index.html', context)