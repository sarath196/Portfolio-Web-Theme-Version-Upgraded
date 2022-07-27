# Generated by Django 2.0 on 2019-03-17 19:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.routable_page.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('portfolio', '0030_auto_20190315_0830'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('git_title', models.CharField(blank=True, max_length=150)),
                ('date', models.DateTimeField(default=datetime.datetime.today, verbose_name='Project date')),
                ('GIT', wagtail.fields.StreamField((('GIT', wagtail.blocks.StructBlock((('name', wagtail.blocks.CharBlock(classname='full title')), ('description', wagtail.blocks.RichTextBlock()), ('excerpt', wagtail.blocks.RichTextBlock(blank=True)), ('menu_title', wagtail.blocks.CharBlock(classname='full title')), ('git_url', wagtail.blocks.URLBlock(classname='full title')), ('git_image', wagtail.images.blocks.ImageChooserBlock()), ('image_text', wagtail.blocks.CharBlock(classname='full title')), ('start_date', wagtail.blocks.CharBlock(classname='full title')), ('end_date', wagtail.blocks.CharBlock(classname='full title')), ('language', wagtail.blocks.StreamBlock((('skills', wagtail.blocks.CharBlock()),), icon='user'))))),), blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GitParentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='URLPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('git_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('bitbucket_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='git_url',
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='linkedin_url',
        ),
    ]