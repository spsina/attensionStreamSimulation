# Generated by Django 4.0.1 on 2022-01-29 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_percent_fee_arena_arena_fund_fee_percentage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='max_target_amount',
        ),
        migrations.AddField(
            model_name='choice',
            name='target_amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='max_target_amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
