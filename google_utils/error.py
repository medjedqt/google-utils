class GoogleUtilsError(Exception):
	pass

class InvalidCalculation(GoogleUtilsError):
	def __init__(self, calc: str):
		message: str = f'Invalid calculation: "{calc}"'
		super().__init__(message)