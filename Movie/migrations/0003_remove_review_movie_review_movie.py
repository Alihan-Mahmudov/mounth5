# Generated by Django 4.1.5 on 2023-03-10 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0002_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='Movie',
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.movie'),
        ),
    ]
