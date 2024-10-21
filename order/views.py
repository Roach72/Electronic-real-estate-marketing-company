#views.py
from django.shortcuts import render, redirect
from .forms import ItemForm, ItemImageForm, ItemForm2, ItemImageForm2, ItemForm3, ItemImageForm3
from django.contrib.auth.decorators import login_required  # للتأكد من أن المستخدم مسجل الدخول
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Item, ItemImage, Item2, ItemImage2, Item3, ItemImage3  # استيراد النموذج ItemImage أيضًا

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.added_by = request.user
            item.save()

            # هنا نقوم بتحميل الصور الإضافية
            additional_images = request.FILES.getlist('additional_images')  # تأكد من الحصول على الصور الإضافية
            for img in additional_images:
                item_image = ItemImage(item=item, image=img)  # إنشاء كائن جديد من ItemImage
                item_image.save()  # حفظ الصورة في قاعدة البيانات

            messages.success(request, "تم إضافة العنصر بنجاح!")
            return redirect('item_list')
        else:
            messages.error(request, "هناك خطأ في البيانات المدخلة.")
    else:
        form = ItemForm()
    return render(request, 'order/create_item.html', {'form': form, 'image_form': ItemImageForm()})
@login_required
def item_list(request):
    items = Item.objects.all()  # عرض كل العناصر
    return render(request, 'order/item_list.html', {'items': items})


@login_required
def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # جلب الصور الإضافية الخاصة بالعنصر
    additional_images = item.images.all()
    return render(request, 'order/item_detail.html', {'item': item, 'additional_images': additional_images})





@login_required
def create_item2(request):
    if request.method == 'POST':
        form = ItemForm2(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.added_by = request.user
            item.save()

            # هنا نقوم بتحميل الصور الإضافية الخاصة بـ Item2
            additional_images = request.FILES.getlist('additional_images')
            for img in additional_images:
                item_image = ItemImage2(item=item, image=img)  # يجب استخدام ItemImage2 مع Item2
                item_image.save()

            messages.success(request, "تم إضافة العنصر بنجاح!")
            return redirect('item_list2')  # تأكد من إعادة التوجيه إلى القائمة الصحيحة
        else:
            messages.error(request, "هناك خطأ في البيانات المدخلة.")
    else:
        form = ItemForm2()
    return render(request, 'order2/create2_item.html', {'form': form, 'image_form': ItemImageForm2()})
    
@login_required
def item_list2(request):
    items = Item2.objects.all()  # عرض كل العناصر
    return render(request, 'order2/item2_list.html', {'items': items})


@login_required
def item_detail2(request, item_id):
    item = get_object_or_404(Item2, id=item_id)  # الحصول على Item2 وليس Item
    additional_images = item.images.all()
    return render(request, 'order2/item2_detail.html', {'item': item, 'additional_images': additional_images})







@login_required
def create_item3(request):
    if request.method == 'POST':
        form = ItemForm3(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.added_by = request.user
            item.save()

            # هنا نقوم بتحميل الصور الإضافية الخاصة بـ Item3
            additional_images = request.FILES.getlist('additional_images')
            for img in additional_images:
                item_image = ItemImage3(item=item, image=img)  # يجب استخدام ItemImage3 مع Item3
                item_image.save()

            messages.success(request, "تم إضافة العنصر بنجاح!")
            return redirect('item_list3')  # تأكد من إعادة التوجيه إلى القائمة الصحيحة
        else:
            messages.error(request, "هناك خطأ في البيانات المدخلة.")
    else:
        form = ItemForm3()
    return render(request, 'order3/create3_item.html', {'form': form, 'image_form': ItemImageForm3()})
    
@login_required
def item_list3(request):
    items = Item3.objects.all()  # عرض كل العناصر
    return render(request, 'order3/item3_list.html', {'items': items})


@login_required
def item_detail3(request, item_id):
    item = get_object_or_404(Item3, id=item_id)  # الحصول على Item3 وليس Item
    additional_images = item.images.all()
    return render(request, 'order3/item3_detail.html', {'item': item, 'additional_images': additional_images})




