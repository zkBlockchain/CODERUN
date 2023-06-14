import sys
from datetime import datetime


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")


def format_date(date):
    return datetime.strftime(date, "%Y-%m-%d")


def merge_intervals(intervals):
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def sort_params(items):
    param_1 = items[0]

    param_2 = 0
    if items[3] == 'COLD':
        param_2 = 1
    elif items[3] == 'OTHER':
        param_2 = 2

    param_3 = datetime.strptime(items[1], "%Y-%m-%d").timestamp()
    
    return param_1, param_2, param_3


def main():
    warehouses = {}
    for line in sys.stdin:

        if line.strip() == "":
            break

        row = line.strip().split(',')     
        warehouse_id = int(row[0])
        start_date, end_date = map(str, row[1].split())
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)
        product_type = row[2]

        if product_type == "NULL":
            product_types = ["KGT", "COLD", "OTHER"]
        else:
            product_types = [product_type]

        for p_type in product_types:
            if (warehouse_id, p_type) not in warehouses:
                warehouses[(warehouse_id, p_type)] = []
            warehouses[(warehouse_id, p_type)].append((start_date, end_date))

    merged_records = []
    for (warehouse_id, product_type), intervals in sorted(warehouses.items()):
        merged_intervals = merge_intervals(intervals)
        for start, end in merged_intervals:
            merged_records.append([warehouse_id, format_date(start), format_date(end), product_type])

    sorted_records = sorted(merged_records, key=sort_params)

    for item in sorted_records:
        print(str(item[0]) + ',' + str(item[1]) + " " + str(item[2]) + "," + str(item[3]))


if __name__ == '__main__':
    main()
