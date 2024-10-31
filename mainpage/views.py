from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm



def mainpage(request):
    return render(request, 'pages/mainpage.html')



def custom_login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', 'mainpage')  # توجيه المستخدم إلى الصفحة المقصودة
            return redirect(next_url)  
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة.")  # رسالة الخطأ
            return render(request, 'auth/login.html', {'next': request.POST.get('next')})
    return render(request, 'auth/login.html', {'next': request.GET.get('next')})




def custom_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainpage')) 
    

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.full_name = form.cleaned_data.get('full_name')
            user.mobile_number = form.cleaned_data.get('mobile_number')
            user.save()
            messages.success(request, 'تم إنشاء الحساب بنجاح! يمكنك تسجيل الدخول الآن.')
            return redirect('login')  # تأكد من استخدام اسم المسار الصحيح لصفحة تسجيل الدخول
    else:
        form = UserRegistrationForm()
    
    return render(request, 'auth/register.html', {'form': form})

def choice(request):
    return render(request, 'choice.html')



def explore(request):
    return render(request, 'explore.html')

