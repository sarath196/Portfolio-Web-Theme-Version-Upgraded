# Generated by Django 2.0 on 2019-02-25 17:22

from django.db import migrations, models
import django.db.models.deletion
import wagtailmd.utils


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
        ('portfolio', '0002_auto_20190224_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', wagtailmd.utils.MarkdownField(blank=True, verbose_name='Profile Name')),
                ('designation', wagtailmd.utils.MarkdownField(blank=True, verbose_name='Destination')),
                ('age', models.IntegerField(blank=True, verbose_name='Year of Birth')),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('location', wagtailmd.utils.MarkdownField(blank=True, verbose_name='Location')),
                ('profile_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
