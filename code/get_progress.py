#!/usr/bin/env python3
import os
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

# Define Path
load_dotenv(verbose=True)
try:
    PROJECT_PATH = Path(__file__).parents[1]
except NameError:
    PROJECT_PATH = Path('.').absolute().parents[0]
RAW_DATA_PATH = Path(os.getenv('RAW_DATA_PATH'))
OUTPUT_DATA_PATH = Path(os.getenv('OUTPUT_DATA_PATH'))
JSON_DATA_PATH = Path(os.getenv('JSON_DATA_PATH'))

def read_folder_contents(path:Path, extension:str)->list:
    return path.glob(f'**/*.{extension}')

def get_json_file_name_list(json_list)->list:
    return list({"_".join(js.name.split("_")[:4]) for js in json_list})

def make_csv(raw, processed)->pd.DataFrame:
    raw_df = pd.DataFrame({'file': raw, 'raw' : 1})
    processed_df = pd.DataFrame({'file': processed, 'processed' : 1})
    return pd.merge(raw_df, processed_df, on = ['file'], how = 'left')\
            .sort_values('file')\
            .reset_index(drop = True)\
            .fillna(0)\
            .astype({'raw':'int8', 'processed':'int8'})
    
def write_to_csv(df:pd.DataFrame):
    df.to_csv(Path(PROJECT_PATH,'current_json_list.csv'), index = False)
    
def calculate_progress(df:pd.DataFrame):
    count_raw = df['raw'].sum() 
    count_processed = df['processed'].sum()
    print (f"Progress: {count_processed:3d}/{count_raw:3d} ({count_processed/count_raw*100:.3f}%)")

def main():
    raw_mp4_list = read_folder_contents(RAW_DATA_PATH, 'mp4')
    raw_mp4_name_list = [f.stem for f in raw_mp4_list if "out" not in f.stem]
    processed_json_list = read_folder_contents(JSON_DATA_PATH, 'json')
    processed_json_name_list = get_json_file_name_list(processed_json_list)
    csv_content = make_csv(raw_mp4_name_list, processed_json_name_list)
    write_to_csv(csv_content)
    calculate_progress(csv_content)
            
if __name__ == '__main__':
    main()