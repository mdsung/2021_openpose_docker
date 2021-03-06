#!/usr/bin/env python3

import subprocess
from pathlib import Path

CURRENT_PATH = Path(__file__)
RAW_DATA_PATH = Path('/data/processed/core/assembly/')
PROCESSED_DATA_PATH = Path('/data/processed/core/assembly_json/')
# RAW_DATA_PATH = Path('/home/nia_data/processed/core/assembly')
# PROCESSED_DATA_PATH = Path('/home/nia_data/processed/core/assembly_json')

def run_openpose(input_path, output_path, json_output_path, rendering=False):
    """
    command exmaple:
        /openpose/build/examples/openpose/openpose.bin --video /data/processed/core/assembly/B031/B031_GMS_1_1.mp4 --display 0 --hand --write_video /data/processed/core/assembly_skeletal/B031/B031_GMS_1_1_out.mp4 --write_json /data/processed/core/assembly_json/B031 --disable_blending
    """
    if rendering:
        cmd = f"/openpose/build/examples/openpose/openpose.bin --video '{input_path}' --display 0 --hand --write_json '{json_output_path}' --write_video '{output_path}' --disable_blending"
    else:
        cmd = f"/openpose/build/examples/openpose/openpose.bin --video '{input_path}' --display 0 --hand --write_json '{json_output_path}' --render_pose 0 --disable_blending"
        
    subprocess.run(cmd, shell = True)
    
def read_folder_contents(path:Path, extension:str):
    return path.glob(f'**/*.{extension}')

def create_output_folder(output_folder):
    output_folder.mkdir(parents=True, exist_ok=True)

def get_target_file_list(raw_mp4_list, processed_json_name_list):
    results = []
    for f in raw_mp4_list:
        if ((f.stem not in processed_json_name_list)):
            print(f.name[:12], f.name[5])
            results.append(f)
    
    return results

def get_json_output_folder(input_file:Path):
    patient_id = input_file.name[:4]
    json_output_path = Path(PROCESSED_DATA_PATH, patient_id)
    return json_output_path

def get_json_file_name_list(json_list):
    return list({"_".join(js.name.split("_")[:4]) for js in json_list})

def get_output_folder(input_file:Path):
    output_file_name = str(input_file).\
                            replace('assembly', 'assembly_skeletal').\
                            replace('.mp4', '_out.mp4')
    output_file = Path(output_file_name)
    create_output_folder(output_file.parent)
    return output_file

def main():
    raw_mp4_list = list(RAW_DATA_PATH.glob('**/*.mp4'))
    raw_MP4_list = list(RAW_DATA_PATH.glob('**/*.MP4'))
    raw_list = raw_mp4_list + raw_MP4_list
    raw_list = [f for f in raw_list if (f.name[5] == 'G') and (f.name.startswith('D'))]
    
    processed_json_list = PROCESSED_DATA_PATH.glob('**/*.json') 
    processed_json_name_list = get_json_file_name_list(processed_json_list)
    for f in raw_list:
        if f.stem not in processed_json_name_list:
            print(f)
            output_path = get_output_folder(f)
            json_output_path = get_json_output_folder(f)
            run_openpose(f, output_path, json_output_path)
    # target_mp4_list = get_target_file_list(raw_list, processed_json_name_list)
    # print(target_mp4_list)
    
    # for mp4_file in target_mp4_list:
    #     input_path = mp4_file
    #     output_path = get_output_folder(mp4_file)
    #     json_output_path = get_json_output_folder(mp4_file)
    #     # print(str(input_path),
    #     #       str(output_path), 
    #     #       str(json_output_path))
    #     # run_openpose(input_path, output_path, json_output_path)
        
if __name__ == '__main__':
    main()