from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question, Choice


# Question에 관한 정보를 나타내주는 페이지
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


# question text를 상세하게 나타내 주는 페이지, 투표할 수 있는 형태로 보여짐
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


'''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
'''


# question에 관한 결과를 나타내주는 페이지
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# 투표하는 기능 구현
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # key value값으로 데이터 받아옴
    except(KeyError, Choice.DoesNotExist):
        # question 투표 폼 다시보여주기
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


''' 
reverse함수는 polls:results(url의 name를 거꾸로 바꿔주는 함수
    # args에는 url에 필요한 변수를 넣어줌
    # 즉 result view로 웹페이지를 띄우라는 소리 
'''
