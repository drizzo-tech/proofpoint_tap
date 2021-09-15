# tapclient



One to two paragraph statement about your product and what it does.


## Installation

OS X & Linux:

```sh
python -m pip install tapclient
```

Windows:

```sh
py -m pip install tapclient
```

## Usage and Tutorial
Create a front end script to import the TAPClient class and create a new TAPClient object with your TAP Sevice Principal and Key.
Use the json module to browse data.

```python
from tapclient import TAPClient
import json

sp = '<your service principal here>'
api_key = '<your api key here>'
tap = TAPClient(sp, api_key)
```

### SIEM API
Methods:
* get_all_events
* get_clicks_blocked
* get_clicks_permitted
* get_messages_blocked
* get_messages_delivered
* get_issues (clicks permitted + messages delivered)

<br>

Parameters:
- params - Dictionary of valid params
- sinceSeconds - int representing seconds
- format - str representing returned format

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
    


### get_all_events(params, sinceSeconds, format)
#### parameters:
**params** - (Optional) dict of supported API parameters
- Accepted keys:

**sinceSeconds** - (Optional) int representing the number of seconds to fetch events, defaults to 600

**format** - (Optional) str representing the returned format, defaults to 'json'
- Accepted values: 'syslog', 'json'

### get_clicks_blocked
#### parameters:
**params** - (Optional) dict of supported API parameters

**sinceSeconds** - (Optional) int representing the number of seconds to fetch events, defaults to 600

**format** - (Optional) str representing the returned format, defaults to 'json'
- Accepted values: 'syslog', 'json'

### get_clicks_permitted
#### parameters:
**params** - (Optional) dict of supported API parameters

**sinceSeconds** - (Optional) int representing the number of seconds to fetch events, defaults to 600

**format** - (Optional) str representing the returned format, defaults to 'json'
- Accepted values: 'syslog', 'json'

### get_messages_blocked
#### parameters:
**params** - (Optional) dict of supported API parameters

**sinceSeconds** - (Optional) int representing the number of seconds to fetch events, defaults to 600

**format** - (Optional) str representing the returned format, defaults to 'json'
- Accepted values: 'syslog', 'json'

### get_messages_delivered
#### parameters:
**params** - (Optional) dict of supported API parameters

**sinceSeconds** - (Optional) int representing the number of seconds to fetch events, defaults to 600

**format** - (Optional) str representing the returned format, defaults to 'json'
- Accepted values: 'syslog', 'json'

### get_issues
#### parameters:
**params** - (Optional) dict of supported API parameters

**sinceSeconds** - (Optional) int representing the number of seconds to fetch events, defaults to 600

**format** - (Optional) str representing the returned format, defaults to 'json'
- Accepted values: 'syslog', 'json'


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
_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
* 0.0.1
    * Work in progress

## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki