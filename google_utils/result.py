class Result:
	def __init__(self, **kwargs):
		self.title = kwargs.get('title')
		self.link = kwargs.get('link')
		self.domain = kwargs.get('domain')
		self.answer = kwargs.get('answer')
		self.question = kwargs.get('question')
		self.phrase = kwargs.get('phrase')
		self.pronunciation = kwargs.get('pronun')
		self.type = kwargs.get('type')
		self.meaning = kwargs.get('meaning')