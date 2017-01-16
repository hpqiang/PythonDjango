from django.http import HttpResponseRedirect#, HttpResponse
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# Create your views here.

# class IndexView(generic.ListView):
# 	template_name = 'polls/index.html'
# 	context_object_name = 'latest_question_list'

# 	def get_queryset(self):
# 		"""Return the last five published questions."""
# 		#print compute(1,0.1,1,20)
# 		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def index(request):
	#return HttpResponse("Hello, World!")
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	sidebar_items = [
			{'name': 'polls1', 'site':'/polls/'},
			{'name': 'Sci Calc1', 'site':'/my_sci/'},
		]
	# sidebar_items = tuple(sidebar_items)
	names = [d['name'] for d in sidebar_items]
	sites = [s['site'] for s in sidebar_items]
	# print("Calling index")
	# print names
	# print sites
	site_items = zip(names, sites)
	# print site_items
	#template = loader.get_template('polls/index.html')

	context = {
		'latest_question_list':latest_question_list,
		'site_items':site_items,
	}
	#return HttpResponse(template.render(context,request))
	return render(request,'polls/index.html', context)

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