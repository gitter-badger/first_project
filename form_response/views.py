from django.shortcuts import render

# Create your views here.
def index(request):
    if request.POST['registration_status'] == "true":
        return render(request, 'registration_successful.html', {'event_name': request.POST['event_name']})
    else:
        return render(request, 'registration_failed.html', {'event_name': request.POST['event_name'],
                                                            'registration_failure_reason': request.POST['registration_failure_reason']})