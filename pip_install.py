import subprocess
import sys

# package = 'Pygame'
# subprocess.check_call([sys.executable,'-m','pip','install',package])

packages_to_install = ['Numpy','Pandas','Matplotlib','Flask','Kivy','Panda3D','Pillow','PyQt5','Pygame','','','','','']

for package in packages_to_install:
    subprocess.check_call([sys.executable,'-m','pip','install',package])

# import pip
# def install(package):
#     pip.main(['install',package])
# install(Pygame)
