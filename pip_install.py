import subprocess
import sys

packages_to_install = ['Numpy','Pandas','Matplotlib','Flask','Kivy','Panda3D','Pillow','PyQt5','Pygame','pytesseract','pyttsx3','playsound','SciPy','Seaborn','statsmodels','plotly','bokeh','scikit-learn','Requests','HTTPX','Retrying','Celery','Dramatiq','TensorFlow','Keras','PyTorch','Pymorphy2','Pymystem3','OpenCV','rich','loguru','pydantic','dateparser','Py-spy','Pympler','Responses','Freezegun','Faker','Factory_boy','Funcy','tqdm','black',]

for package in packages_to_install:
    subprocess.check_call([sys.executable,'-m','pip','install',package])

# msiexec /a python-3.6.msi TARGETDIR=r: \python36 ALLUSERS=1
# subprocess.check_call([sys.executable,'-m','pip','install',package])

#########################################
# import pip
# def install(package):
#     pip.main(['install',package])
# install(Pygame)
