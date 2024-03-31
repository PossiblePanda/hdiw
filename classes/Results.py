from colorama import Fore
import json

name_colors = {}

with open('main.json', 'r') as file:
	data = file.read()
	
	name_colors = json.loads(data)["name-colors"]

	for i in name_colors.keys():
		v = name_colors[i]
		
		name_colors[i] = getattr(Fore, v)


class Result:
	def __init__(self, name:str, chance:int) -> None:
		self.name, self.chance = name, chance

		# Set Text
		color: str = Fore.RED
		if chance >= 100:
			color = Fore.BLUE
		elif chance >= 75:
			color = Fore.GREEN
		elif chance >= 60:
			color = Fore.YELLOW
		
		self.text = f"{name_colors[name.lower()]}{name}{Fore.WHITE}: {color}{chance}%{Fore.RESET}"
	
	def __repr__(self) -> str:
		return self.text

class Results:
	def __init__(self) -> None:
		self.results = {}

	def add_to_results(self, name: str, value: int, category: str = "Other"):
		if category in self.results:
			if name in self.results[category]:
				if value > self.results[category][name]:
					self.results[category][name] = value
			else:
				self.results[category][name] = value
		else:
			self.results[category] = {name: value}
		