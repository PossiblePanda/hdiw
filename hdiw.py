from os import listdir
from os.path import isfile, join
from colorama import init, Fore
from argparse import ArgumentParser, Namespace

import utils
from classes.Results import Result, Results

parser = ArgumentParser()

parser.add_argument("dir", help="The directory of the program")

parser.add_argument("-v", action="store_true")
args: Namespace = parser.parse_args()

init()

results: Results = Results()

print(f"{Fore.GREEN}Gathering Info")

for f in utils.get_file_descendents(args.dir, args.v):
	if args.v:
		print(f"{Fore.LIGHTGREEN_EX}Gathering results for {Fore.GREEN}{f}{Fore.RESET}")

	# Godot
	if "godot" in f.file_name.lower():
		results.add_to_results("Godot", 100, "Game Engines")
	
	if f.file_name.endswith(".gd"):
		results.add_to_results("Godot", 90, "Game Engines")
	
	# Cocos2D
	if "cocos2d" in f.file_name.lower():
		results.add_to_results("Cocos2D", 100, "Game Engines")
	
	# Cocos2D
	if "love.exe" in f.file_name:
		results.add_to_results("Love Framework", 100, "Game Engines")

	# Unity
	if "MonoBleedingEdge" in f.file_name:
		results.add_to_results("Unity", 100, "Game Engines")
	
	
	if "UnityCrashHandler64" in f.file_name:
		results.add_to_results("Unity", 100, "Game Engines")
	
	if "UnityPlayer" in f.file_name:
		results.add_to_results("Unity", 100, "Game Engines")
	
	# Unreal Engine 4
	if "UE4" in f.file_name:
		results.add_to_results("Unreal Engine 4", 100, "Game Engines")
	
	# Ubisoft Anvil
	if f.file_name.endswith(".forge"):
		results.add_to_results("Ubisoft Anvil", 100, "Game Engines")
	
	# Source Engine
	if f.file_name.lower().endswith(".vpk"):
		results.add_to_results("Source Engine", 95, "Game Engines")
	
	# Python
	if f.file_name.lower().endswith(".py"):
		results.add_to_results("Python", 100, "Programming Languages")
	
	# C#
	if f.file_name.lower().endswith(".cs"):
		results.add_to_results("C#", 100, "Programming Languages")
	
	# C++
	if f.file_name.lower().endswith(".cpp"):
		results.add_to_results("C++", 100, "Programming Languages")

	# PHP
	if f.file_name.lower().endswith(".php"):
		results.add_to_results("PHP", 100, "Programming Languages")
	
	# Java
	if f.file_name.lower().endswith(".jar"):
		results.add_to_results("Java", 100, "Programming Languages")

	# LUA
	if f.file_name.lower().endswith(".lua"):
		results.add_to_results("Lua", 100, "Programming Languages")

	if f.file_name.lower().endswith(".luau"):
		results.add_to_results("Lua", 100, "Programming Languages")

	# Microsoft XNB
	if f.file_name.lower().endswith(".xnb"):
		results.add_to_results("Microsoft XNA", 80, "Game Engines")
	
	if "xnafx40_redist" in f.file_name:
		results.add_to_results("Microsoft XNA", 100, "Game Engines")
	
	# Steamworks API
	if "steam_api" in f.file_name:
		results.add_to_results("Steamworks API", 100, "APIs")
	
	# .NET
	if "dotnet" in f.file_name.lower():
		results.add_to_results(".NET Framework", 100, "APIs")

	# SQLite
	if "sqlite" in f.file_name.lower():
		results.add_to_results("SQLite", 100, "Databases")
	
	# EFT Themes
	if f.file_name.endswith(".eft"):
		results.add_to_results("EFT Themes", 100, "Other")
	
	# Shell Script
	if f.file_name.endswith(".sh"):
		results.add_to_results("Shell Script", 100, "Other")
	
	# EFT Themes
	if "ffmpeg" in f.file_name:
		results.add_to_results("FFMPEG", 100, "Other")

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
