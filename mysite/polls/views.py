from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        'question': question
    })

def vote(request, question_id):
    question = get_object_or_404(Question, pl=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html' , {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Dica: sempre retornar um HttpResponseRedirect 
        # após sucesso com data POST.
        # Isso evita o envio do dado novamente
        # caso o usuário clique no botão de voltar
        return HttpResponseRedirect(reverse('pols:results', args=(question.id,)))