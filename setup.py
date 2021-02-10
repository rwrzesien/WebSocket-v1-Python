#!/usr/bin/env python3
from setuptools import setup


setup(
    name='WebSocketV1Python',
    version='0.1',
    url='https://github.com/rwrzesien/Websocket-v1-Python',
    maintainer='',
    maintainer_email='',
    packages=[
        'cf_websocket',
        'cf_websocket.util'
    ],
    package_data={},
    include_package_data=True,
    python_requires='>=3.6',
)

