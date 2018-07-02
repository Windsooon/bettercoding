from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.db.models import Case, When, Count
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required


def index(request):
    '''Front page'''
    return render(request, 'start.html')
