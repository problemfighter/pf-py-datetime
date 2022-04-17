from datetime import datetime

from pf_py_datetime.pfpd_datetime_util import PFPDDatetimeUtil


def test1():
    # datetime(year, month, day, hour, minute, second)
    previous = datetime(2022, 2, 11, 20, 26, 0)
    response = PFPDDatetimeUtil.difference_min_hour_day_full(previous)
    print(response)


def date_time_split():
    date_time_data = PFPDDatetimeUtil.data_time_split()
    print("Day : " + str(date_time_data.day))
    print("Month : " + str(date_time_data.month))
    print("Month Name : " + str(date_time_data.monthName))
    print("Year : " + str(date_time_data.year))
    print("Hour 24 : " + str(date_time_data.hour24))
    print("Hour 12 : " + str(date_time_data.hour12))
    print("Minute : " + str(date_time_data.minute))
    print("Second : " + str(date_time_data.second))
    print("AM PM : " + str(date_time_data.amPm))
    print("Day of Year : " + str(date_time_data.dayOfYear))
    print("Week of Year : " + str(date_time_data.weekOfYear))


if __name__ == '__main__':
    date_time_split()
    # test1()
