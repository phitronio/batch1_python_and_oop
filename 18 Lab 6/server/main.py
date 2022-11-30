""" object processor.
 A demonstration of event driven programming.
 This is an example of a large system or a micro-saas itself.

 Always comment your code, and put your signature. 

 author: ashraf minhaj
 (c) Programming Hero
"""

import glob
import shutil
import os

source_path = '../source/*'
destination_path = '../destination'

postfix = [1, 2, 3]

while True:
    source_object = glob.glob(source_path)
    # print(source_object)

    if len(source_object) > 0:

        object_path = source_object[0]
        shutil.copy(object_path, '.')
        print(object_path)

        object_name = object_path.split('/')[-1].split('.')
        prefix = object_name[0]
        postfix2 = object_name[1]
        # print(object_name)
        # print(type(object_name))

        for item in range(len(postfix)):
            filename = prefix + '_' + str(item) + '.' + postfix2
            print(filename)
            shutil.copy(object_path, f"{destination_path}/{filename}")

        os.remove(object_path)
        os.remove(object_path.split('/')[-1])