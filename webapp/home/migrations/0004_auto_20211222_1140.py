# Generated by Django 3.2.10 on 2021-12-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_menu_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dish_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
