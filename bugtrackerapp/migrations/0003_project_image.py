# Generated by Django 4.2.6 on 2023-10-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtrackerapp', '0002_alter_project_submission_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ticketimgs/'),
        ),
    ]
