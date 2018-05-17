import re
import io
from setuptools import setup
from setuptools.extension import Extension

__version__ = "0.3.9.0"

setup(
    author="nyanye",  # Original wordcloud author: Andreas Mueller t3kcit+wordcloud@gmail.com
    author_email="iam@nyanye.com", 
    name='goorm',
    version=__version__,
    url='https://github.com/koshort/goorm',
    description='A little word cloud generator wrapper with Korean support',
    license='MIT',
    install_requires=['matplotlib', 'numpy>=1.6.1', 'pillow', 'eunjeon'],
    ext_modules=[Extension("goorm.query_integral_image",
                           ["goorm/query_integral_image.c"])],
    packages=['goorm'],
    package_data={'goorm': ['stopwords', 'NanumBarunGothic.ttf']}
)
