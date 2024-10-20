import os
import shutil
import pandas as pd

# Load the smaller CSV file
# small_csv = pd.read_excel('/mnt/c/Users/user/Pictures/AI/research/scripts/filtered_merged_for_yes_no_and_count.xlsx')
small_csv = pd.read_excel('/mnt/c/Users/user/Pictures/AI/research/scripts/small_versions/like_DAQUAR/both/data_train.xlsx')

# Define the directory where the original images are stored
original_image_dir = '/mnt/e/train2014/train2014/'

# Define the directory where the filtered images will be copied
filtered_image_dir = '/mnt/c/Users/user/Pictures/AI/research/dataset_pro/images'

# Create the directory if it doesn't exist
os.makedirs(filtered_image_dir, exist_ok=True)

# Loop through each image_id in the CSV file
for image_id in small_csv['image_id']:
    # Construct the full image filename
    image_filename = f"{str(image_id)}"
    
    # Source path for the original image
    src_image_path = os.path.join(original_image_dir, image_filename)
    
    # Destination path for the filtered image
    dest_image_path = os.path.join(filtered_image_dir, image_filename)
    
    # Copy the image to the new directory if it exists
    if os.path.exists(src_image_path):
        shutil.copy(src_image_path, dest_image_path)
    else:
        print(src_image_path)
        print(f"Image {image_filename} not found in the source directory.")

print(f"Images have been filtered and copied to {filtered_image_dir}")
