import hashlib
import traceback

from python_aternos import Client
import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

at_client = Client()

at_client.login(username=USERNAME, password=PASSWORD)

aternos = at_client.account

servers = aternos.list_servers()
my_server = servers[0]

