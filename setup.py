from setuptools import setup


setup(
    name='gagaframe',
    version='0.1',
    description='An attempt at a fun picture digital frame made with pygame',
    url='https://github.com/Gagaro/gagaframe',
    author='Gagaro',
    author_email='gagaro42@gmail.com',
    license='MIT',
    packages=['gagaframe'],
    install_requires=[
        'pygame',
    ],
    zip_safe=False
)
