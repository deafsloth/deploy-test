# Generated by Django 4.0.5 on 2022-07-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_targetimg_resulttext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resulttext',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='targetimg',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]