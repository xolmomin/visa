from django.urls import path, include

from app.views import index, default, application, check, validate, login, check_process, summary


urlpatterns = [
    path('', index, name='index'),
    path('default/', default, name='default'),
    path('application/', application, name='application'),
    path('application/check/', check, name='check'),
    path('check_process', check_process, name='check_process'),
    path('validate', validate, name='validate'),
    path('login', login, name='login'),
    path('summary', summary, name='summary'),
]
