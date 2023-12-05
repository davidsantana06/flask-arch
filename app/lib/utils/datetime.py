from datetime import date, datetime


TIME_PATTERN = '%I:%M %p'
DATE_PATTERN = '{} {}, {}'
MONTH = [
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
        formatted_dt = dt.strftime(TIME_PATTERN)
    else:
        month_idx = dt.month - 1
        formatted_dt = DATE_PATTERN.format(MONTH[month_idx], dt.day, dt.year)

    return formatted_dt
