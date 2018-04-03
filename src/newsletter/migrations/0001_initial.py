# Generated by Django 2.0.3 on 2018-04-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(blank=True, default='', max_length=254, unique=True)),
            ],
        ),
    ]
