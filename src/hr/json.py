import json
import pwd

from .helpers import user_names

def read(file_path):
    with open(file_path, "r") as f:
        file_contents = json.loads(f.read())
    return file_contents

def export(file_path, user_names=user_names()):
    with open(file_path, "w") as f:
        f.write(json.dumps(user_names))


