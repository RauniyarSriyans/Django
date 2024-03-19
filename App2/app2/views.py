from django.shortcuts import render, get_object_or_404
from .models import JobPosting

# Create your views here.
def homePage(request):
    active_jobs = JobPosting.objects.filter(is_active=True)
    context = {
        'job_postings': active_jobs
    }
    return render(request, 'app2/index.html', context)

def JobDetail(request, pk):
    # get object or 404 gives a 404 error whenever the object can't be retrieved
    job_posting = get_object_or_404(JobPosting, pk=pk, is_active=True)
    context = {
        'posting': job_posting
    }
    return render(request, 'app2/detail.html', context)
