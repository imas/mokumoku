import shutil
import os
import sys


def replase_number(path_name, dir_name):
    files = ['/slide.md', '/kpt.md', '/p.md']
    for file in files:
        file_name = path_name + file
        with open(file_name) as f:
            data_lines = f.read()
        data_lines = data_lines.replace("XXX", dir_name)
        with open(file_name, mode="w") as f:
            f.write(data_lines)
    pass


def zero_padding(num):
    return('{0:03d}'.format(num))


def create_meetup_dir(argvs):
    path_name = './meetups/kanto/'
    if len(argvs) >= 2:
        new_dir_name = argvs[1]
        shutil.copytree(path_name + "templates", path_name + argvs[1])
    else:
        current_dir_list = sorted(os.listdir(path_name), reverse=True)
        new_dir_name = zero_padding(int(current_dir_list[:2][1]) + 1)
        shutil.copytree(path_name + "templates", path_name + new_dir_name)
    new_path_name = path_name + new_dir_name
    replase_number(new_path_name, new_dir_name)
    print(new_path_name + ' was created!')
    pass


argvs = sys.argv
create_meetup_dir(argvs)
