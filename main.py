import os


file_list = []
for root, dirs, files in os.walk("."):
  for file in files:
    if file.endswith(".txt") and file != 'result.txt':
      file_list.append(file)


records = []
for name in file_list:
    with open(name, encoding='utf-8') as file:
        lines = file.readlines()
        quantity = len(lines)
        records.append([name, quantity, ''.join(lines)])
records.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as file:
    for item in records:
        file.write(item[0]+'\n')
        file.write(str(item[1])+'\n')
        file.write(item[2]+'\n')
