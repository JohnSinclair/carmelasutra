# Generated by Django 3.0.6 on 2020-08-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0005_auto_20200609_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseoflife',
            name='image',
            field=models.ImageField(upload_to='uploads/cv/images/2020/8/26/'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='path',
            field=models.CharField(default='uploads/images/2020/8/26/', max_length=40),
        ),
        migrations.AlterField(
            model_name='picture',
            name='upload',
            field=models.ImageField(upload_to='uploads/images/2020/8/26/'),
        ),
    ]
