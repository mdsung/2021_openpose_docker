#!/usr/bin/env python3
import pwd
import grp
import os
from pathlib import Path
from dotenv import load_dotenv

# Define Path
load_dotenv(verbose=True)
PROCESSED_DATA_PATH = Path(os.getenv('OUTPUT_DATA_PATH'))
USERNAME = 'suncheol'
GROUP = 'nia'

def read_folder_mp4_contents(path:Path):
    return path.glob('**/*.mp4')

def rename_file(file:Path):
    if "out" not in str(file):
        name = str(file).replace('.mp4', '_out.mp4')
        file.rename(name)

def chown_file(file:Path):
    uid = pwd.getpwnam(USERNAME).pw_uid
    gid = grp.getgrnam(GROUP).gr_gid
    os.chown(file, uid, gid)
    
def main():
    target_file_list = read_folder_mp4_contents(PROCESSED_DATA_PATH)
    for target_file in target_file_list:
        chown_file(target_file)
        rename_file(target_file)

if __name__ == '__main__':
    main()