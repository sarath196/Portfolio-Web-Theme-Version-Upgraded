# Generated by Django 2.0 on 2019-03-12 20:51

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20190312_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='project',
            field=wagtail.fields.StreamField((('project', wagtail.blocks.StructBlock((('name', wagtail.blocks.CharBlock(classname='full title')), ('menu_title', wagtail.blocks.CharBlock(classname='full title')), ('project_url', wagtail.blocks.CharBlock(classname='full title'))))),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfoliopage',
            name='project_title',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
