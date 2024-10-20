from py4web import redirect, URL
from py4web.core import Fixture


class Admin(Fixture):
    
    def __init__(self, auth, admin_list, redirect_url=None):
        super().__init__()
        self.admin_list = admin_list
        self.auth = auth
        self.__prerequisites__ = [auth]
        # One thing to note here is that the URL function can ONLY be called in a 
        # request context (while serving a request).  Thus, we cannot store in the fixture
        # initialization the full URL to redirect, but only the path. 
        self.redirect_url = redirect_url or 'index'
        
    def on_request(self, context):
        if ((not self.auth.current_user) 
            or self.auth.current_user.get('email') not in self.admin_list):
            # The URL function can be called while serving a request to get the full URL
            # from the URL path. 
            redirect(URL(self.redirect_url))
            
    def on_success(self, context):
        # The line below is used only to show that the thread-local object is in place.
        print(f"admin_storage: {self.local.admin_storage}")
    
    def on_error(self, context):
        redirect(URL(self.redirect_url))
