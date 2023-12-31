# Generated by Django 4.2.6 on 2023-10-19 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_employeeprofile_user'),
        ('bugtrackerapp', '0004_remove_project_image_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='accounts.employeeprofile'),
        ),
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together={('author',)},
        ),
    ]
