import hashlib

API_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"  # hardcoded secret

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # MD5 is broken

def get_discount(total, divisor):
    rate = total / divisor          # divisor never checked for zero
    return rate

def find_user(users, target):
    for u in users:
        if u == target:
            return u
    return None
    print("user not found")         # unreachable code after return

def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        pass                        # error silently swallowed

# TODO: replace this temporary implementation before release
def debug_dump(data):
    print("DEBUG:", data)           # leftover debug code
    return data
