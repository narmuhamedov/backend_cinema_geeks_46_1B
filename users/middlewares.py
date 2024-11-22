from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class AgeClubMiddleware(MiddlewareMixin):
    def proccess_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            age = int(request.POST.get('age'))
            if age < 5:
                return HttpResponseBadRequest('Ваш возраст слишком мал приходите на следующий год')
            elif age >= 5 and age <= 10:
                request.club = "Детский клуб"
            elif age >= 11 and age <= 18:
                request.club = 'Подростковый клуб'
            elif age >= 19 and age <= 45:
                request.club = 'Взрослый клуб'
            else:
                return HttpResponseBadRequest('Ваш возраст состовляет больше 45 извините вы не подходите')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'Клуб не определен проверьте данные еще раз!')
