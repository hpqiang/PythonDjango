from django.shortcuts import render #render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from models import InputForm
from compute import compute
import os

# Create your views here.

def index(request):
	#return HttpResponse("Hello, My Sci Py")
	os.chdir(os.path.dirname(__file__))
	result = None
	print(request)
	if request.method == 'POST':
		#print("is posting")
		form = InputForm(request.POST)
		#print("form from InputFrom")
		if form.is_valid():
			#print("form valid")
			form2 = form.save(commit=False)
			#print("form2 OK")
			result = compute(form2.A,form2.b,form2.w, form2.T)
			#print("result 1: {}".format(result))
			result = result.replace('static\\','') #should use '\\', not '/' as the tutorial said
			#print(result)

		else:
			print("invalid form")
	else:
		#print("is showing input form")
		form = InputForm()

	# refer to: http://stackoverflow.com/questions/38739422/django-error-render-to-response-got-an-unexpected-keyword-argument-context-i
	# return render_to_response('my_sci/result.html',
	# 		{
	# 			'form':form,
	# 			'result':result
	# 		}, context_instance=RequestContext(request)
	# 	)

	sidebar_items = [
			{'name': 'fft', 'site':'/my_sci/'},
			{'name': 'fluid', 'site':'/my_sci/'},
		]
	names = [d['name'] for d in sidebar_items]
	sites = [s['site'] for s in sidebar_items]
	site_items = zip(names, sites)


	return render(request, 'my_sci/result.html',
			{
				'form':form,
				'result':result,
				'site_items':site_items,
			}
		)