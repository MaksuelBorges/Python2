from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def feed(request):
    context = {
    'posts': [
        {'author': 'Maksuel', 'date': '01/02/2024', 'content': 'A rapadura é doce mas não é mole não'},
        {'author': 'Pedro', 'date': '06/03/2024', 'content': 'A rapadura é doce mas não é mole não'},
        {'author': 'Maria', 'date': '12/05/2024', 'content': 'A rapadura é doce mas não é mole não'},
    ]
    }
    return render(request, 'feed.html', context)

def publicate(request):
    if request.method == 'POST':
        author = request.POST.get("author")
        content = request.POST.get("content")
        print(author)
        print(content)
        return HttpResponseRedirect('/feed')
    else:
        return render(request, 'publicate.html')
    