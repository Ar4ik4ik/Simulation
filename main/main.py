import json
from pathlib import Path

balance = {
    'Grass': 0.2,
    'Rock': 0.05,
    'Tree': 0.07,
    'Predator': 0.05,
    'Herbivore': 0.1
}
path = Path().cwd() / 'balance_conf.json'
json.dump(balance, path.open('w'))
