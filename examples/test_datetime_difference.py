from datetime import datetime

from pf_py_datetime.pfpd_datetime_util import PFPDDatetimeUtil


def test1():
    # datetime(year, month, day, hour, minute, second)
    previous = datetime(2022, 2, 11, 20, 26, 0)
    response = PFPDDatetimeUtil.difference_min_hour_day_full(previous)
    print(response)


if __name__ == '__main__':
    test1()
