# recommendation-engine-sandbox
To build it:
```sh
docker-compose up --build
```

Then you can visit the http://localhost:8290/

To send an event to divolte:
```js
divolte.signal('event', {"item_id": 101321, "event_date":3213213})
```
To connect Apache Cassandra:
```sh
docker-compose exec  cassandra /bin/bash
```
```sh
cqlsh localhost -ucassandra -pcassandra
```
```sql
SELECT * FROM demo.click_stream;
```

Result:
```sh
pk         | created_at                      | client_ip     | cookie_id                                   | event_name | item_id | url
------------+---------------------------------+---------------+---------------------------------------------+------------+---------+------------------------
 2019-10-20 | 2019-10-20 17:15:19.607000+0000 | 192.168.224.1 | 0:k1co3zug:yAGV1PjuaWIQEmZ1Yx~f8eHnB~Yr9Eqo |      event |  101321 | http://localhost:8290/
 2019-10-20 | 2019-10-20 17:15:24.445000+0000 | 192.168.224.1 | 0:k1co3zug:yAGV1PjuaWIQEmZ1Yx~f8eHnB~Yr9Eqo |      event |  101321 | http://localhost:8290/
 2019-10-20 | 2019-10-20 17:15:32.199000+0000 | 192.168.224.1 | 0:k1co3zug:yAGV1PjuaWIQEmZ1Yx~f8eHnB~Yr9Eqo |      event |  101321 | http://localhost:8290/
 2019-10-20 | 2019-10-20 20:51:02.638000+0000 | 192.168.224.1 | 0:k1co3zug:yAGV1PjuaWIQEmZ1Yx~f8eHnB~Yr9Eqo |      event |  101321 | http://localhost:8290/
 2019-10-20 | 2019-10-20 20:51:03.251000+0000 | 192.168.224.1 | 0:k1co3zug:yAGV1PjuaWIQEmZ1Yx~f8eHnB~Yr9Eqo |      event |  101321 | http://localhost:8290/
 2019-10-20 | 2019-10-20 20:51:07.953000+0000 | 192.168.224.1 | 0:k1co3zug:yAGV1PjuaWIQEmZ1Yx~f8eHnB~Yr9Eqo |      event |  101321 | http://localhost:8290/
 2019-10-20 | 2019-10-20 20:51:09.155000+0000 | 192.168.224.1 | 0:k1co3zug:yAGV1PjuaWIQEmZ1Yx~f8eHnB~Yr9Eqo |      event |  101321 | http://localhost:8290/
 2019-10-20 | 2019-10-20 20:51:09.849000+0000 | 192.168.224.1 | 0:k1co3zug:yAGV1PjuaWIQEmZ1Yx~f8eHnB~Yr9Eqo |      event |  101321 | http://localhost:8290/
 2019-10-20 | 2019-10-20 20:51:10.405000+0000 | 192.168.224.1 | 0:k1co3zug:yAGV1PjuaWIQEmZ1Yx~f8eHnB~Yr9Eqo |      event |  101321 | http://localhost:8290/
 2019-10-20 | 2019-10-20 20:51:10.908000+0000 | 192.168.224.1 | 0:k1co3zug:yAGV1PjuaWIQEmZ1Yx~f8eHnB~Yr9Eqo |      event |  101321 | http://localhost:8290/
