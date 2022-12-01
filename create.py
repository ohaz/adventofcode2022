import os
import shutil
from aocd import get_data

YEAR = 2022

if __name__ == '__main__':
    folders = os.listdir('solutions')
    newest_day = max([int(x.replace('day', '')) for x in folders if x.startswith('day')], default=0) + 1

    source_file = 'template.py'
    target_folder = os.path.join('solutions', f'day{newest_day}')
    target_file = os.path.join(target_folder, 'main.py')
    os.makedirs(target_folder, exist_ok=False)
    shutil.copyfile(source_file, target_file)
    shutil.copyfile(os.path.join('solutions', '__init__.py'), os.path.join(target_folder, '__init__.py'))

    data = get_data(day=newest_day, year=YEAR)
    with open(os.path.join(target_folder, 'input.txt'), 'w') as f:
        f.write(data)