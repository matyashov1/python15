import os
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent'])

def get_file_info(path):
    file_info_list = []
    parent_dir = os.path.basename(os.path.normpath(path))
    
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            file_info_list.append(FileInfo(entry, None, True, parent_dir))
        else:
            name, extension = os.path.splitext(entry)
            file_info_list.append(FileInfo(name, extension, False, parent_dir))
    
    return file_info_list

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        return

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
        return

    file_info_list = get_file_info(directory_path)
    for file_info in file_info_list:
        print(file_info)

if __name__ == "__main__":
    main()
