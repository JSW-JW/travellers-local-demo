# Generated by Django 3.1.8 on 2021-05-11 07:54

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('diary', '0003_auto_20210510_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
