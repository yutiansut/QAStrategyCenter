import codecs
import io
import os
import re
import sys
import platform

try:
    from setuptools import setup
except:
    from distutils.core import setup
"""
打包的用的setup必须引入，
"""

if sys.version_info.major != 3 or sys.version_info.minor not in [4, 5, 6, 7, 8]:
    print('wrong version, should be 3.4/3.5/3.6/3.7/3.8 version')
    sys.exit()


def read(fname):

    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


NAME = "QAStrategyCenter"
"""
名字，一般放你包的名字即可
"""
PACKAGES = ['QAStrategyCenter','QAStrategyCenter.Template','QAStrategyCenter.Loader']

DESCRIPTION = "QAStrategyCenter"


"""
参见read方法说明
"""

KEYWORDS = ["quantaxis", "quant", "finance", "Backtest", 'Framework']
"""
关于当前包的一些关键字，方便PyPI进行分类。
"""

AUTHOR_EMAIL = "yutiansut@qq.com"

URL = "https://github.com/yutiansut/QAStrategyCenter"


LICENSE = "MIT"

setup(
    name=NAME,
    version='1.0',
    description=DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    install_requires=['QUANTAXIS', 'jinja2',
                      'QACEPEngine', 'quantaxis_rank', 'quantaxis_pubsub'],
    entry_points={
        'console_scripts': [
            'QASC_Loader = QAStrategyCenter.Loader.fileloader:load_from_file'
        ]
    },
    # install_requires=requirements,
    keywords=KEYWORDS,
    author='yutiansut',
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True
)