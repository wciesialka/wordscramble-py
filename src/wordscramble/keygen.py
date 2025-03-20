# Import pickle and base64 modules for serialization
import pickle
import base64
# Import random module to generate our random key
import random
# Import string module for string operations
import string
# Import zlib to compress out data to make it a little more manageable
import zlib
# Import Dict from Typing module for type-hinting
from typing import Dict

# Seed the random number generator
random.seed()

def generate_random_key():
    # Create a list of letters, and a shuffled version of that list
    letters = string.ascii_letters + string.digits + string.punctuation + " "
    shuffled = random.sample(letters, len(letters))
    # Create our key
    key = {k: v for k, v in zip(letters, shuffled)}
    return key

def decode_key(keystring: str):
    # Decode our base85 string, then using pickle to load it.
    compressed_data = base64.b85decode(keystring)
    uncompressed_data = zlib.decompress(compressed_data)
    return pickle.loads(uncompressed_data)

def encode_key(key: Dict[str, str]):
    # Serialize our key to bytes using pickle, then encode the
    # bytes to base85 for easier copy/pasting.
    serialized_data = pickle.dumps(key)
    compressed_data = zlib.compress(serialized_data, level=9)
    # Encode our data into base85 so we can easily copy/paste it
    encoded_data = base64.b85encode(compressed_data)
    # Decode our base-64 data into ascii so that it shows as a string instead 
    # of a byte.
    return encoded_data.decode('ascii')