import datetime

import ephem  # pip install pyephem
import pytz


__all__ = ['date_sun_info']


def date_sun_info(latitude=None, longitude=None, calc_date=None):
    """
    Mimics PHPs `date_sun_info` using `pyephem`. Use `pytz` to set a timezone for the `calc_date`.
    """

    # Initialize the location
    latitude = latitude or '35.3484055'  # Moore, OK, USA  @35.3484055,-97.48163
    longitude = longitude or '-97.48163'
    # Use calc_date if given, otherwise start fresh with utcnow (shifted to US/Central to match lat,lon)
    calc_date = calc_date or datetime.datetime.utcnow().replace(tzinfo=pytz.utc)\
        .astimezone(pytz.timezone('US/Central'))

    # Find the first second of the day for the date provided by calc_date
    start_date = datetime.datetime(calc_date.year, calc_date.month, calc_date.day, 0, 0, 0)
    # Set the start_date timezone to match the calc_date timezone, or if unavailable assume it is utc.
    try:
        start_date = calc_date.tzinfo.localize(start_date)
    except AttributeError:
        start_date = calc_date.replace(tzinfo=pytz.utc)

    results = dict()

    # Create an ephem observer object with our location and date
    observer = ephem.Observer()
    observer.lat = latitude
    observer.lon = longitude
    observer.date = start_date.astimezone(pytz.utc)  # shift start_date to utc for use with ephem

    # Set pressure to 0.0 to match the U.S. Naval Observatory calculation procedure
    observer.pressure = 0.0  # Defaults to 1010.0

    # Find the Sun transit time (solar noon) and update observer date for future calculations
    results['transit'] = observer.next_transit(ephem.Sun()).datetime()
    observer.date = results['transit']

    # Calculate sunrise, sunset (horizon '-0:34')
    observer.horizon = '-0:34'
    results['previous_sunset'] = observer.previous_setting(ephem.Sun()).datetime()
    results['sunrise'] = observer.previous_rising(ephem.Sun()).datetime()
    results['sunset'] = observer.next_setting(ephem.Sun()).datetime()
    results['next_sunrise'] = observer.next_rising(ephem.Sun()).datetime()

    # Calculate civil twilight (horizon @ -6)
    observer.horizon = '-6'
    results['civil_twilight_begin'] = observer.previous_rising(ephem.Sun(), use_center=True).datetime()
    results['civil_twilight_end'] = observer.next_setting(ephem.Sun(), use_center=True).datetime()

    # Calculate nautical twilight (horizon @ -12)
    observer.horizon = '-12'
    results['nautical_twilight_begin'] = observer.previous_rising(ephem.Sun(), use_center=True).datetime()
    results['nautical_twilight_end'] = observer.next_setting(ephem.Sun(), use_center=True).datetime()

    # Calculate astronomical twilight (horizon @ -18) (Earliest and latest light visible)
    observer.horizon = '-18'
    results['astronomical_twilight_begin'] = observer.previous_rising(ephem.Sun(), use_center=True).datetime()
    results['astronomical_twilight_end'] = observer.next_setting(ephem.Sun(), use_center=True).datetime()

    for key in results:
        # everything ephem does is in utc, so add the timezone to the results
        results[key] = results[key].replace(tzinfo=pytz.utc)
        # shift the results to match the timezone provided by calc_date
        results[key] = results[key].astimezone(calc_date.tzinfo)

    return results


def main():
    print 'DateSunInfo:'
    print date_sun_info()
