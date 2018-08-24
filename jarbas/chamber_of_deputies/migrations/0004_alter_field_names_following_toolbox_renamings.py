from django.contrib.postgres.fields import ArrayField
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamber_of_deputies', '0003_remove_available_in_latest_dataset_field'),
    ]

    operations = [
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
