# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

from .models import Bb

from .models import Rubric

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)
    # bbs = Bb.objects.order_by('-published')
    # return render(request, 'bboard/index.html', {'bbs': bbs})
    # template = loader.get_template('bboard/index.html')
    # bbs = Bb.objects.order_by('-published')
    # context = {'bbs': bbs}
    # return HttpResponse(template.render(context, request))
    # s = 'Объявления\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')
    # return HttpResponse('Здесь будет выведен список объявлений.')

def rubric_bbs(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/rubric_bbs.html', context)