class File:
	def __init__(self, path: str) -> None:
		self.path = path
		self.file_name = path.split("\\")[-1]
	
	def __repr__(self) -> str:
		return self.path