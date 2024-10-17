from django.shortcuts import render


from django.http import HttpResponse
 
 
def index(request):
    headers = request.META
    remote_user = request.META.get('USERNAME', 'Заголовок не передан')
    return HttpResponse(f"USERNAME: {remote_user}<br>Все заголовки: {headers}")
