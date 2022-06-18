import os
import typing as t
from random import SystemRandom



class SecurePassword:
    def __init__(self) -> None:
        self._sysrand = SystemRandom()
        
        self._passwd = None
        self._generated_count: int = 1
        
        self._ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        self._ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._digits = '0123456789'
        self._symbols = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        self._all = self._ascii_lowercase + self._ascii_uppercase + self._digits + self._symbols
    
    def __repr__(self) -> str:
        return f"<Count: {self._generated_count}, LastPassword: {self._passwd}>"
    
    def password(
        self,
        length: t.Union[int, None] = None, 
        lower: t.Union[bool, None] = None,
        upper: t.Union[bool, None] = None, 
        digits: t.Union[bool, None] = None, 
        symbols: t.Union[bool, None] = None
    ):
        
        character_set = r""
        if (150 <= length) and (length >= 3):
            if lower:
                character_set += self._ascii_lowercase
            if upper:
                character_set += self._ascii_uppercase
            if digits:
                character_set += self._digits
            if symbols:
                character_set += self._digits

        self._passwd = ''.join(
            self._sysrand.choice(self._all) 
            for i in range(
                length
                )
            )  

        self._generated_count += 1

obj = SecurePassword()
obj.password(100)
print(obj)
