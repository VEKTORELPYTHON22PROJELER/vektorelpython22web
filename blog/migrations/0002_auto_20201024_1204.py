# Generated by Django 3.1.2 on 2020-10-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gonderimodel',
            name='tur',
            field=models.CharField(choices=[('1', 'Romantik Komedi'), ('2', 'Drama'), ('3', 'Korku')], default='1', max_length=5, verbose_name='Gönderi Türü'),
        ),
        migrations.AlterField(
            model_name='gonderimodel',
            name='baslik',
            field=models.CharField(max_length=200, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='gonderimodel',
            name='yazi',
            field=models.TextField(verbose_name='Yazı'),
        ),
    ]