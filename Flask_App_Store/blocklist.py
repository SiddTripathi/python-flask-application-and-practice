"""
This file just contains the blocklist of jwt tokens. It will be imported by app and the logout resources so that tokens can be added 
to blocklist when the user logs out

"""

BLOCKLIST = set()