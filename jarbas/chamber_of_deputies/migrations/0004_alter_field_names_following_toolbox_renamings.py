# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields import ArrayField
from django.db import migrations, models


# net_values = models.CharField('Valores Líquidos dos Ressarcimentos', max_length=140)
# numbers
# reimbursement_numbers = models.CharField('Números dos Ressarcimentos', max_length=140)
# reimbursement_values = models.CharField('Valores dos Ressarcimentos', max_length=140, blank=True, null=True)
# subquota_id = models.IntegerField('Número da Subcota', db_index=True)
# subquota_number
# total_reimbursement_value = models.DecimalField('Valor da Restituição', max_digits=10, decimal_places=3, blank=True, null=True)
# total_value


class Migration(migrations.Migration):

    dependencies = [
        ('chamber_of_deputies', '0003_remove_available_in_latest_dataset_field'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='reimbursement',
        #     name='available_in_latest_dataset',
        # ),
        # migration.RenameField(
        #     model_name='reimbursement',
        #     old_name='',
        #     new_name='',
        # ),
        # migrations.AddField(
        #     model_name='reimbursement',
        #     name='numbers',
        #     field=ArrayField(models.CharField(), default=list),
        # ),
        migrations.AlterField(
            model_name='reimbursement',
            name='reimbursement_numbers',
            field=ArrayField(models.CharField(max_length=128), default=list),
        ),
        migrations.RenameField(
            model_name='reimbursement',
            old_name='reimbursement_numbers',
            new_name='numbers',
        ),
        migrations.RenameField(
            model_name='reimbursement',
            old_name='total_reimbursement_value',
            new_name='total_value',
        ),
        migrations.RemoveField(
            model_name='reimbursement',
            name='net_values',
        ),
    ]
