import zipfile
import os
import re
import hashlib
import requests

directory_to_extract_to = os.path.dirname(os.path.abspath('main.py'))+'//extract'
arch_file = os.path.join(os.path.dirname(os.path.abspath('main.py')), "tiff-4.2.0_lab1.zip")
zip_file = zipfile.ZipFile(arch_file)
zip_file.extractall(directory_to_extract_to)

txt_files = []

for r, _, f in os.walk(directory_to_extract_to):
    for file in f:
        if re.search(r"\.txt", file):
            txt_files.append(os.path.join(r, file))

hashes_files = []
for file in txt_files:
    with open(file, "rb") as file_data:
        print(file + ' ' + hashlib.md5(file_data.read()).hexdigest())

sh_files = []
for r, _, f in os.walk(directory_to_extract_to):
    for file in f:
        if re.search(r"\.sh", file):
            sh_files.append(os.path.join(r, file))

for file in sh_files:
    with open(file, "rb") as file_data:
        hashes_files.append(hashlib.md5(file_data.read()).hexdigest())

fhs = "4636f9ae9fef12ebd56cd39586d33cfb"

count = 0
for hs in hashes_files:
    if hs == fhs:
        with open(sh_files[count], "r") as file_data:
            print(sh_files[count] + ' ' + file_data.read())
        break
    count += 1

with open(sh_files[count], "r") as file_data:
    r = requests.get(file_data.read())
result_dct = {}
headers = []
first_iteration = True

lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)
for line in lines:
    if first_iteration:
        for i in re.split(r",+", re.sub("<.*?>", ",", line)):
            if i != '':
                headers.append(i)
        first_iteration = False
        continue
    line = re.sub("<.*?>", " ", line)  # убираем <...>
    line = re.sub(r"\(.*?\)", " ", line)  # убираем (0-9)
    line = re.sub(r"[^\w’\-—«»]", ";", line)
    tmp = re.split(r";{2,}", line)
    tokens = []
    for i in tmp:
        if i == '':
            continue
        tokens.append(re.sub(";", " ", i))
    result_dct.update({tokens[0]: (tokens[1], tokens[2], tokens[3], tokens[4])})

with open("table.csv", "w") as f:
    for i in headers:
        f.write(i+';')
    for key, values in result_dct.items():
        f.write("\n")
        f.write(key+';'+values[0]+';'+values[1]+';'+values[2]+';'+values[3])

while True:
    t_c = input("Введите название страны(esc для выхода): ")
    if t_c == 'esc':
        break
    print("(Страна); ", end='')
    for i in headers:
        print('(' + i + ')' + '; ', end='')
    print('\n'+t_c+';\t'+result_dct[t_c][0]+';\t'+result_dct[t_c][1]+';\t'+result_dct[t_c][2]+';\t'+result_dct[t_c][3])
