import json
import math
from itertools import groupby

import pygal

# 将数据加载到一个列表中
filename = 'data/btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

dates, months, weeks, weekdays, close = [], [], [], [], []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))


def normal():
    line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
    line_chart.title = '收盘价（￥）'
    line_chart.x_labels = dates
    N = 20  # x轴坐标每隔20天显示一次
    line_chart.x_labels_major = dates[::N]
    line_chart.add('收盘价', close)
    line_chart.render_to_file('收盘价折线图（￥）.charts')


def log10():
    line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
    line_chart.title = '收盘价对数变换（￥）'
    line_chart.x_labels = dates
    N = 20  # x轴坐标每隔20天显示一次
    line_chart.x_labels_major = dates[::N]
    close_log = [math.log10(_) for _ in close]
    line_chart.add('log收盘价', close_log)
    line_chart.render_to_file('收盘价对数变换折线图（￥）.charts')


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = zip(*xy_map)

    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    return line_chart


def month_mean():
    idx_month = dates.index('2017-12-01')
    line_chart = draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值（￥）', '月日均值')
    line_chart.render_to_file('收盘价月日均值（￥）' + '.charts')


def week_mean():
    idx_week = dates.index('2017-12-11')
    line_chart = draw_line(weeks[1:idx_week], close[1:idx_week], '收盘价周日均值（￥）', '周日均值')
    line_chart.render_to_file('收盘价周日均值（￥）' + '.charts')


def weekday_mean():
    idx_week = dates.index('2017-12-11')
    wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
    line_chart = draw_line(weekdays_int, close[1:idx_week], '收盘价星期日均值（￥）', '星期日均值')
    line_chart.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    line_chart.render_to_file('收盘价星期日均值（￥）.charts')


def show_all():
    with open('charts/收盘价dashboard.html', 'w', encoding='utf-8') as html_file:
        html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
        for svg in [
            '收盘价折线图（￥）.charts', '收盘价对数变换折线图（￥）.charts', '收盘价月日均值（￥）.charts',
            '收盘价周日均值（￥）.charts', '收盘价星期日均值（￥）.charts'
        ]:
            html_file.write('    <object type="image/charts+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')


# month_mean()
# week_mean()
# weekday_mean()
show_all()

