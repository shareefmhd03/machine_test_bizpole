import requests
from datetime import date

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import login as auth_login
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import UserRegistrationForm,ActivityForm
from .utils import send_email,CustomAuthBackend
from .models import Activity



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            auth_login(request,user)
            activity_type = user.selected_activity

            data_list = []
            for i in range(0,10):
                url = f'https://www.boredapi.com/api/activity?type={activity_type}&participants=1'
                
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    data_list.append(data)
            for activity_data in data_list:
                activity = Activity.objects.create(
                    user=user,
                    activity_name=activity_data['activity'],
        )
            mail_subject = 'WELCOME!'
            message = render_to_string('welcome_email.html', {
                'user': user,
            })
            send_email(mail_subject,message,user.email)


            return redirect('activities')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = CustomAuthBackend.authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('activities')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')



@login_required
def activity_listing(request):
    user = request.user
    activities = Activity.objects.filter(user=user).order_by('id')

    paginator = Paginator(activities, 3)
    page = request.GET.get('page')

    try:
        activities_page = paginator.page(page)
    except PageNotAnInteger:
        activities_page = paginator.page(1)
    except EmptyPage:
        activities_page = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'activities': activities_page})


from .models import Activity

def fetch_more_activities(request):
    user = request.user
    today = date.today()
    activities_fetched_today = Activity.objects.filter(user=user, created_at__date=today).count()
    activity_type = user.selected_activity
    if activities_fetched_today >= 2:
        messages.warning(request, "You have reached the daily limit for fetching activities.")
    else:
        url = f'https://www.boredapi.com/api/activity?type={activity_type}&participants=1'
                
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        activity = Activity.objects.create(
                    user=user,
                activity_name=data['activity'],
        )


        messages.success(request, "Additional activities fetched successfully.")

    return redirect('activities')


def edit_activity(request, activity_id):
    activity = Activity.objects.get(Q(user = request.user) & Q(id = activity_id))
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activities')
    else:
        form = ActivityForm(instance=activity)

    return render(request, 'update.html', {'form': form})

