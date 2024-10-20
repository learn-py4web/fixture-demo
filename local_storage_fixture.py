import uuid

from py4web import redirect, URL
from py4web.core import Fixture


class LocalStorageDemo(Fixture):
    
    def __init__(self):
        super().__init__()
        
    def on_request(self, context):
        Fixture.local_initialize(self) 
        print(f"is_valid: {self.is_valid()}")
        content = str(uuid.uuid4())
        print(f"Storing content: {content}")
        self.local.my_content = content
            
    def on_success(self, context):
        # The line below is used only to show that the thread-local object is in place.
        print(f"Retrieved: {self.local.my_content}")
    