import json
from datetime import datetime, timedelta

# 从文件中读取 JSON 数据
def load_json_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# 生成日期范围内的日期
def generate_date_range(start_date, end_date):
    start = datetime.strptime(start_date, "%Y%m%d")
    end = datetime.strptime(end_date, "%Y%m%d")
    dates = []
    while start <= end:
        dates.append(start.strftime("%Y%m%d"))
        start += timedelta(days=1)
    return dates

# 计算缺失的日期
def find_missing_dates(data, start_date, end_date):
    all_dates = set(generate_date_range(start_date, end_date))
    present_dates = set(item['date'] for item in data)
    missing_dates = sorted(all_dates - present_dates)
    return missing_dates

# 文件名和日期范围
filename = 'bing_en-US.json'
start_date = "20190101"
end_date = "20240814"

# 读取 JSON 数据并查找缺失的日期
data = load_json_from_file(filename)
missing_dates = find_missing_dates(data, start_date, end_date)
print("Missing dates:", missing_dates)
