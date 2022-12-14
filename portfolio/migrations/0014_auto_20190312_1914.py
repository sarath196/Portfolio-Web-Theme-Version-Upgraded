# Generated by Django 2.0 on 2019-03-12 19:14

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_portfoliopage_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='education_title',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='portfoliopage',
            name='education',
            field=wagtail.fields.StreamField((('education', wagtail.blocks.StructBlock((('university', wagtail.blocks.CharBlock(classname='full title')), ('year_passing', wagtail.blocks.CharBlock(classname='full title')), ('education_content', wagtail.blocks.CharBlock(classname='full title'))))),), blank=True, null=True),
        ),
    ]
