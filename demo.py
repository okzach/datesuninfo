from __future__ import print_function

import datetime

import pytz

from datesuninfo import date_sun_info


# Get the current time in utc and assign it the pytz utc time zone
calc_date = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
# Shift the calc_date to Central time zone
calc_date = calc_date.astimezone(pytz.timezone('US/Central'))

# Get the date_sun_info for Moore, OK using the current time in the central time zone.
sun_info = date_sun_info(latitude='35.3484055', longitude='-97.48163', calc_date=calc_date)

print('Sunrise: {0}'.format(sun_info.get('sunrise')))
print('Solar Noon: {0}'.format(sun_info.get('transit')))
print('Sunset: {0}'.format(sun_info.get('sunset')))

print(sun_info.keys())
