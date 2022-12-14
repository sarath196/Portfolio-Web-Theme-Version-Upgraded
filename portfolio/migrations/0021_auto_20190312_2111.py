# Generated by Django 2.0 on 2019-03-12 21:11

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_auto_20190312_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopage',
            name='project',
            field=wagtail.fields.StreamField((('project', wagtail.blocks.StructBlock((('name', wagtail.blocks.CharBlock(classname='full title')), ('description', wagtail.blocks.RichTextBlock()), ('menu_title', wagtail.blocks.CharBlock(classname='full title')), ('project_url', wagtail.blocks.URLBlock(classname='full title')), ('project_image', wagtail.images.blocks.ImageChooserBlock()), ('language', wagtail.blocks.StreamBlock((('skills', wagtail.blocks.CharBlock()),), icon='user'))))),), blank=True, null=True),
        ),
    ]
