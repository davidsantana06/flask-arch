from datetime import date, datetime
from typing import List


DATE_PATTERN: str = '{month} {day}, {year}'
MONTH: List[str] = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]


def format_datetime(dt: datetime, reference_date: date):
    formatted_dt: str = ''

    if dt.date() == reference_date:
        formatted_dt = dt.strftime('%I:%M %p')
    else:
        month_idx: int = dt.month - 1
        formatted_dt = DATE_PATTERN.format(
            month=MONTH[month_idx], day=dt.day, year=dt.year
        )

    return formatted_dt
