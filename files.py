import os

def get_files(root_dir, filter=None):
    
    if filter is None:
        filter = ''
    return [ os.path.join(root_dir, y) for y in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, y)) and y.find(filter)!= -1]

def get_dirs(root_dir, filter=None):

    if filter is None:
        filter = ''
    return [ os.path.join(root_dir, y) for y in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, y)) and y.find(filter)!= -1]


def get_file_name(file_path):
    if os.path.isfile(file_path):
        return file_path.split('/')[-1]
    else:
        return None