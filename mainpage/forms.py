from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # استخدام CustomUser بدلاً من User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="البريد الإلكتروني")
    full_name = forms.CharField(max_length=100, required=True, label="الاسم الكامل")
    mobile_number = forms.CharField(max_length=15, required=True, label="رقم الموبايل")

    class Meta:
        model = CustomUser  # استخدام CustomUser هنا
        fields = ['username', 'full_name', 'email', 'mobile_number', 'password1', 'password2']

    # إضافة تنسيق إضافي لعرض الحقول في النموذج
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "اسم المستخدم"
        self.fields['full_name'].widget.attrs['placeholder'] = "الاسم الكامل"
        self.fields['email'].widget.attrs['placeholder'] = "البريد الإلكتروني"
        self.fields['mobile_number'].widget.attrs['placeholder'] = "رقم الموبايل"
        self.fields['password1'].widget.attrs['placeholder'] = "كلمة المرور"
        self.fields['password2'].widget.attrs['placeholder'] = "تأكيد كلمة المرور"
