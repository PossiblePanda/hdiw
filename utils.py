import os
from classes.File import *

def get_file_descendents(path):
	files = [File(path)]
	for f in os.listdir(path):
		global_path: str = f"{path}\\{f}"

		files.append(File(global_path))
		if os.path.isdir(global_path):
			for v in get_file_descendents(global_path):
				files.append(v)
	return files