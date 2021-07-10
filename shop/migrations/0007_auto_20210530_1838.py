# Generated by Django 3.2 on 2021-05-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210530_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='closingTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='openingTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='longDescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='oneLine',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shortDescription',
            field=models.TextField(blank=True, null=True),
        ),
    ]