#!/usr/bin/python3

import glob
import os
import sys
import zipfile

def package_dir(base_dir, target_file):
    dir_list = [''] # local path in base_dir
    with zipfile.ZipFile(target_file, 'w') as zip:
        while len(dir_list) > 0:
            local_dir_path = dir_list.pop(0)
            dir_path = os.path.join(base_dir, local_dir_path)
            for p in os.listdir(dir_path):
                p_path = os.path.join(dir_path, p)
                p_local_path = os.path.join(local_dir_path, p)
                if os.path.isfile(p_path):
                    with open(p_path, 'rb') as f:
                        content = f.read()
                    zip.writestr(zipfile.ZipInfo(p_local_path), content)
                elif os.path.isdir(p_path):
                    dir_list.append(p_local_path)
                else:
                    print('Ignoring {} in {}'.format(p_local_path, base_dir))

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    for p in glob.glob('./*/autorun.py'):
        dir_path = os.path.dirname(p)
        print("Creating new archive {}.rpe for extension in {}".format(dir_path, dir_path))
        package_dir(dir_path, os.path.join('..', 'game', "{}.rpe".format(dir_path)))
