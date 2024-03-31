from os import listdir
from os.path import isfile, join
from colorama import init, Fore
from argparse import ArgumentParser, Namespace
import json

import utils
from classes.Results import Result, Results

parser = ArgumentParser(epilog=f"Thanks for using HDIW! \nGitHub: {Fore.GREEN}https://github.com/possiblepanda/hdiw{Fore.RESET}")

parser.add_argument("dir", help="The directory of the program")

parser.add_argument("-v", action="store_true", help="Adds messages to indicate what is going on in the program")

cfg: dict

with open('main.json', 'r') as file:
	data = file.read()
	
	cfg = json.loads(data)


args: Namespace = parser.parse_args()

init()

results: Results = Results()

print(f"{Fore.GREEN}Gathering Info")

for f in utils.get_file_descendents(args.dir, args.v):
	if args.v:
		print(f"{Fore.LIGHTGREEN_EX}Gathering results for {Fore.GREEN}{f}{Fore.RESET}")
	
	
	for i in cfg["file-extension"].keys():
		v = cfg["file-extension"][i]

		if f.file_name.endswith(i):
			results.add_to_results(v["name"], v["chance"], v["category"])
	
	for i in cfg["name-contains"].keys():
		v = cfg["name-contains"][i]

		if i.lower() in f.file_name.lower():
			results.add_to_results(v["name"], v["chance"], v["category"])


print(f"{Fore.GREEN}Generating Results\n")

results_none_found: str = f"{Fore.RED}No results have been found!{Fore.RESET}"
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

print(results_string)
