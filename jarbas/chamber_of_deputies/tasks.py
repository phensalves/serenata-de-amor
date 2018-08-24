from itertools import chain

from rows.fields import FloatField

from jarbas.chamber_of_deputies.fields import ArrayField, DateAsStringField, IntegerField
from jarbas.chamber_of_deputies.models import Reimbursement


INTEGERS = (
    'applicant_id',
    'batch_number',
    'congressperson_document',
    'congressperson_id',
    'document_id',
    'document_type',
    'installment',
    'month',
    'subquota_group_id',
    'subquota_number',
    'term',
    'term_id',
    'year'
)

FLOATS = (
    'document_value',
    'remark_value',
    'total_net_value'
)

TYPES = tuple(chain(
    ((field, IntegerField) for field in INTEGERS),
    ((field, FloatField) for field in FLOATS),
    (('issue_date', DateAsStringField),),
    (('numbers', ArrayField),),
))


def serialize(row):
    """
    Read the dict generated by the reimbursement command and returns a
    Reimbursement model instance.
    """
    for key, type_ in TYPES:
        value = row.get(key)
        row[key] = type_.deserialize(value)

    return Reimbursement(**row)
