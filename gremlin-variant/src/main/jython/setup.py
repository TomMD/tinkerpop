'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''
import os
import time
import codecs

from setuptools import setup

# Folder containing the setup.py
root = os.path.dirname(os.path.abspath(__file__))

# Path to __version__ module
version_file = os.path.join(root, '.', '__version__.py')

# Check if this is a source distribution.
# If not create the __version__ module containing the version
if not os.path.exists(os.path.join(root, 'PKG-INFO')):
    timestamp = int(os.getenv('TIMESTAMP', time.time() * 1000)) / 1000
    fd = codecs.open(version_file, 'w', 'utf-8')
    fd.write('version   = %r\n' % os.getenv('VERSION', '?').replace('-SNAPSHOT', '.dev-%d' % timestamp))
    fd.write('timestamp = %d\n' % timestamp)
    fd.close()
# Load version
exec(open(version_file).read())

setup(
    name='gremlinpython',
    version=version,
    packages=['gremlin_driver','gremlin_python', 'gremlin_rest_driver'],
    license='Apache 2',
    url='http://tinkerpop.apache.org',
    description='Gremlin Language Variant for Apache TinkerPop - Gremlin',
    long_description=open("README").read(),
    install_requires=[
        'aenum'
    ]
)
