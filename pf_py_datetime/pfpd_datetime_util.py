from datetime import datetime
from math import floor


class PFPDDatetimeUtil:

    @staticmethod
    def difference_min_hour_day_full(previous: datetime, current: datetime = None, str_format="%d %B %Y at %I:%M %p") -> str:
        date_time = "1m"
        if not current:
            current = datetime.now()
        if previous:
            difference = current - previous
            seconds = difference.total_seconds()
            if not seconds or seconds <= 0:
                return ""

            days = floor(seconds / (60 * 60 * 24))
            if 0 < days <= 7:
                return str(days) + "d"
            elif days > 7:
                return previous.strftime(str_format)

            hours = floor(seconds / (60 * 60))
            if hours > 0:
                return str(hours) + "h"

            minute = floor(seconds / 60)
            if minute > 0:
                return str(minute) + "m"
        return date_time
