# Generated by Django 2.1 on 2018-08-12 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes',
            new_name='lngVotes',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='strChoiceText',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_date',
            new_name='dtmPublishDate',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='strQuestionText',
        ),
    ]
