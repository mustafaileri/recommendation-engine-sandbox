import os
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from datetime import datetime


class ClickItemModel(Model):
    """ClickstreamItem model for cassandra."""
    __keyspace__ = os.getenv('CASSANDRA_KEYSPACE')
    __table_name__ = os.getenv('CASSANDRA_CLICK_STREAM_TABLE')

    pk = columns.Text(primary_key=True, required=True, partition_key=True)
    created_at = columns.DateTime(primary_key=True, default=datetime.utcnow)
    cookie_id = columns.Text(required=True, index=True)
    item_id = columns.Text(required=True, index=True)
    event_name = columns.Text(required=True, index=True)
    url = columns.Text(required=False)
    client_ip = columns.Text(required=False)
