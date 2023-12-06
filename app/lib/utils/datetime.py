from datetime import date, datetime


_TIME_PATTERN = '%I:%M %p'
_DATE_PATTERN = '{} {}, {}'
_MONTH = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]


def format_dt(dt: datetime, reference_date: date) -> str:
    '''
    Format a datetime object based on a reference date.

    :param dt: The datetime object to be formatted.
    :type dt: datetime

    :param reference_date: The reference date for comparison.
    :type reference_date: date

    :return: The formatted datetime string.
    :rtype: str
    '''
    if dt.date() == reference_date:
        formatted_dt = dt.strftime(_TIME_PATTERN)
    else:
        month_idx = dt.month - 1
        formatted_dt = _DATE_PATTERN.format(_MONTH[month_idx], dt.day, dt.year)

    return formatted_dt
