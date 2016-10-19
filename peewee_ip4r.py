import ipaddress

from peewee import Field, Expression, Param, OP
from playhouse.postgres_ext import PostgresqlExtDatabase, IndexedFieldMixin


class IPField(IndexedFieldMixin, Field):
    default_index_type = 'GiST'

    def db_value(self, value):
        return str(value)

    def __lshift__(self, other):
        return Expression(self, OP.IP4R_CONTAINED_BY, Param(other))
    def __rshift__(self, other):
        return Expression(self, OP.IP4R_CONTAINS, Param(other))

class IPAddressField(IPField):
    db_field = 'ipaddress'

    def python_value(self, value):
        return ipaddress.ip_address(value)

class IPRangeField(IPField):
    db_field = 'iprange'

    def python_value(self, value):
        return ipaddress.ip_network(value)

ip_ops = {
    'IP4R_CONTAINS': '>>=',
    'IP4R_STRICT_CONTAINS': '>>',
    'IP4R_CONTAINED_BY': '<<=',
    'IP4R_STRICT_CONTAINED_BY': '<<',
    'IP4R_OVERLAPS': '&&',
}

for op_name, op in ip_ops.items():
    OP[op_name] = 'IP' + op

PostgresqlExtDatabase.register_fields({'ipaddress': 'ipaddress', 'iprange': 'iprange'})
PostgresqlExtDatabase.register_ops({OP[op_name]: op for op_name, op in ip_ops.items()})
