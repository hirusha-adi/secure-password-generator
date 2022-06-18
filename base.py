import time
import os
import secrets
import typing as t

class SecurePassword:
    def __init__(self) -> None:
        self._passwd = None
        
        self._ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        self._ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._digits = '0123456789'
        self._punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        self._all = self._ascii_lowercase + self._ascii_uppercase + self._digits + self._punctuation
    
    def __repr__(self) -> str:
        pass
    
    def password(
        length: t.Union[int, None] = None, 
        lower: t.Union[bool, None] = None,
        upper: t.Union[bool, None] = None, 
        num: t.Union[bool, None] = None, 
        symbols: t.Union[bool, None] = None
    ):
        
        all = lower + upper + num + symbols

#use secrets

password = ''.join(secrets.choice(all) for i in range(length))  

#print the password
print(password)
