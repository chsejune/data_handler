__author__ = 'Sejune Cheon'

import os

input_path = 'datasets'
output_path = 'datasets2'


os.rename('path/original_file_name', 'path/renaming_file_name')
# if path is different, the file will be moved to the renaming path
# 1st argument is the source path and name, 2nd argument is the target path and name