from proofpoint_tap import TAPClient
import json

with open('settings.json', 'r') as f:
    settings = json.load(f)

tap_client = TAPClient(
    settings['service_principal'],
    settings['key']
)

events = tap_client.get_all_events()
print(events)
