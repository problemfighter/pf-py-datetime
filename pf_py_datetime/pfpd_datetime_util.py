from datetime import datetime, timedelta
from math import floor

from pf_py_datetime.data.date_time_data import DateTimeData


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

    @staticmethod
    def data_time_split(diff=0) -> DateTimeData:
        date_time_data = DateTimeData()
        date_difference = datetime.now() + timedelta(diff)

        date_time_data.day = date_difference.day
        date_time_data.month = date_difference.month
        date_time_data.monthName = date_difference.strftime("%B")
        date_time_data.year = date_difference.year
        date_time_data.hour12 = date_difference.strftime("%I")
        date_time_data.hour24 = date_difference.strftime("%H")
        date_time_data.minute = date_difference.minute
        date_time_data.second = date_difference.second
        date_time_data.weekday = date_difference.strftime("%A")
        date_time_data.amPm = date_difference.strftime("%p")
        date_time_data.dayOfYear = date_difference.strftime("%j")
        date_time_data.weekOfYear = date_difference.strftime("%W")

        return date_time_data

    @staticmethod
    def time_manipulation(time: str, source_time_format="%I:%M:%S", return_time_format="%I:%M:%S", hour=0, minute=0, second=0):
        parsed_time = datetime.strptime(time, source_time_format)
        diff = parsed_time + timedelta(hours=hour, minutes=minute, seconds=second)
        return diff.strftime(return_time_format)
