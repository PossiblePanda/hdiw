from os import listdir
from os.path import isfile, join
from colorama import init, Fore
from argparse import ArgumentParser, Namespace
import json
import time

import utils
from classes.Results import Result, Results

parser = ArgumentParser(epilog=f"Thanks for using HDIW! \nGitHub: {Fore.GREEN}https://github.com/possiblepanda/hdiw{Fore.RESET}")

parser.add_argument("path", help="The path of the program, Directory, or file.")

parser.add_argument("-v", "--verbose", action="store_true", help="Adds messages to indicate what is going on in the program")

parser.add_argument("-d", "--deep", action="store_true", help="Searches binaries for common technologies. May take longer to scan")

cfg: dict

start = time.time()

with open('main.json', 'r') as file:
	data = file.read()
	
	cfg = json.loads(data)


args: Namespace = parser.parse_args()

init()

results: Results = Results()

print(f"{Fore.GREEN}Gathering Info{Fore.RESET}")

ignore = []
try:
	with open(f'{args.path}\\hdiwignore.json', 'r') as file:
		data = file.read()
		
		load = json.loads(data)

		for l in load:
			ignore.append(f"{args.path}\\{l}")

except:
	if args.verbose:
		print(f"{Fore.YELLOW}No hdiwignore found, ignoring.{Fore.RESET}")

scanned = 0

for f in utils.get_file_descendents(args.path, args.verbose, ignore):
	scanned += 1
	if args.verbose:
		print(f"{Fore.LIGHTGREEN_EX}Gathering results for {Fore.GREEN}{f}{Fore.RESET}")
	
	
	for i in cfg["file-extension"].keys():
		v = cfg["file-extension"][i]

		if f.file_name.endswith(i):
			results.add_to_results(v["name"], v["chance"], v["category"])
	
	for i in cfg["name-contains"].keys():
		v = cfg["name-contains"][i]

		if i.lower() in f.file_name.lower():
			results.add_to_results(v["name"], v["chance"], v["category"])
	
	if args.deep:
		if f.file_name.endswith(".exe"):
			try:
				file = open(f.path, "rb")
				array = file.read()

				if args.verbose:
					print(f"{Fore.MAGENTA}Deep Searching {f.path}{Fore.RESET}")

				ansi: str = array.decode("ansi")
				
				for i in cfg["deep-contains"].keys():
					v = cfg["deep-contains"][i]

					if i in ansi:
						results.add_to_results(v["name"], v["chance"], v["category"])
			except:
				print(f"{Fore.LIGHTRED_EX}Unable to open {Fore.RED}{f.path}{Fore.RESET}")

print(f"{Fore.GREEN}Generating Results\n")

results_none_found: str = f"{Fore.RED}No results have been found!{Fore.RESET}"
if args.deep == False:
	results_none_found += f"\n{Fore.MAGENTA}Try running HDIW with the {Fore.LIGHTMAGENTA_EX}-h{Fore.MAGENTA} flag."

results_string: str = results_none_found

print(f"{Fore.YELLOW}------------Results------------{Fore.RESET}\n")

for i in results.results.keys():
	c = results.results[i]
	if results_string == results_none_found:
		results_string = f"{i}\n"
	else:
		results_string = f"{results_string}{i}\n"
	
	for i2 in results.results[i].keys():
		r = results.results[i][i2]
		result = Result(i2, r)

		results_string = f"{results_string} - {result.text}\n"

end = time.time()

print(f"""{Fore.LIGHTCYAN_EX}Time Elapsed: {Fore.BLUE}{round(end - start, 2)}s
{Fore.LIGHTCYAN_EX}Files Searched: {Fore.BLUE}{scanned}{Fore.RESET}
{Fore.LIGHTCYAN_EX}Results Found: {Fore.BLUE}{results.result_count}{Fore.RESET}\n""")

print(results_string)