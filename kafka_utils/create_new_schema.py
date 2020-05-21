import requests

schema_registry_url = 'http://localhost:8081'
topic = 'telegram_00_test'
schema_file = '/Users/jannitschke/Google Drive/Uni/Master/1. Semester/IoSL/source/iosl/IoSL/avro_schemas/telegram_channel_message.avsc'


print("Schema Registry URL: " + schema_registry_url)
print("Topic: " + topic)
print("Schema file: " + schema_file)


with open(schema_file, 'r') as content_file:
    schema = content_file.read()

payload = "{ \"schema\": \"" \
          + schema.replace("\"", "\\\"").replace("\t", "").replace("\n", "") \
          + "\" }"

url = schema_registry_url + "/subjects/" + topic + "-value/versions"
headers = {"Content-Type": "application/vnd.schemaregistry.v1+json"}

r = requests.post(url, headers=headers, data=payload)
if r.status_code == requests.codes.ok:
    print("Success")
else:
    r.raise_for_status()
