import hashlib

# Constants
CREDENTIALS_FILE = "A8_T5_credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    hashed = hashlib.md5(password.encode())
    return hashed.hexdigest()


def register(PUsername: str, PPassword: str) -> None:
    """
    Register a new user by appending their credentials to the file.
    """
    with open(CREDENTIALS_FILE, "r") as file:
        lines = file.readlines()
        new_id = len(lines)

    hashed = hash_password(PPassword)

    with open(CREDENTIALS_FILE, "a") as f:
        f.write(f"{new_id}{DELIMITER}{PUsername}{DELIMITER}{hashed}\n")

    return None

def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    hashed = hash_password(PPassword)

    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            user_id, username, stored_hash = line.split(DELIMITER)

            if username == PUsername and stored_hash == hashed:
                return True

    return False


def viewProfile(PUsername: str) -> list[str]:
    """
    Return the user ID and username for the given username.
    """
    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            user_id, username, pw_hash = line.split(DELIMITER)

            if username == PUsername:
                return [user_id, username]

    return []


def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    # TODO: Read all lines, update the password for the matching user
    # TODO: Write the updated lines back to the file
    pass
