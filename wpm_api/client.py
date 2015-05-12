# Copyright 2000 - 2015 NeuStar, Inc.All rights reserved.
# NeuStar, the Neustar logo and related names and logos are registered
# trademarks, service marks or tradenames of NeuStar, Inc. All other
# product names, company names, marks, logos and symbols may be trademarks
# of their respective owners.
from .connection import Connection
from .load import Load
from .instanttest import InstantTest
from .monitor import Monitor

class Client:
    def __init__(self, api_key, secret):
        """Initialize the API client.

        Arguments:
        api_key -- The WPM user's API key
        secret -- Shared secret

        """
        self.connection = Connection(api_key, secret)
        
    def load(self, id=None):
        return Load(self.connection, id)
        
    def instanttest(self, id=None):
        return InstantTest(self.connection, id)
        
    def monitor(self, id=None):
        return Monitor(self.connection, id)