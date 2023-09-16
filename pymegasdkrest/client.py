from requests import Session
from .constants import RoutePath
from .utils import constructUrl, checkAndRaise 

class MegaSdkRestClient:

	def __init__(self,base_endpoint,session=Session()):
		self.base_endpoint = base_endpoint
		self.session = session

	def login(self, email, password):
		res = self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_LOGIN), json={
			'email': email,
			'password': password
		}).json()
		return checkAndRaise(res, "error_code")

	def adddownload(self, link, directory):
		res = self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_ADD_DL), json={
			'link': link,
			'dir': directory
		}).json()
		return checkAndRaise(res, "error_code")

	def canceldownload(self, gid):
		res = self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_CANCEL_DL), json={
			'gid': gid
		}).json()
		return checkAndRaise(res, "error_code")

	def getstatus(self, gid):
		res = self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_DL_INFO), json={
			'gid': gid
		}).json()
		return checkAndRaise(res, "error_code")