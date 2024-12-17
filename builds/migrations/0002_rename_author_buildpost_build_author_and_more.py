# Generated by Django 4.2.17 on 2024-12-17 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('builds', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buildpost',
            old_name='author',
            new_name='build_author',
        ),
        migrations.RenameField(
            model_name='buildpost',
            old_name='description',
            new_name='build_description',
        ),
        migrations.RenameField(
            model_name='buildpost',
            old_name='status',
            new_name='status_build_post',
        ),
        migrations.RemoveField(
            model_name='buildpost',
            name='value',
        ),
        migrations.AddField(
            model_name='buildpost',
            name='money_spent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildpost',
            name='year_build',
            field=models.DateField(default='2015-01-01'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_title', models.CharField(max_length=100, unique=True)),
                ('comment_body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('comment_status', models.IntegerField(choices=[(0, 'Draft'), (1, 'In Progress'), (2, 'Approved')], default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('build_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='builds.buildpost')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
