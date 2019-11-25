class ActivateUser(object):
	def process_request(self, request):
		if request.user.is_authenticated():
			request.session.modified = True