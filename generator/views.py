from django.shortcuts import render

import random

CHARS = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '1234567890'
SPECIAL_CHARS = '~@#$%^&*()_-+='

def index(request):
    """View-функция для главной страницы."""
    nums = [idx for idx in range(5, 15)]
    context = {'nums': nums}
    return render(request, 'index.html', context)

def generate_password(request):
    """View-функция для вывода сгенерированного пароля."""
    nums = [idx for idx in range(5, 15)]
    char_pool = []
    password = ''
    alphabet = list(CHARS)

    if request.GET.get('uppercase'):
        char_pool.append(random.choice(CHARS.upper()))
        alphabet.extend(CHARS.upper())

    if request.GET.get('special_chars'):
        char_pool.append(random.choice(SPECIAL_CHARS))
        alphabet.extend(SPECIAL_CHARS)

    if request.GET.get('numbers'):
        char_pool.append(random.choice(NUMBERS))
        alphabet.extend(NUMBERS)

    length = int(request.GET.get('length', 12))

    while len(char_pool) < length:
        char_pool.append(random.choice(alphabet))

    random.shuffle(char_pool)

    password = ''.join(char_pool)

    context = {'password': password, 'nums': nums}
    return render(request, 'index.html', context)
