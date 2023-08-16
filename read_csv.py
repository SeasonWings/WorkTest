import csv

def split_list(lst, batch_size):
    for i in range(0, len(lst), batch_size):
        batch = lst[i:i+batch_size]
        print(batch)

# 从CSV文件中读取数据并存储到列表中
my_list = []
with open('fyx_chinamoney.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        my_list.extend(row)

# 将列表按照80个为一批进行拆分并打印输出
split_list(my_list, 80)