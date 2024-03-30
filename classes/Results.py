from colorama import Fore

name_colors = {
	"godot": Fore.CYAN,
	"unity": Fore.LIGHTBLACK_EX,
	"cocos2d": Fore.BLUE,
	"steamworks api": Fore.LIGHTCYAN_EX,
	"microsoft xna": Fore.GREEN,
	".net framework": Fore.MAGENTA,
	"eft themes": Fore.LIGHTGREEN_EX,
	"python": Fore.YELLOW,
	"c#": Fore.LIGHTYELLOW_EX,
	"c++": Fore.LIGHTBLACK_EX,
	"java": Fore.LIGHTRED_EX,
	"source engine": Fore.LIGHTRED_EX,
	"sqlite": Fore.LIGHTGREEN_EX,
	"unreal engine 4": Fore.BLACK,
	"ffmpeg": Fore.LIGHTRED_EX,
	"php": Fore.MAGENTA,
	"lua": Fore.LIGHTBLUE_EX,
	"shell script": Fore.BLACK,
	"love framework": Fore.LIGHTBLUE_EX
}

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
		