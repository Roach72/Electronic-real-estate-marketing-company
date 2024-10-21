# Generated by Django 5.1.1 on 2024-10-04 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="name",
            new_name="name_item",
        ),
        migrations.RemoveField(
            model_name="item",
            name="field1",
        ),
        migrations.RemoveField(
            model_name="item",
            name="field2",
        ),
        migrations.RemoveField(
            model_name="item",
            name="field3",
        ),
        migrations.RemoveField(
            model_name="item",
            name="field4",
        ),
        migrations.RemoveField(
            model_name="item",
            name="field5",
        ),
        migrations.RemoveField(
            model_name="item",
            name="size",
        ),
        migrations.AddField(
            model_name="item",
            name="Plakona",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="item",
            name="added_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="added_by_name",
            field=models.CharField(editable=False, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="area_in_meters",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="item",
            name="bathroom",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="item",
            name="hall",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="item",
            name="kitchen",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="item",
            name="room",
            field=models.IntegerField(default=0),
        ),
    ]
