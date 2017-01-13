from django.http import HttpResponseRedirect#, HttpResponse
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic

#from django.template import loader

# #testing
# from numpy import exp, cos, linspace
# import matplotlib.pyplot as plt  
# import os,time,glob
# #end of testing

from .models import Choice, Question

# def dampled_vibrations(t,A,b,w):
# 	return A*exp(-b*t)*cos(w*t)

# def compute(A,b,w,T, resolution=500):
# 	print os.getcwd()
# 	t = linspace(0,T,resolution+1)
# 	y = dampled_vibrations(t,A,b,w)
# 	plt.figure()
# 	plt.plot(t,y)
# 	#plt.show()
# 	plt.title('A=%g,b=%g,w=%g' % (A,b,w))
# 	return "compute finished"

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		#print compute(1,0.1,1,20)
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


# def index(request):
# 	#return HttpResponse("Hello, World!")
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	#template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list':latest_question_list,
# 	}
# 	#return HttpResponse(template.render(context,request))
# 	return render(request,'polls/index.html', context)

# def detail(request,question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/detail.html', {'question':question})

# def results(request,question_id):
# 	#pass
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question':question})
#     #return

def vote(request,question_id):
	#pass

	#compute(1,0.1,1,20)

	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', 
			{'question': question,'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))