# Generated by Django 4.1.1 on 2022-09-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssistanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]
