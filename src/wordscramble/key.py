# Import pickle and base64 modules for serialization
import pickle
import base64
# Import string module for string operations
import string
# Import zlib to compress out data to make it a little more manageable
import zlib
# Import Dict from Typing module for type-hinting
from typing import Dict
# Import Random object from the random module to generate our random key
from random import Random
# Import deepcopy to make "deep copies" of dictionaries
from copy import deepcopy

class Key:
    
    def __init__(self, mapping: Dict[str, str]):
        self.__mapping = mapping
    
    # We don't want to let people have access to our direct key dictionary,
    # since dict objects are mutable. Instead, create a deep copy to give them.
    @property
    def mapping(self):
        return deepcopy(self.__mapping)
    
    @classmethod
    def random(cls, seed=None) -> "Key":
        randomizer = Random(seed)
        letters = string.ascii_letters + string.digits + string.punctuation + " "
        shuffled = randomizer.sample(letters, len(letters))
        # Create our key
        mapping = {k: v for k, v in zip(letters, shuffled)}
        return cls(mapping)
    
    @classmethod
    def loads(cls, keystring: str):
        # Decode our base85 string, then using pickle to load it.
        compressed_data = base64.b85decode(keystring)
        uncompressed_data = zlib.decompress(compressed_data)
        mapping = pickle.loads(uncompressed_data)
        return cls(mapping)
    
    def dumps(self) -> str:
        # Serialize our key to bytes using pickle, then encode the
        # bytes to base85 for easier copy/pasting.
        serialized_data = pickle.dumps(self.mapping)
        compressed_data = zlib.compress(serialized_data, level=9)
        # Encode our data into base85 so we can easily copy/paste it
        encoded_data = base64.b85encode(compressed_data)
        # Decode our base-64 data into ascii so that it shows as a string instead 
        # of a byte.
        return encoded_data.decode('ascii') 

    def inverse(self) -> "Key":
        # Create a dictionary that has the current mapping dictionary's
        # values as keys and vice versa.
        inverse_mapping = {v: k for k, v in self.mapping.items()}
        return Key(inverse_mapping)

    def __getitem__(self, key: str) -> str:
        if key in self.__mapping:
            return self.__mapping[key]
        raise KeyError(f"Key \"{key}\" not found.")