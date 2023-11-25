from django.shortcuts import render, redirect, HttpResponse
from .forms import ArticleForm, Moder
from django.contrib import messages
# from parser.parser import parser_vk
from AI.AI_model import exec


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            print("Valid form data:", form.cleaned_data['full_text'])
            cat, theme = exec(form.cleaned_data['full_text'])
            messages.success(request, 'Ваше обращение отправлено!')
            form = ArticleForm()
            return render(request, 'circulation_page/page.html', {
                'form': form,
                'theme': theme,
                'category': cat,
            })
        else:
            error = 'Форма была неверной'
    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'circulation_page/page.html', data)


def sub(request):
    return HttpResponse('!Тестовый вывод!')


def moderator(request):
    items = Moder.objects.all()
    #  здесь вызов функции парсинга и передача ему текста с формы
    return render(request, 'circulation_page/moderator.html', {'items': items})

def submitForm(request):
    print("Test")