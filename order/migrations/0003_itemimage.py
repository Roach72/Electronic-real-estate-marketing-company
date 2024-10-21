# Generated by Django 5.1.1 on 2024-10-16 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0002_rename_name_item_name_item_remove_item_field1_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="images/")),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="order.item",
                    ),
                ),
            ],
        ),
    ]
