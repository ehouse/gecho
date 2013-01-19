from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home', renderer='machineList.mak')
def homeView(request):
	return {'project': 'web','title':'gecho'}
