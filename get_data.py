import random


def get_num(min, max, places):
    """
    根据范围生成符合要求的数字
    :param min: 取值范围1
    :param max: 取值范围2
    :param places: 小数位数
    :return: 返回生成数
    """

    # 整数
    if places == 0:
        if min > max: min, max = max, min
        return random.randint(min, max)

    # 小数
    else:
        return round(random.uniform(min, max), places)


def _get_num(int_places, float_places):
    """
    根据整数位数和小数位数生成数字
    :param int_places: 整数位数
    :param float_places: 小数位数
    :return: 返回给get_num生成数
    """
    min = 10 ** (int_places - 1)
    max = 10 ** int_places - 1
    return get_num(min, max, float_places)


def get_date():
    """
    生成日期，范围在1800-2040
    :return: 日期字符串
    """
    month = get_num(1, 12, 0)
    day = get_num(1, 31, 0)
    year = get_num(1800, 2040, 0)
    return '{:0>2d}/{:0>2d}/{}'.format(month, day, year)


def get_money():
    """
    生成价格，两位整数，两位小数
    :return: 价格浮点数
    """
    return '$%s' % get_num(0, 100, 2)


def get_time():
    """
    生成时间24小时制
    :return: 返回时间字符串
    """
    hour = get_num(0, 24, 0)
    minute = get_num(0, 60, 0)
    return '{:0>2d}:{:0>2d}'.format(hour, minute)


def get_teen():
    """
    生成teen易混淆数字
    :return: 返回整数数字
    """
    teen_list = [
        12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90
    ]
    return random.choice(teen_list)


def get_tel():
    """
    生成电话，范围在1800-2040
    :return: 日期字符串
    """
    tel1 = _get_num(3, 0)
    tel2 = _get_num(3, 0)
    tel3 = _get_num(3, 0)
    return '{:0>3d}-{:0>3d}-{:0>3d}'.format(tel1, tel2, tel3)


def get_no():
    """
    生成序数，范围在1-30
    :return: 返回整数序数
    """
    return get_num(1, 30, 0)

if __name__ == '__main__':
    print(get_time())
