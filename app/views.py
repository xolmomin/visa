import random
import string

from captcha.image import ImageCaptcha
from django.shortcuts import render, redirect

from app.forms import CheckLogin, CheckForm, EnterInformationForm
from app.models import Winner


def index(request):
    return render(request, 'app/index.html')


def default(request):
    return render(request, 'app/default.html')


def application(request):
    return render(request, 'app/application.html')


def validate(request):
    return render(request, 'app/validate.html')


def login(request):
    if request.method == 'POST':
        check_login = CheckLogin(request.POST)
        if check_login.is_valid():
            image = ImageCaptcha()
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            image.generate(code)
            image.write(code, 'app/static/login_captcha.png')

            context = {'captcha': code, 'case_number': check_login.clean_case_number()}
            return render(request, 'app/login_2.html', context)
        return render(request, 'app/login.html', {'check_form': check_login})
    else:
        return render(request, 'app/login.html')


def check(request):
    image = ImageCaptcha()
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    image.generate(code)
    image.write(code, 'app/static/code.png')

    # audiofile = AudioCaptcha()
    # data = audiofile.generate(code)
    # audiofile.write(code, './static/hello.png')
    enter_form = EnterInformationForm()

    if request.method == 'POST':
        enter_form = EnterInformationForm(request.POST)

        if enter_form.is_valid():
            confirm = enter_form.cleaned_data['confirm']

            winner = Winner.objects.filter(confirm_number__exact=confirm).first()
            if winner is not None:
                return render(request, 'app/won.html')
            else:
                return render(request, 'app/failed.html')

        return render(request, 'app/check.html', {'code': code, 'enter_form': enter_form})
    else:
        return render(request, 'app/check.html', {'code': code, 'enter_form': enter_form})


def check_process(request):
    image = ImageCaptcha()
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    image.generate(code)
    image.write(code, 'app/static/login_captcha.png')


def summary(request):
    check_form = CheckForm()
    if request.method == 'POST':
        check_form = CheckForm(request.POST)
        case_number = request.POST['case_number']
        # org_captcha

        if check_form.is_valid():
            winner = Winner.objects.get(case_number=case_number)
            context = {'winner': winner}
            return render(request, 'app/summary.html', context)
        else:
            image = ImageCaptcha()
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            image.generate(code)
            image.write(code, 'app/static/login_captcha.png')
            return render(request, 'app/login_2.html', {'check_form': check_form})
    else:
        return redirect('login')
