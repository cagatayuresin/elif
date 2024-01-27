import random
import string
import os
from pathlib import Path


def create_dot_env():
    def generate_secret_key():
        characters = string.ascii_letters + string.digits + string.punctuation
        secret_key = "".join(random.choice(characters) for _ in range(50)).replace(
            '"', "?"
        )
        return secret_key

    project_root = Path(__file__).resolve().parent.parent.parent
    env_file_path = os.path.join(project_root, ".env")
    new_secret_key = generate_secret_key()
    with open(env_file_path, "w") as env_file:
        env_file.write(f'DJANGO_SECRET_KEY="django-insecure-{new_secret_key}"\n')
