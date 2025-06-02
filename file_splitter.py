import os
import random

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

# copy
if not os.path.exists(COPY_DIR): os.makedirs(COPY_DIR)
if not os.path.exists(DIR_70PERCENT): os.makedirs(DIR_70PERCENT)
if not os.path.exists(os.path.join(DIR_70PERCENT, "images")): os.makedirs(os.path.join(DIR_70PERCENT, "images"))
if not os.path.exists(os.path.join(DIR_70PERCENT, "labels")): os.makedirs(os.path.join(DIR_70PERCENT, "labels"))
if not os.path.exists(DIR_20PERCENT): os.makedirs(DIR_20PERCENT)
if not os.path.exists(os.path.join(DIR_20PERCENT, "images")): os.makedirs(os.path.join(DIR_20PERCENT, "images"))
if not os.path.exists(os.path.join(DIR_20PERCENT, "labels")): os.makedirs(os.path.join(DIR_20PERCENT, "labels"))
if not os.path.exists(DIR_10PERCENT): os.makedirs(DIR_10PERCENT)
if not os.path.exists(os.path.join(DIR_10PERCENT, "images")): os.makedirs(os.path.join(DIR_10PERCENT, "images"))

## train copy 70P
print("Copying 70% . . .")
for image in IMAGES_70PERCENT:
    os.system(f"cp {os.path.join(IMAGES_DIR, image)} {os.path.join(DIR_70PERCENT, 'images', image)}")
    label_name = remove_extention_file_name(image)
    for label in LABELS_DIR_LIST:
        if remove_extention_file_name(label) == label_name:
            os.system(f"cp {os.path.join(LABELS_DIR, label)} {os.path.join(DIR_70PERCENT, 'labels', label)}")
print("Copyed")

## val copy 20P
print("Copying 20% . . .")
for image in IMAGES_20PERCENT:
    os.system(f"cp {os.path.join(IMAGES_DIR, image)} {os.path.join(DIR_20PERCENT, 'images', image)}")
    label_name = remove_extention_file_name(image)
    for label in LABELS_DIR_LIST:
        if remove_extention_file_name(label) == label_name:
            os.system(f"cp {os.path.join(LABELS_DIR, label)} {os.path.join(DIR_20PERCENT, 'labels', label)}")
print("Copyed")

## test copy 10P
print("Copying 10% . . .")
for image in IMAGES_10PERCENT:
    os.system(f"cp {os.path.join(IMAGES_DIR, image)} {os.path.join(DIR_10PERCENT, 'images', image)}")
print("Copyed")

## YAML 파일 생성
print("Creating YAML file . . .")
with open(YAML_FILE_NAME, "w") as yaml_file:
    yaml_file.write(YAML_DATA)
print("YAML file created")

print("Done!")
