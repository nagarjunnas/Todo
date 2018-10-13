# Generated by Django 2.1.2 on 2018-10-13 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('in_progress', 'Progress'), ('completed', 'Completed'), ('pending', 'Pending')], default='in_progress', max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
