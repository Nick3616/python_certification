from collections import namedtuple
import os
import logging
import sys


FileInfo = namedtuple('FileInfo', 'name extension is_directory parent_directory')

logging.basicConfig(filename='directory_contents.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def collect_directory_info(directory_path):
    for root, dirs, files in os.walk(directory_path):
        parent_directory = os.path.basename(root)
        for dir_name in dirs:
            dir_info = FileInfo(name=dir_name, extension=None, is_directory=True, parent_directory=parent_directory)
            logging.info(dir_info)
        
        for file_name in files:
            name, extension = os.path.splitext(file_name)
            file_info = FileInfo(name=name, extension=extension, is_directory=False, parent_directory=parent_directory)
            logging.info(file_info)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: Task_1.py <путь_к_директории>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print(f"Указанный путь '{directory_path}' не является каталогом.")
        sys.exit(1)

    collect_directory_info(directory_path)

# Пример ввода python task_1.py 'D:/'
