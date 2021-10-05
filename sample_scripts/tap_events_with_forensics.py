from proofpoint_tap import TAPClient
import json

with open('settings.json', 'r') as f:
    settings = json.load(f)

tap = TAPClient(
    settings['service_principal'],
    settings['key']
)

events = json.loads(tap.get_all_events(sinceSeconds=3600))
for event in events['messagesBlocked']:
    for threat in event['threatsInfoMap']:
        if threatID := threat['threatID']:
            threat['forensicsInfo'] = json.loads(tap.get_forensics(threatID=threatID))
        if campaignID := threat['campaignID']:
            threat['campaignInfo'] = json.loads(tap.get_campaign(campaignID=campaignID))

print(json.dumps(events, indent=4))


