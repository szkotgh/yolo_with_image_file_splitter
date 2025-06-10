import os
import random
import shutil

# YOLO Export with image 파일 경로 설정
## Zip 폴더 경로(images, labels가 있는 폴더 경로)
ORIGINAL_DIR = "./"
IMAGES_DIR = os.path.join(ORIGINAL_DIR, "images")
LABELS_DIR = os.path.join(ORIGINAL_DIR, "labels")
# 내보낼 폴더 경로
COPY_DIR = "Project"
## 70%, 20%, 10%로 나누어 저장할 폴더 경로(수정불필요)
DIR_70PERCENT = os.path.join(COPY_DIR, "train")
DIR_20PERCENT = os.path.join(COPY_DIR, "val")
DIR_10PERCENT = os.path.join(COPY_DIR, "test")
YAML_FILE_NAME = os.path.join(COPY_DIR, "data.yaml")
## YAML 파일 내용(수정 필요)
YAML_DATA = '''
train: /content/dataset/train/images val: /content/dataset/val/images test: /content/dataset/test/images
nc: 3
names: ['can', 'plastic', 'styrofoam']
'''

def remove_extention_file_name(file_name):
    return os.path.splitext(file_name)[0]

def get_directory_files(directory):
    if not os.path.exists(directory):
        return []
    return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

IMAGES_DIR_LIST = get_directory_files(IMAGES_DIR)
random.shuffle(IMAGES_DIR_LIST)
LABELS_DIR_LIST = get_directory_files(LABELS_DIR)

IMAGES_70PERCENT = IMAGES_DIR_LIST[:int(len(IMAGES_DIR_LIST) * 0.7)]
IMAGES_20PERCENT = IMAGES_DIR_LIST[int(len(IMAGES_DIR_LIST) * 0.7):int(len(IMAGES_DIR_LIST) * 0.9)]
IMAGES_10PERCENT = IMAGES_DIR_LIST[int(len(IMAGES_DIR_LIST) * 0.9):]

def make_dirs(path):
    os.makedirs(os.path.join(path, "images"), exist_ok=True)
    os.makedirs(os.path.join(path, "labels"), exist_ok=True)

make_dirs(DIR_70PERCENT)
make_dirs(DIR_20PERCENT)
make_dirs(DIR_10PERCENT)

def copy_image_and_label(image_list, dest_dir):
    for image in image_list:
        image_path = os.path.join(IMAGES_DIR, image)
        label_name = remove_extention_file_name(image)
        label_path = None
        for label in LABELS_DIR_LIST:
            if remove_extention_file_name(label) == label_name:
                label_path = os.path.join(LABELS_DIR, label)
                break
        shutil.copy(image_path, os.path.join(dest_dir, "images", image))
        if label_path:
            shutil.copy(label_path, os.path.join(dest_dir, "labels", os.path.basename(label_path)))

print("Copying 70% . . .")
copy_image_and_label(IMAGES_70PERCENT, DIR_70PERCENT)
print("Copied")

print("Copying 20% . . .")
copy_image_and_label(IMAGES_20PERCENT, DIR_20PERCENT)
print("Copied")

print("Copying 10% . . .")
for image in IMAGES_10PERCENT:
    image_path = os.path.join(IMAGES_DIR, image)
    shutil.copy(image_path, os.path.join(DIR_10PERCENT, "images", image))
print("Copied")

print("Creating YAML file . . .")
with open(YAML_FILE_NAME, "w") as yaml_file:
    yaml_file.write(YAML_DATA)
print("YAML file created")

print("Done!")
