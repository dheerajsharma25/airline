from sjango.http import Http404, HttpResponse
from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request,"singlepage/index.html")

text = ["W
THE CHALLENGE OF THE FUTURE
HENEVER I INTERVIEW someone for a job, I like to ask this question: “What
important truth do very few people agree with you on?”
This question sounds easy because it’s straightforward. Actually, it’s very hard to
answer. It’s intellectually difficult because the knowledge that everyone is taught in
school is by definition agreed upon. And it’s psychologically difficult because anyone
trying to answer must say something she knows to be unpopular. Brilliant thinking
is rare, but courage is in even shorter supply than genius.
Most commonly, I hear answers like the following:
“Our educational system is broken and urgently needs to be fixed.” "]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(text[num-1])
    else:
        raise Http404("no such directories")