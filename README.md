# Proofpoint TAP API Client for Python

A python library for Proofpoint's Targeted Attack Protection (TAP) API

## Installation

OS X & Linux:

```sh
python -m pip install proofpoint_tap
```

Windows:

```sh
py -m pip install proofpoint_tap
```

## Usage and Tutorial
Create a front end script to import the TAPClient class and create a new TAPClient object with your TAP Sevice Principal and Key.
Use the json module to browse data.

```python
from proofpoint_tap import TAPClient
import json

sp = '<your service principal here>'
api_key = '<your api key here>'
tap = TAPClient(sp, api_key)
```

## Class Object
>### TAPClient(service_principal, api_key, base_url=*str*)
#### Parameters:
* **service_principal** (pos, required) - *str* Service Principal obtained from TAP Dashboard
* **api_key** (pos, required) - *str* API Key obtained from TAP Dashbaord
* **base_url** (optional) - *str* TAP API Url, only used if a different url is needed, defaults to 'https://tap-api-v2.proofpoint.com/v2'

---
<br>

## Class Methods

<br>

>### SIEM API
*Data format: json, syslog*

Methods:
* get_all_events - Get all TAP events
* get_clicks_blocked - Get all clicks_blocked events
* get_clicks_permitted - Get all clicks_permitted events
* get_messages_blocked - Get all messages_blocked events
* get_messages_delivered - Get all messages_delivered events
* get_issues - Get all clicks_permitted + messages_delivered events

<br>

Parameters:
* params - *dict* Dictionary of valid params
* sinceSeconds - *int* Integer representing seconds
* format - *str* String representing returned format

