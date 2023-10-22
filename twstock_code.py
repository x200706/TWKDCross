import os
import json
import twstock

f = twstock.codes
# 指定檔案路徑
file_path = 'code.txt'
# 建立空白檔案
open(file_path, 'w').close()
# 或者寫入內容到檔案中
with open(file_path, 'w', encoding='UTF-8') as file:
    file.write(json.dumps(f, ensure_ascii=False))