import time
import os
import secrets
import typing as t

class SecurePassword:
    def __init__(self) -> None:
        self._passwd = None
        self._generated_count: int = 1
        
        self._ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        self._ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._digits = '0123456789'
        self._punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        self._all = self._ascii_lowercase + self._ascii_uppercase + self._digits + self._punctuation
    
    def __repr__(self) -> str:
        return f"<Count: {self._generated_count}, LastPassword: {self._passwd}>"
    
    def password(
        self,
        length: t.Union[int, None] = None, 
        lower: t.Union[bool, None] = None,
        upper: t.Union[bool, None] = None, 
        num: t.Union[bool, None] = None, 
        symbols: t.Union[bool, None] = None
    ):
        
        if (150 <= length) and (length >= 3):
            pass 
            self._generated_count += 1

        self._passwd = ''.join(secrets.choice(self._all) for i in range(length))  

obj = SecurePassword()
obj.password(5)
print(obj)