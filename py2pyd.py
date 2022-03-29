# !/usr/bin/python3.7.8
# -*- coding: utf-8 -*-
# @Date: 2022/3/27 17:42
import os
import distutils.core
import distutils.extension
import Cython.Build
import shutil


def py2pyd(path):

    file_list = []
    for root, dirs, files in os.walk(path, topdown=False):
        if files:
            for file in files:
                if os.path.splitext(file)[-1] != '.py':
                    continue

                if file not in exclude_filename:
                    file_list.append(os.path.join(root, file))

    for file in file_list:
        # 切换目录
        file_info = os.path.split(file)
        file_dir = file_info[0]
        file_name = file_info[1]
        os.chdir(file_dir)

        # 打包文件
        module_name = os.path.splitext(file_name)[0]
        extensions = [distutils.extension.Extension(module_name, [file_name])]
        distutils.core.setup(name=module_name, ext_modules=Cython.Build.cythonize(extensions))

        # 重命名
        src = module_name + '.cp37-win_amd64.pyd'
        dst = module_name + '.pyd'
        os.rename(src, dst)

        # 清理后缀
        for ext in ('c', 'pyc', 'py'):
            file = f"{module_name}.{ext}"
            os.path.isfile(file) and os.remove(file)

    clean_build(path)


def clean_build(path):

    build_paths = []
    for root, dirs, files in os.walk(path):
        if dirs:
            if 'build' in dirs:
                build_paths.append(os.path.join(root, 'build'))

    for build_path in build_paths:
        shutil.rmtree(build_path)


if __name__ == '__main__':
    # 1 复制文件到新目录中
    # 2 删除多余文件
    # 3 需要在cmd中执行该脚本
    # python py2pyd.py build_ext --inplace

    # 排除不打包的文件
    exclude_filename = [
        'setup.py',
        'main.py',
        '__init__.py',
    ]

    file_path = 'C:\\Users\\30818\\Desktop\\pyd_mobile_flashwork'
    py2pyd(file_path)
