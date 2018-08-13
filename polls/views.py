'''
@author Ryan Kilbride
@since 2018-08-12
'''

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404,render
from django.template import loader
from .models import Question


#static page example
# def index(request):
#     arrLatestQuestions = Question.objects.order_by('-dtmPublishDate')[:5]
#     output = ', '.join([q.strQuestionText for q in arrLatestQuestions])
#     return HttpResponse(output)

def index(request):
    arrLatestQuestions = Question.objects.order_by('-dtmPublishDate')[:5]
    objTemplate = loader.get_template('polls/index.html')
    context = {
        'arrLatestQuestions': arrLatestQuestions,
    }
    return HttpResponse(objTemplate.render(context,request))

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(id=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Poll does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

