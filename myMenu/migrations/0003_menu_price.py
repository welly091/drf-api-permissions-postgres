# Generated by Django 4.1 on 2022-08-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myMenu", "0002_remove_menu_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="price",
            field=models.IntegerField(blank=True, default=13),
            preserve_default=False,
        ),
    ]
