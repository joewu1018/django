from django.shortcuts import render
from flower.models import Flower
from django.shortcuts import render, get_object_or_404
# Create your views here.


def flowers(request):
    q = request.GET.get('q', None)
    flowers = ''
    if q is None or q is "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)
    return render(request, 'flower.html', {'flowers': flowers })

def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'detail.html', locals())