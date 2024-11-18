from django.shortcuts import render, redirect
from .models import Buyer, Game
from .forms import UserRegister


# Create your views here.
def home(request):
    return render(request, 'home.html', {'pagename': 'Главная страница'})


def shop(request):
    game = Game.objects.all()
    context = {
        'game': game
    }

    return render(request, 'shop.html', context)


def basket(request):
    return render(request, 'basket.html', {'pagename': 'Корзина'})





def sign_up_by_html(request):
    return sign_up_by_django(request)

def game_list_view(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'shop.html', context)


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        username = request.POST.get('username')

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                if not Buyer.objects.filter(name=username).exists():
                    Buyer.objects.create(name=username)
                else:
                    info['error'] = 'Пользователь уже существует'
                    return render(request, 'registration_page.html', {'info': info})

                return render(request, 'fifth_task/registration_page.html', {'info': {}, 'message': f'Приветствуем, {username}!'})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', {'info': info})
