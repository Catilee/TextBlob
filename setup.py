import sys
import os

import text

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

IS_PY3 = (sys.version_info[0] == 3)
try:
    MODULE = os.path.dirname(os.path.abspath(__file__))
except:
    MODULE = ""

PUBLISH = "python setup.py register sdist upload"
TEST = 'nosetests --verbosity 2'

if sys.argv[-1] == 'publish':
    os.system(PUBLISH)
    sys.exit()

if sys.argv[-1] == 'test':
    try:
        __import__('nose')
    except ImportError:
        print('nose required.')
        sys.exit(1)

    os.system(TEST)
    sys.exit()

# Install nltk 3.0 alpha
if IS_PY3:
    os.chdir(os.path.join(MODULE, 'nltk'))
    os.system('python setup.py install')
    os.chdir('..')

def cheeseshopify(rst):
    '''Since PyPI doesn't support the `code-block` or directive, this replaces
    all `code-block` directives with `::`.
    '''
    ret = rst.replace(".. code-block:: python", "::").replace(":code:", "")
    return ret

with open('README.rst') as fp:
    long_desc = cheeseshopify(fp.read())

setup(
    name='textblob',
    version=text.__version__,
    description='Simple, Pythonic text processing. Sentiment analysis, '
                'POS tagging, noun phrase parsing, and more.',
    long_description=long_desc,
    author='Steven Loria',
    author_email='sloria1@gmail.com',
    url='https://github.com/sloria/TextBlob',
    install_requires=['nltk'],
    packages=[
        'text',
        'nltk'
    ],
    package_data={
        "text": ["*.txt", "*.xml"],
    },
    license='MIT',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    tests_require=['nose'],
)
