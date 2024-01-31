from django.shortcuts import render

LOREM_IPSUM = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

# Create your views here.
def home(request):
    posts = [
        {'Autor': 'Maksuel',
         'Data': '31/01/2024',
         'Conteudo': LOREM_IPSUM},
        {'Autor': 'Pedro',
         'Data': '02/02/2024',
         'Conteudo': LOREM_IPSUM},
        {'Autor': 'Henrique',
         'Data': '03/02/2024',
         'Conteudo': LOREM_IPSUM},
        
    ]
    return render(request,'index.html', {'posts': posts})
