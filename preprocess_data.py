import os, sys
from PIL import Image

RAW_DATA_DIR = os.path.join(os.getcwd(), 'raw_data')
PROCESSED_DATA_DIR = os.path.join(os.getcwd(), 'dataset')

if not os.path.exists(RAW_DATA_DIR):
    sys.exit(0)

if not os.path.exists(PROCESSED_DATA_DIR):
    os.makedirs(PROCESSED_DATA_DIR)

def resize_images():
    for root, dirs, files in os.walk(RAW_DATA_DIR):
        for dir in dirs:
            preprocessed_data_dir = os.path.join(PROCESSED_DATA_DIR, os.path.relpath(os.path.join(root, dir), RAW_DATA_DIR))
            if not os.path.exists(preprocessed_data_dir):
                os.makedirs(preprocessed_data_dir)

        for file in files:
            raw_file_path = os.path.join(root, file)
            preprocessed_file_path = os.path.join(PROCESSED_DATA_DIR, os.path.relpath(raw_file_path, RAW_DATA_DIR))
            preprocessed_file_path = os.path.splitext(preprocessed_file_path)[0] + '.png'
            try:
                with Image.open(raw_file_path) as img:
                    img = img.resize((256, 256), Image.LANCZOS)
                    img.save(preprocessed_file_path)
            except IOError:
                print("Error file not a photo. File skipped: ", file)
        
resize_images()