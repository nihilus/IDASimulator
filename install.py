#!/usr/bin/env python

import os
import sys
import shutil

python_dir = 'idasim'
plugin_file = 'idasimulator.py'
plugin_dir = 'idasimlib'

try:
	ida_directory = sys.argv[1]
except:
	print "Full path to your IDA install directory: ",
	ida_directory = sys.stdin.readline().strip()
	print ""

python_dir_path = os.path.join(ida_directory, 'python', python_dir)
plugin_file_path = os.path.join(ida_directory, 'plugins', plugin_file)
plugin_dir_path = os.path.join(ida_directory, 'plugins', plugin_dir)
plugin_src_dir_path = os.path.join('src', 'plugins', plugin_dir)

if not os.path.exists(plugin_dir_path):
	os.mkdir(plugin_dir_path)

if os.path.exists(python_dir_path):
	shutil.rmtree(python_dir_path)

shutil.copytree(os.path.join('src', 'python', python_dir), python_dir_path)
shutil.copyfile(os.path.join('src', 'plugins', plugin_file), plugin_file_path)

for file_name in os.listdir(plugin_src_dir_path):
	src = os.path.join(plugin_src_dir_path, file_name)
	dst = os.path.join(plugin_dir_path, file_name) 
	if not os.path.isdir(src):
		shutil.copyfile(src, dst)

print "IDASimulator installed to %s" % ida_directory

