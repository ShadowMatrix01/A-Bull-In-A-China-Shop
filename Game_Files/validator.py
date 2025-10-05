import re
import unicodedata

def valid_name(name):
    name = unicodedata.normalize('NFC', name.strip())
    return bool(re.fullmatch(r"[A-Za-z\s'-]{1,20}", name))