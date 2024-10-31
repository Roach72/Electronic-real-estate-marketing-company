#models.py
from django.conf import settings
from django.db import models

class Item(models.Model):
    name_item = models.CharField(max_length=255) 
    description = models.TextField()        
    image = models.ImageField(upload_to='images/')  
    video = models.FileField(upload_to='videos/', null=True, blank=True)  # حقل لتحميل الفيديو
    area_in_meters = models.DecimalField(max_digits=10, decimal_places=2 )  
    room = models.IntegerField()  # إضافة قيمة افتراضية 0
    kitchen = models.IntegerField()  # إضافة قيمة افتراضية 0
    bathroom = models.IntegerField()  # إضافة قيمة افتراضية 0
    hall = models.IntegerField()  # إضافة قيمة افتراضية 0
    Plakona = models.IntegerField()  # إضافة قيمة افتراضية 0
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    added_by_name = models.CharField(max_length=150, editable=False, null=True)

    def save(self, *args, **kwargs):
        if self.added_by:
            self.added_by_name = self.added_by.full_name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_item


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'Image for {self.item.name_item}'





class Item2(models.Model):
    name_item = models.CharField(max_length=255) 
    description = models.TextField()        
    image = models.ImageField(upload_to='images/')  
    video = models.FileField(upload_to='videos/', null=True, blank=True)  # حقل لتحميل الفيديو
    area_in_meters = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  

    room = models.IntegerField(default=0)  # إضافة قيمة افتراضية 0
    kitchen = models.IntegerField(default=0)  # إضافة قيمة افتراضية 0
    bathroom = models.IntegerField(default=0)  # إضافة قيمة افتراضية 0
    hall = models.IntegerField(default=0)  # إضافة قيمة افتراضية 0
    Plakona = models.IntegerField(default=0)  # إضافة قيمة افتراضية 0
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    added_by_name = models.CharField(max_length=150, editable=False, null=True)

    def save(self, *args, **kwargs):
        if self.added_by:
            self.added_by_name = self.added_by.get_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_item


class ItemImage2(models.Model):
    item = models.ForeignKey(Item2, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images2/')
    def __str__(self):
        return f'Image for {self.item.name_item}'


class Item3(models.Model):
    name_item = models.CharField(max_length=255) 
    description = models.TextField()        
    image = models.ImageField(upload_to='images/')  
    video = models.FileField(upload_to='videos/', null=True, blank=True)  # حقل لتحميل الفيديو
    area_in_meters = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  

    room = models.IntegerField(default=0)  # إضافة قيمة افتراضية 0
    kitchen = models.IntegerField(default=0)  # إضافة قيمة افتراضية 0
    bathroom = models.IntegerField(default=0)  # إضافة قيمة افتراضية 0
    hall = models.IntegerField(default=0)  # إضافة قيمة افتراضية 0
    Plakona = models.IntegerField(default=0)  # إضافة قيمة افتراضية 0
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    added_by_name = models.CharField(max_length=150, editable=False, null=True)

    def save(self, *args, **kwargs):
        if self.added_by:
            self.added_by_name = self.added_by.get_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_item


class ItemImage3(models.Model):
    item = models.ForeignKey(Item3, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images3/')
    def __str__(self):
        return f'Image for {self.item.name_item}'


