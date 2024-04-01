import os
from colorama import Fore
from classes.File import *

def get_file_descendents(path, verbose, ignore, root=True):
	files = [File(path)]

	if not os.path.isdir(path):
		if root:
			return files

	for f in os.listdir(path):
		global_path: str = f"{path}\\{f}"
		if verbose:
			print(f"{Fore.LIGHTGREEN_EX}Gathering directories for {Fore.GREEN}{global_path}{Fore.RESET}")
		try:
			files.append(File(global_path))
			if os.path.isdir(global_path):
				for v in get_file_descendents(global_path, verbose, ignore, False):
					for i in ignore:
						if i != global_path:
							files.append(v)
		except:
			print(f"{Fore.LIGHTRED_EX}Failed to open {Fore.RED}{global_path}")
	return files