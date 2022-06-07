import os

def watch_file_update(path):
  timestamp = os.stat(path).st_mtime
  while 1:
    if timestamp != os.stat(path).st_mtime:
      timestamp = os.stat(path).st_mtime
      print('Файл изменён!')

watch_file_update("/home/roman/test/temp.json")