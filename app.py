from flask import Flask, render_template, request
from waitress import serve

from get_data import _get_num, get_time, get_date, get_money, get_teen, get_tel, get_no
from get_speech import get_speech

app = Flask(__name__)


def say_num(lang, rate, int_places, float_places):
    """
    生成随机数数据及语音（需as：math，准确来说整数需要，但是浮点数加了也行）
    :param lang: 语言
    :param rate: 速度
    :param int_places:整数位数
    :param float_places:小数位数
    :return: 随机数数据及语音
    """
    data = []
    for i in range(10):
        data.append(_get_num(int_places, float_places))

    say_as = 'math'
    file_name = get_speech(lang, rate, say_as, data)
    return data, file_name


def say_date(lang, rate):
    """
    生成日期金数据和语音（无需as）
    :param lang: 语言
    :param rate: 速度
    :return: 日期数据及语音
    """
    data = []
    for i in range(10):
        data.append(get_date())

    say_as = ''
    file_name = get_speech(lang, rate, say_as, data)
    return data, file_name


def say_money(lang, rate):
    """
    生成金额数据和语音（无需as）
    :param lang: 语言
    :param rate: 速度
    :return: 金额数据及语音
    """
    data = []
    for i in range(10):
        data.append(get_money())

    say_as = ''
    file_name = get_speech(lang, rate, say_as, data)
    return data, file_name


def say_time(lang, rate):
    """
    生成时间数据和语音（无需as）
    :param lang: 语言
    :param rate: 速度
    :return: 时间数据及语音
    """
    data = []
    for i in range(10):
        data.append(get_time())

    say_as = ''
    file_name = get_speech(lang, rate, say_as, data)
    return data, file_name


def say_teen(lang, rate):
    """
    生成teen/ty数据和语音（无需as）
    :param lang: 语言
    :param rate: 速度
    :return: teen/ty数据及语音
    """
    data = []
    for i in range(10):
        data.append(get_teen())

    say_as = ''
    file_name = get_speech(lang, rate, say_as, data)
    return data, file_name


def say_tel(lang, rate):
    """
    生成电话数据和语音（需as：telephone）
    :param lang: 语言
    :param rate: 速度
    :return: 电话数据及语音
    """
    data = []
    for i in range(10):
        data.append(get_tel())

    say_as = 'telephone'
    file_name = get_speech(lang, rate, say_as, data)
    return data, file_name


def say_no(lang, rate):
    """
    生成序数数据和语音（需as：ordinal）
    :param lang: 语言
    :param rate: 速度
    :return: 序数数据及语音
    """
    data = []
    for i in range(10):
        data.append(get_no())

    say_as = 'ordinal'
    file_name = get_speech(lang, rate, say_as, data)
    return data, file_name


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dictation/<lang>/<rate>', methods=['GET', 'POST'])
def say(lang, rate):
    data_list = [[
        '------使用方法------',
        '　生成数字：',
        '1、设置整数位数',
        '2、设置小数位数',
        '3、点击生成数字',
        '　',
        '　生成其他：',
        '1、点击生成内容',
        '2、等待直接生成',
        '--------------------'
    ], 'static/wav/0.mp3']

    getData = request.args.to_dict()
    if getData:
        value = getData['value']
        int_places = int(getData['int'])
        float_places = int(getData['float'])
        if value == 'num':
            data_list = say_num(lang, rate, int_places, float_places)
        elif value == 'date':
            data_list = say_date(lang, rate)
        elif value == 'time':
            data_list = say_time(lang, rate)
        elif value == 'no':
            data_list = say_no(lang, rate)
        elif value == 'money':
            data_list = say_money(lang, rate)
        elif value == 'tel':
            data_list = say_tel(lang, rate)
        elif value == 'teen':
            data_list = say_teen(lang, rate)
        else:
            data_list = say_num(lang, rate, int_places, float_places)

    # 数据监控
    print('生成数据：' + str(data_list[0]))
    print('生成语音文件：' + data_list[1])

    return render_template('dictation.html', lang=lang, rate = rate, data_list=data_list[0], file_name=data_list[1])


if __name__ == '__main__':
    app.run(debug=True, threaded=False)
    # serve(app, host='127.0.0.1', port=14771, threads=1)
    # num('en-US', '+0', 2, 2)
