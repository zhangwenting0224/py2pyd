#!/usr/bin/python3.7.8
# -*- coding: utf-8 -*-
import PyInstaller.__main__
import os
import shutil

# 1 --hidden-import不用涵盖python内置模块

PROJECTPATH = r"C:\Users\30818\Desktop\pyd_mobile_flashwork"
DISTPATH = os.path.join(PROJECTPATH, 'dist')
BUILDPATH = os.path.join(PROJECTPATH, 'build')
IMAGESPATH = os.path.join(PROJECTPATH, 'images')

if os.path.exists(DISTPATH):
    print('移除源文件')
    shutil.rmtree(DISTPATH)
try:
    PyInstaller.__main__.run([
        "--onedir",
        "--windowed",
        "--clean",
        "-i", os.path.join(IMAGESPATH, 'buoy.ico'),
        "--distpath", DISTPATH,
        "--workpath", BUILDPATH,
        "--specpath", PROJECTPATH,
        "--hidden-import=PySimpleGUI",
        "--hidden-import=logzero",
        "--hidden-import=requests",
        "--hidden-import=uiautomator2",
        "--hidden-import=adbutils",
        "--hidden-import=xmltodict",
        "--hidden-import=uiautomator2",
        "--hidden-import=playsound",
        os.path.join(PROJECTPATH, "main.py")
    ])
except Exception as err:
    print(str(err))
finally:
    print('清理工作目录和spec文件')
    shutil.rmtree(BUILDPATH)
    os.remove(os.path.join(PROJECTPATH, "main.spec"))

