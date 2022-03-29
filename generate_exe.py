import PyInstaller.__main__
import os
import shutil


PyInstaller.__main__.run([
    "--onedir",
    "--console",
    "--distpath", r"C:\Users\Slow\Desktop\pyinstall_test\dist",
    "--workpath", r"C:\Users\Slow\Desktop\pyinstall_test\build",
    "--specpath", r"C:\Users\Slow\Desktop\pyinstall_test",
    "--splash", r"C:\Users\Slow\Desktop\pyinstall_test\images\loadsoft.png",
    r"C:\Users\Slow\Desktop\pyinstall_test\main.py"
])

shutil.rmtree(r"C:\Users\Slow\Desktop\pyinstall_test\build")
os.remove(r"C:\Users\Slow\Desktop\pyinstall_test\main.spec")

