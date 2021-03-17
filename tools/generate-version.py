#!/usr/bin/env python
'''
 * Copyright (c) 2018 Spotify AB.
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
'''

from __future__ import print_function

import os
import subprocess
import sys


def main():
    output_dir = os.path.join(os.path.join('build', 'output'))
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print('Generating nfdriver_generated_header.h in ' + output_dir)
    generated_header_filename = os.path.join(output_dir, 'nfdriver_generated_header.h')
    generated_header = open(generated_header_filename, 'w')
    generated_header.write('// This is a generated header from generate-version.py\n')
    cwd = os.getcwd()
    git_count = subprocess.check_output(['git', 'rev-list', '--count', 'HEAD'], cwd = cwd).decode()
    git_describe = subprocess.check_output(['git', 'describe', '--always'], cwd = cwd).decode()
    generated_header.write('#define NFDRIVER_VERSION "' + str(git_count.strip()) + '-' + str(git_describe.strip()) + '"\n')


if __name__ == "__main__":
    main()
