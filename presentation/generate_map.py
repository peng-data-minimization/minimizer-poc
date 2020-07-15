import json

from kafka import KafkaConsumer
import plotly.graph_objects as go
import pandas as pd
from confluent_kafka import Consumer


# c = Consumer({
#     'bootstrap.servers': '35.246.144.21:31090',
#     'group.id': 'mygroup',
#     'auto.offset.reset': 'earliest'
# })

# c.subscribe(['anon'])


mapbox_access_token = "pk.eyJ1Ijoiam9oYW5uZ29sdHoiLCJhIjoiY2tjbWFiaHRsMjBzcjJycXFuM3pseDEybSJ9.8MIAWvV1iG11vsGgLpmJsA"
consumer = KafkaConsumer(bootstrap_servers="35.246.144.21:31090", auto_offset_reset="latest",
                         value_deserializer=json.loads)
consumer.subscribe(["anon"])

consumer2 = KafkaConsumer(bootstrap_servers="35.246.144.21:31090", auto_offset_reset="latest",
                         value_deserializer=json.loads)
consumer2.subscribe(["processed"])

lon, lat = [], []
lon_new, lat_new = [], []
print("consumer ready")
index = 0
# while True:
#     msg = c.poll(1.0)
#     if not msg:
#         continue
#     index =+1
try:
    for msg in consumer:
        value = msg.value
        print(value)
        lon.append(value["position_long"])
        lat.append(value["position_lat"])
        for msg in consumer2:
            value = msg.value
            print(value)
            lon_new.append(value["position_long"])
            lat_new.append(value["position_lat"])
            break
except KeyboardInterrupt:

    print(lon, lat)
    fig = go.Figure(data=go.Scattermapbox(lon=lon, lat=lat))
    fig.add_trace(go.Scattermapbox(lon=lon_new, lat=lat_new))
    fig.update_layout(mapbox=dict(accesstoken=mapbox_access_token), mapbox_style="outdoors")
    fig.show()
