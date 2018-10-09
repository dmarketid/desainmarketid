from django.shortcuts import render

def index(request):
	context = {
		'tab_title': 'Illustrator . desainmarket',
		'h1_title': 'illustrator',
	}
	return render(request, 'illustrator/index.html', context)
