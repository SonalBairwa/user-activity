# user-activity api

This app is responsible for list out user and their activity period.

* Base URL
```
BASE_URL/API_NAME/
```
For example: http://localhost:8000/user-activity/

The project already added throttling. A user cannot call any api more than specified in config/base_setting.py in a day.
```
'DEFAULT_THROTTLE_CLASSES': (
    'rest_framework.throttling.AnonRateThrottle',
    'rest_framework.throttling.UserRateThrottle'
),
'DEFAULT_THROTTLE_RATES': {
    'anon': '50/day',
    'user': '100/day'
},
```

