# Generated by Django 3.2.5 on 2021-07-31 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auther', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='children', to='auther.user'),
        ),
    ]
