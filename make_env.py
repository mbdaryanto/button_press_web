from pathlib import Path
from django.core.management.utils import get_random_secret_key

env_file = Path(__file__).parent / '.env'


def make_env():
    with env_file.open('w') as f:
        f.write('SECRET_KEY = {!r}\n'.format(get_random_secret_key()))


if __name__ == '__main__':
    make_env()
