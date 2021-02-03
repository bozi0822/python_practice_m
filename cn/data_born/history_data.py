import random
import datetime
import time


def datetime_to_timestamp(date_time):
    return datetime.datetime.timestamp(date_time)


def timestamp_to_string(stamp):
    return time.strftime("%Y-%m-%d-%H", time.localtime(stamp))


def history_data_generation(device_code, param_code, upper, lower, num):
    today_datetime = datetime.datetime.now()
    # today = today_datetime.strftime("%Y%m%d")

    for i in range(num):
        no = str(i).zfill(4)
        timestamp_now = '%d' % (datetime_to_timestamp(today_datetime))
        offset = datetime.timedelta(minutes=(i + 1))
        history_id = 'eamtest' + timestamp_now + no
        param_value = random.randint(lower, upper)
        datetime_acquisition = (today_datetime - offset * 0.3).strftime("%Y-%m-%d %H:%M:%S")

        sql = "insert into device_parameter_history \n" \
              "      (history_id,\n" \
              "       device_code,\n" \
              "       param_code,\n" \
              "       param_value,\n" \
              "       datetime_acquisition)\n" \
              "    values\n" \
              f"      ('{history_id}',\n" \
              f"       '{device_code}',\n" \
              f"       '{param_code}',\n" \
              f"       '{param_value}',\n" \
              f"       to_date('{datetime_acquisition}', 'yyyy-MM-dd HH24:mi:ss'));"

        print(sql + '\n')


if __name__ == '__main__':
    # A1202050001180953
    # 22070100060003200049 电压
    # 22070100060003200050 电流
    # 22070100060003200051 频率
    # 22070100060003200052 功率

    # A1202050001200011
    # 22070100060003200049 电压
    # 22070100060003200050 电流
    # 22070100060003200051 频率
    # 22070100060003200052 功率
    device_code = 'A1202050001180953'
    param_code = '22070100060003200049'  # 电压
    upper = 250
    lower = 200
    history_data_generation(device_code=device_code, param_code=param_code, upper=upper, lower=lower, num=300)
