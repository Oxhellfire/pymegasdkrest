from aiohttp import ClientSession
from. constants import RoutePath
from .utils import constructUrl, checkAndRaise

class AsyncMegaSdkRestClient:

    def __init__(self, base_endpoint, session=ClientSession()):
        self.base_endpoint = base_endpoint
        self.session = session

    async def login(self, email, password):
        async with self.session.post(constructUrl(self.base_endpoint,RoutePath.PATH_LOGIN), json={
            'email': email,
            'password': password
        }) as res:
            res_json = await res.json()
            return checkAndRaise(res_json, "error_code")
        
    async def adddownload(self, link, directory):
        async with self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_ADD_DL), json={
            'link': link,
            'dir': directory
        }) as res:
            res_json = await res.json()
            return checkAndRaise(res_json, "error_code")
    
    async def canceldownload(self, gid):
        async with self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_CANCEL_DL), json={
            'gid': gid
        }) as res:
            res_json = await res.json()
            return checkAndRaise(res_json, "error_code")

    async def getstatus(self, gid):
        async with self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_DL_INFO), json={
			'gid': gid
		}) as res:
            res_json = await res.json()
            return checkAndRaise(res_json, "error_code")