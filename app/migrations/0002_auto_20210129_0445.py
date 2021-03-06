# Generated by Django 3.1.5 on 2021-01-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Name of the category', max_length=128),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(help_text='Name of the country', max_length=128),
        ),
        migrations.AlterField(
            model_name='title',
            name='categories',
            field=models.ManyToManyField(help_text='The categories of the title', to='app.Category'),
        ),
        migrations.AlterField(
            model_name='title',
            name='countries',
            field=models.ManyToManyField(help_text='Specific countries where this title was released to', to='app.Country'),
        ),
        migrations.AlterField(
            model_name='title',
            name='date_added',
            field=models.DateField(auto_now=True, help_text='Date at which the movie was added to Netflix'),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(help_text='Brief overview about the title', max_length=384),
        ),
        migrations.AlterField(
            model_name='title',
            name='duration',
            field=models.CharField(help_text='The duration till which the title runs', max_length=32),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(help_text='Name of the title', max_length=256),
        ),
        migrations.AlterField(
            model_name='title',
            name='release_year',
            field=models.IntegerField(blank=True, help_text='The year on which this title was released', null=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='type',
            field=models.CharField(choices=[('tv', 'TV Show'), ('movie', 'Movie')], help_text='The type of the title. Can be either a TV Show or a Movie', max_length=10),
        ),
    ]