Valid params:
* 'interval' 
(*if not included sinceSeconds will be used with default of 600*)
* 'sinceSeconds'
(*Defaults to 600*)
* 'sinceTime'
(*if not included sinceSeconds will be used with default of 600*)
* 'format'
(*'json' or 'syslog', if not included will default to 'json'*)
* 'threatStatus'
(*'active', 'cleared', 'falsePositive*)
* 'threatType'
(*'url', 'attachment', 'messageText'*)

*sinceSeconds and format can be used as direct kwargs to provide easier syntax*

*see Proofpoint TAP documentations for valid parameter values*
    
<br>

>### get_all_events(params=*dict*, sinceSeconds=*int*, format=*str*)
#### Parameters:
**params** (optional) - *dict* Dictionary of supported API parameters

**sinceSeconds** (optional) - *int* Integer representing the number of seconds to fetch events, defaults to 600

**format** (optional) - *str* String representing the returned format, defaults to 'json'
* Accepted values: 'syslog', 'json'

<br>

>### get_clicks_blocked(params=*dict*, sinceSeconds=*int*, format=*str*)
#### Parameters:
**params** (optional) - *dict* Dictionary of supported API parameters

**sinceSeconds** (optional) - *int* Integer representing the number of seconds to fetch events, defaults to 600

**format** (optional) - *str* String representing the returned format, defaults to 'json'
* Accepted values: 'syslog', 'json'

<br>

>### get_clicks_permitted(params=*dict*, sinceSeconds=*int*, format=*str*)
#### Parameters:
**params** (optional) - *dict* Dictionary of supported API parameters

**sinceSeconds** (optional) - *int* Integer representing the number of seconds to fetch events, defaults to 600

**format** (optional) - *str* String representing the returned format, defaults to 'json'
* Accepted values: 'syslog', 'json'

<br>

>### get_messages_blocked(params=*dict*, sinceSeconds=*int*, format=*str*)
#### Parameters:
**params** (optional) - *dict* Dictionary of supported API parameters

**sinceSeconds** (optional) - *int* Integer representing the number of seconds to fetch events, defaults to 600

**format** (optional) - *str* String representing the returned format, defaults to 'json'
* Accepted values: 'syslog', 'json'

<br>

>### get_messages_delivered(params=*dict*, sinceSeconds=*int*, format=*str*)
#### Parameters:
**params** (optional) - *dict* Dictionary of supported API parameters

**sinceSeconds** (optional) - *int* Integer representing the number of seconds to fetch events, defaults to 600

**format** (optional) - *str* String representing the returned format, defaults to 'json'
* Accepted values: 'syslog', 'json'

<br>

>### get_issues(params=*dict*, sinceSeconds=*int*, format=*str*)
#### Parameters:
**params** (optional) - *dict* Dictionary of supported API parameters

**sinceSeconds** (optional) - *int* Integer representing the number of seconds to fetch events, defaults to 600

**format** (optional) - *str* String representing the returned format, defaults to 'json'
* Accepted values: 'syslog', 'json'

---
### Get SIEM events examples:
Get all events in the last 10 minutes returned as a dict
```py
events = json.loads(tap.get_all_events())
```
Get clicks permitted in the last 30 minutes returned as a syslog string
```py
events = tap.get_all_events(sinceSeconds=1800, format='syslog')
```
Get issues in the last 30 minutes with threatStatus=active, returned as json string
```py
events = tap.get_issues(
    params={
        'sinceSeconds': 600,
        'threatStatus': 'active',
        'format': 'json'
    })
```
---
<br>

>### Forensics API
*Data format: json*

Methods:
* get_forensics - Obtain forensic data for a specific threat or campaign

<br>


>### get_forensics(campaignID=*str*, threatID=*str*, includeCampaignForensics=*bool*)
#### Parameters:
**threatID** (required or campaignID) - *str* threatId obtained from SIEM API logs

**campaignID** (required or threatID) - *str* campaignId obtained from SIEM API logs

**includeCampaignForensics** (optional) - *bool* Defaults to False

---

### Get forensics data examples:
Get threat forensics as json string
```py
forensics = tap.get_forensics(threatID='<threatId>')
```
Get threat forensics with campaign info as dict
```py
forensics = json.loads(tap.get_forensics(threatID='<threatId>', includeCampaignForensics=True))
```
Get campaign forensics as json string
```py
forensics = tap.get_forensics(campaignID='<campaignId>')
```
---
<br>

>### Campaign API
*Data format: json*

Methods:
* get_campaign
* get_all_campaigns

<br>

>### get_campaign(campaignID)
#### Parameters:
**campaignID** (required) - *str* campaignId obtained from SIEM API logs

<br>

>### get_all_campaigns(params=*dict*, interval=*str*)
#### Parameters:
**params** (optional) - *dict* Dictionary of supported API parameters
* Valid params:
  * 'interval' - *str*
    * A string containing an ISO8601-formatted interval i.e '2020-05-01T12:00:00Z/2020-05-01T13:00:00Z'
    * If not provided, a default interval of 1 day from now will be used
  * 'size' - *int*
    * The maximum number of campaign IDs to retrieve, defaults to 100, max is 200 
  * 'page' - *int*
    * The page of results to return

**interval** (optional) - *str* A string containing an ISO8601-formatted interval i.e '2020-05-01T12:00:00Z/2020-05-01T13:00:00Z'
* Can be used as a kwarg instead of in params to make syntax easier
* If not provided, a default interval of 1 day from now will be used
---
### Get campaigns data examples:
Get campaignID as json string
```py
campaign = tap.get_campaign('<campaignId>')
```
Get campaignID as dict
```py
campaign = json.loads(tap.get_campaign('<campaignId>')
```
Get all campaign IDs in the last 24 hours
```py
campaigns = tap.get_all_campaigns()
```
---

<br>

>### Threat API
*Data format: json*

Methods:
* get_threat_details

<br>

>### get_threat_details(threatID)
#### Parameters:
**threatID** (required) - *str* threatId obtained from SIEM logs

---
### Get campaigns data examples:
Get threatID as json string
```py
threat = tap.get_threat_details('<threatId>')
```
Get threatID as dict
```py
threat = json.loads(tap.get_threat_details('<threatId>')
```
---

<br>

>### People API
*Data format: json*

Methods:
* get_vap_report
* get_top_clicker_report

<br>

>### get_vap_report(params=*dict*, window=*int*)
#### Parameters:
**params** (optional) - *dict* Dictionary of supported API parameters
* Valid params:
  * 'window' - *int* Number of days back to report on
    * Defaults to 30 days
    * Accepted values are 14, 30 and 90
  * 'size' - *int* Number of results to include
  * 'page' - *int* Page number of results to return

**window** (optional) - *int* Number of days back to report on
* Can be used as a kwarg instead of in params to make syntax easier
* Defaults to 30 days
* Accepted values are 14, 30 and 90

<br>

>### get_top_clicker_report(params=*dict*, window=*int*)
#### Parameters:
**params** (optional) - *dict* Dictionary of supported API parameters
* Valid params:
  * 'window' - *int* Number of days back to report on
    * Defaults to 30 days
    * Accepted values are 14, 30 and 90
  * 'size' - *int* Number of results to include
  * 'page' - *int* Page number of results to return

**window** (optional) - *int* Number of days back to report on
* Can be used as a kwarg instead of in params to make syntax easier
* Defaults to 30 days
* Accepted values are 14, 30 and 90

---
### Get people report examples:
Get VAP report for last 30 days
```py
vap = tap.get_vap_report()
```
Get VAP report for the last 90 days
```py
vap = tap.get_vap_report(params={'window': 90})
```
Get Top Clicker report for the last 90 days as dict
```py
clickers = json.loads(tap.get_top_clicker_report(window=90))
```
---

<br>

>### URL Decoder API
*Data format: json*

Methods:
* decode_url

<br>

>### decode_url(data=*dict*)
#### Parameters:
**data** (required) - *dict* Dictionary with a list of urls to decode
* Dictionary scheme: `{'urls': ['<url1>', '<url2>']}`

---
### URL Decode examples:
Decode urls as json string
```py
urls = {
    'urls': [
        'https://urldefense.proofpoint.com/v2/url?u=http-3A__links.mkt3337.com_ctt-3Fkn-3D3-26ms-3DMzQ3OTg3MDQS1-26r-3DMzkxNzk3NDkwMDA0S0-26b-3D0-26j-3DMTMwMjA1ODYzNQS2-26mt-3D1-26rt-3D0&d=DwMFaQ&c=Vxt5e0Osvvt2gflwSlsJ5DmPGcPvTRKLJyp031rXjhg&r=MujLDFBJstxoxZI_GKbsW7wxGM7nnIK__qZvVy6j9Wc&m=QJGhloAyfD0UZ6n8r6y9dF-khNKqvRAIWDRU_K65xPI&s=ew-rOtBFjiX1Hgv71XQJ5BEgl9TPaoWRm_Xp9Nuo8bk&e='
    ]
}
decoded = tap.decode_url(urls)
```
Decode multiple urls as dict
```py
urls = {
    "urls": [
        "https://urldefense.proofpoint.com/v2/url?u=http-3A__links.mkt3337.com_ctt-3Fkn-3D3-26ms-3DMzQ3OTg3MDQS1-26r-3DMzkxNzk3NDkwMDA0S0-26b-3D0-26j-3DMTMwMjA1ODYzNQS2-26mt-3D1-26rt-3D0&d=DwMFaQ&c=Vxt5e0Osvvt2gflwSlsJ5DmPGcPvTRKLJyp031rXjhg&r=MujLDFBJstxoxZI_GKbsW7wxGM7nnIK__qZvVy6j9Wc&m=QJGhloAyfD0UZ6n8r6y9dF-khNKqvRAIWDRU_K65xPI&s=ew-rOtBFjiX1Hgv71XQJ5BEgl9TPaoWRm_Xp9Nuo8bk&e=",
        "https://urldefense.proofpoint.com/v1/url?u=http://www.bouncycastle.org/&amp;k=oIvRg1%2BdGAgOoM1BIlLLqw%3D%3D%0A&amp;r=IKM5u8%2B%2F%2Fi8EBhWOS%2BqGbTqCC%2BrMqWI%2FVfEAEsQO%2F0Y%3D%0A&amp;m=Ww6iaHO73mDQpPQwOwfLfN8WMapqHyvtu8jM8SjqmVQ%3D%0A&amp;s=d3583cfa53dade97025bc6274c6c8951dc29fe0f38830cf8e5a447723b9f1c9a",
        "https://urldefense.com/v3/__https://google.com:443/search?q=a*test&gs=ps__;Kw!-612Flbf0JvQ3kNJkRi5Jg!Ue6tQudNKaShHg93trcdjqDP8se2ySE65jyCIe2K1D_uNjZ1Lnf6YLQERujngZv9UWf66ujQIQ$"
    ]
}
decoded = json.loads(tap.decode_url(urls))
```
---

## Release History

* 0.0.2
    * Updated documentation, no code changes
* 0.0.1
    * Work in progress
