#!/usr/bin/env python3

import subprocess
from pathlib import Path

CURRENT_PATH = Path(__file__)
RAW_DATA_PATH = Path('/data/processed/core/assembly/')
PROCESSED_DATA_PATH = Path('/data/processed/core/assembly_skeletal/')
# RAW_DATA_PATH = Path('/home/nia_data/processed/core/assembly/')
# PROCESSED_DATA_PATH = Path('/home/nia_data/processed/core/assembly_skeletal/')

EXCEPT_PATH = ['B001', 'D002']

def run_openpose(input_path, output_path):
    """
    /openpose/build/examples/openpose/openpose.bin --video /data/processed/core/assembly/B031/B031_GMS_1_1.mp4 --display 0 --hand --write_video /data/processed/core/assembly_skeletal/B031/B031_GMS_1_1_out.mp4
    """
    cmd = f"/openpose/build/examples/openpose/openpose.bin --video '{input_path}' --display 0 --hand  --write_video '{output_path}'"
    subprocess.run(cmd, shell = True)
    
def read_folder_mp4_contents(path:Path):
    return path.glob('**/*.mp4')

def create_output_folder(output_folder):
    output_folder.mkdir(parents=True, exist_ok=True)
    
def get_output_folder(input_file:Path):
    output_file_name = str(input_file).\
                            replace('assembly', 'assembly_skeletal').\
                            replace('.mp4', '_out.mp4')
    output_file = Path(output_file_name)
    create_output_folder(output_file.parent)
    return output_file

def main():
    raw_mp4_list = read_folder_mp4_contents(RAW_DATA_PATH)
    processed_mp4_list = read_folder_mp4_contents(PROCESSED_DATA_PATH)
    processed_mp4_name_list = [mp4_file.name.replace('_out','') for mp4_file in processed_mp4_list]
    target_mp4_list = [f for f in raw_mp4_list if f.name not in processed_mp4_name_list]

    for mp4_file in target_mp4_list:
        if "B001" in str(mp4_file):
            continue
        if "D002" in str(mp4_file):
            continue
        input_path = mp4_file
        output_path = get_output_folder(mp4_file)
        run_openpose(input_path, output_path)
        
if __name__ == '__main__':
    main()