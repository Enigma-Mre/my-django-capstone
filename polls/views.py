
from django.urls import reverse
from .models import Questions, Choice
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):

    # Get the latest 5 questions ordered by publication date.
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]

    # Create a context dictionary with the latest question list.
    context = {'latest_question_list': latest_question_list}

    # Render the 'polls/poll.html' template with the context.
    return render(request, "polls/poll.html", context)


def detail(request, question_id):

    # Get the question object with the specified ID or return a 404 error if not found.
    question = get_object_or_404(Questions, pk=question_id)

    # Render the 'polls/detail.html' template with the question object.
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):

    # Get the question object with the specified ID or return a 404 error if not found.
    question = get_object_or_404(Questions, pk=question_id)

    # Render the 'polls/results.html' template with the question object.
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):

    # Get the question object with the specified ID or return a 404 error if not found.
    question = get_object_or_404(Questions, pk=question_id)
    try:
        # Get the selected choice object from the request's POST data.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        # If the choice was not selected, return an error message.
        return render(request, 'polls/poll.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })

    else:
        # Increment the votes count for the selected choice and save the changes.
        selected_choice.votes += 1
        selected_choice.save()

        # Redirect to the results page for the specified question.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    
    
def landing_page(request):
    return render(request, 'landing_page.html')