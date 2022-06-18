import os
import typing as t
from random import SystemRandom



class SecurePassword:
    def __init__(self) -> None:
        self._sysrand = SystemRandom()
        
        self._passwd = None
        self._generated_count: int = 0
        
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
        lower: t.Union[bool, int, None] = True,
        upper: t.Union[bool, int, None] = None, 
        digits: t.Union[bool, int, None] = None, 
        symbols: t.Union[bool, int, None] = None
    ):

        try:
            if ((250 >= length) and (length <= 3)):
                length = 12
        except TypeError:
            length = 12
            
        character_set = r""
        if bool(lower):
            character_set += self._ascii_lowercase
        if bool(upper):
            character_set += self._ascii_uppercase
        if bool(digits):
            character_set += self._digits
        if bool(symbols):
            character_set += self._digits

        
        self._passwd = ''.join(
            self._sysrand.choice(character_set) 
            for i in range(
                length
                )
            )  

        self._generated_count += 1
        
        return self._passwd
