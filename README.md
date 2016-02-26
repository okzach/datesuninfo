# datesuninfo

Mimics PHPs `date_sun_info()` using python and `ephem`.

Sunrise, solar noon, sunset, and twilight start/end times for a given location and datetime.

## Example

```python
from datesuninfo import date_sun_info
sun_info = date_sun_info(latitude='35.3484055', longitude='-97.48163')
print sun_info.get('sunrise')
print sun_info.get('transit')  # solar noon
print sun_info.get('sunset')
print sun_info.keys()
```
outputs:
```
2016-01-27 13:33:04.804825
2016-01-27 18:42:36.645308
2016-01-27 23:52:29.782016
['civil_twilight_end', 'nautical_twilight_end', 'transit', 'previous_sunset', 'sunset', 'next_sunrise', 'astronomical_twilight_begin', 'astronomical_twilight_end', 'civil_twilight_begin', 'sunrise', 'nautical_twilight_begin']
```

## History

This is a functional work-in-progress.  I use it for personal projects; that is the purpose it serves.

The last time this project saw love was February 2016.