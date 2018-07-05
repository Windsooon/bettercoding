from django.shortcuts import render


def index(request):
    '''Front page'''
    return render(request, 'start.html')


def english(request):
    categories = ['Python', 'HTML', 'CSS', 'Java', 'C++']
    context = {'categories': categories}
    return render(request, 'second.html', context)


def chinese(request):
    categories = ['Python', 'HTML', 'CSS', 'Java', 'C++']
    context = {'categories': categories}
    return render(request, 'second.html', context)

def english_cate(request, cate):
    pass


def chinese_cate(request, cate):
    pass
