import os
from pathlib import Path

user = "YOU"
BRATS_TRAIN_FOLDERS = "/content/drive/MyDrive/BraTS2020/TRAIN"
BRATS_VAL_FOLDER = "/content/drive/MyDrive/BraTS2020/VAL"
BRATS_TEST_FOLDER = "/content/drive/MyDrive/BraTS2020/TEST"


def get_brats_folder(on="val"):
    if on == "train":
        return os.environ['BRATS_FOLDERS'] if 'BRATS_FOLDERS' in os.environ else BRATS_TRAIN_FOLDERS
    elif on == "val":
        return os.environ['BRATS_VAL_FOLDER'] if 'BRATS_VAL_FOLDER' in os.environ else BRATS_VAL_FOLDER
    elif on == "test":
        return os.environ['BRATS_TEST_FOLDER'] if 'BRATS_TEST_FOLDER' in os.environ else BRATS_TEST_FOLDER
