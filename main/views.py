from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.forms import UserRegisterForm, HealthCheckForm


@login_required
def home_view(request):
    BMI = 'please submit the form to see your BMI'
    if request.method == 'GET':
        form = HealthCheckForm()
        context = {
            'form': form
        }
        return render(request, 'main/home.html', {'form': form})
    elif request.method == 'POST':
        form = HealthCheckForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            height = height/100
            BMI = str(weight/(height*height))[:5]
            print(BMI)
            if int(form.cleaned_data['alcohol']) > 14:
                alcohol = "You're an alcoholic! Stop drinking!"
            elif int(form.cleaned_data['alcohol']) == 14:
                alcohol = "You drink exactly the right amount, well done!"
            else:
                alcohol = f"You need to drink {14 - int(form.cleaned_data['alcohol'])} to get your recommended number of units per week."
            return render(request, 'main/home.html', {'form': form, 'bmi': BMI, 'alcohol': alcohol})
    elif request.is_ajax():
        pass



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})