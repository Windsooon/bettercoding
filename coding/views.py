import random
from django.shortcuts import render
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from problems.models import Problem


def get_order(language):
    return 0 if language == 'English' else 1


def index(request):
    '''Front page'''
    title = ['Coding is more than algorithms.', '编程不单单算法']
    subtitle = [
        'Ready to test your Coding Skills?',
        '准备开始测试编程能力了吗？'
    ]
    order = get_order(language)
    context = {
        'title': title[order],
        'subtitle': subtitle[order],
    }
    return render(request, 'start.html', context)


def language(request, language):
    title = ['Choose your favourite topic', '选择你喜欢的主题']
    order = get_order(language)
    categories = ['Python', 'HTML', 'CSS', 'Java', 'C++']
    context = {
        'title': title[order],
        'categories': categories
    }
    return render(request, 'second.html', context)


def cate(request, language, cate):
    '''
    Tell user what should do before start test
    '''
    title = ["Warning", '警告']
    subtitle = [
        "Something you should know before the test",
        '在开始之前你必须了解这些事情'
    ]
    rules = [
        ['Don\'t fool yourself', 'Think carefully', 'The test is hard'],
        ['不要尝试去欺骗自己', '在确定答案之前认真思考', '这里的题目本来就偏难']
    ]
    start = ['Let\'s Begin', '点击开始']
    order = get_order(language)
    context = {
        'title': title[order], 'subtitle': subtitle[order],
        'rules': rules[order], 'start': start[order]
    }
    return render(request, 'info.html', context)


def cate_pro(request, language, cate, id):
    resource_kw = ['References', '参考']
    problem = Problem.objects.filter(
        problem_id=id, category__language=cate.lower())
    if problem:
        problem = problem.first()
        # convert code to html
        code_in_html = highlight(
            problem.code,
            get_lexer_by_name(problem.category.language),
            HtmlFormatter())
        answer_lst = [
            (1, problem.true_answer), (0, problem.wrong_answer1),
            (0, problem.wrong_answer2), (0, problem.wrong_answer3)]
        random.shuffle(answer_lst)
        context = {
            'problem': problem,
            'code_in_html': code_in_html,
            'answer_lst': answer_lst,
            'resource_kw': resource_kw[get_order(language)]
        }
        return render(request, 'problem.html', context)
    return render(request, '404.html')
