from django.db import connection
from collections import namedtuple


def select_sql(sql, *args):
    cursor = connection.cursor()

    if args:
        cursor.execute(sql, args)
    else:
        cursor.execute(sql)

    # row = cursor.fetchall()
    row = named_tuple_fetchall(cursor)

    return row


def named_tuple_fetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])

    return [nt_result(*row) for row in cursor.fetchall()]
