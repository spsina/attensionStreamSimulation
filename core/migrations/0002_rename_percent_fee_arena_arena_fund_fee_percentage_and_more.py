# Generated by Django 4.0.1 on 2022-01-29 07:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arena',
            old_name='percent_fee',
            new_name='arena_fund_fee_percentage',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='label',
        ),
        migrations.RemoveField(
            model_name='arena',
            name='token',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='conflicts_with',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='target_amount',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='choice_min_support_duration',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='topic_duration_in_cycles',
        ),
        migrations.AddField(
            model_name='arena',
            name='choice_creation_fee',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arena',
            name='token_contract_address',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arena',
            name='topic_creation_fee',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='max_target_amount',
            field=models.FloatField(default=10000000000),
        ),
        migrations.AddField(
            model_name='topic',
            name='create_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 29, 7, 58, 47, 776871, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='transfer_period',
            field=models.DurationField(default=datetime.timedelta(0)),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Token',
        ),
    ]
