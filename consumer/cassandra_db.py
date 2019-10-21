import os
from datetime import datetime

from cassandra.cqlengine.management import sync_table
from cassandra.policies import TokenAwarePolicy
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import (
    Cluster,
    DCAwareRoundRobinPolicy
)
from cassandra.cqlengine.connection import (
    register_connection,
    set_default_connection
)

from click_stream_item_model import ClickItemModel


class Cassandra:
    """Cassandra db class."""
    session = None
    cluster = None
    key_space = os.getenv('KAFKA_CONSUMER_GROUP')

    def __init__(self):
        self.connect()

    def connect(self):
        """ DB connection."""
        auth_provider = PlainTextAuthProvider(username=os.getenv('CASSANDRA_USERNAME'),
                                              password=os.getenv('CASSANDRA_PASSWORD'))

        self.cluster = Cluster(
            [os.getenv('CASSANDRA_HOST')],
            load_balancing_policy=TokenAwarePolicy(DCAwareRoundRobinPolicy()),
            port=os.getenv('CASSANDRA_PORT'),
            auth_provider=auth_provider,
            executor_threads=2,
            protocol_version=4,
        )

        self.session = self.cluster.connect()
        register_connection(str(self.session), session=self.session)
        set_default_connection(str(self.session))

    def sync(self):
        """Sync method."""
        create_query = "CREATE KEYSPACE %s WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '%s'}" \
                       " AND durable_writes = true; "
        self.session.execute("DROP KEYSPACE IF EXISTS %s;" % self.key_space)
        self.session.execute(create_query % (self.key_space, 2,))

        sync_table(ClickItemModel)

    def save(self, data: dict):
        """Save data to cassandra."""
        ClickItemModel.create(
            pk=str(datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).date()),
            client_ip=data['client_ip'],
            cookie_id=data['click_stream_cookie_id'],
            event_name=data['event_name'],
            item_id=data['item_id'],
            url=data['url']
        )
        return True
