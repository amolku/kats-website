""" Interviews views """

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Interview

# Create your views here.

def post_list(request):
    interviews = Interview.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'interviews/post_list.html', {'interviews':interviews})

def interview_detail(request, pk):
    interview = get_object_or_404(Interview, pk=pk)
    return render(request, 'interviews/post_detail.html', {'interview': interview})