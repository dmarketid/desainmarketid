from django.shortcuts import render

def index(request):
	context = {
		'tab_title':'Motion graphics . desainmarket',
		'h1_title':'motion graphics',
	} 
	return render(request,'motiongraphics/index.html', context)