# Generated by Django 4.2.6 on 2023-11-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_employeeprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.png', upload_to='avatars/'),
        ),
    ]
