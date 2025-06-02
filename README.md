# YOLO with Images 파일 분할기
train, val, test에 파일을 70%, 20%, 10% 나누는 작업을 자동으로 해주는 파이썬 코드입니다.<br>
파이썬 파일을 바로 실행하시면 됩니다.
```bash
python app.py
```
코드 내용을 자신의 환경에 맞게 설정 후 실행해주세요.

```python
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
```
