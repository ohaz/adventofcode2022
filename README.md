# adventofcode2022

These are my solutions for the [advent of code](https://adventofcode.com/2022) challenges of the year 2022.

Keep in mind that the solutions provided here most of the time do not follow clean code or any other quality metrics, as I try to solve the tasks as quickly as possible.

## Requirements

These scripts require python 3.10 to run, as some features introduced in that version are used.

### Installing

To install the requirements, if a `requirements.txt` exists, run:

`pip install -r requirements.txt`

If you want to use this script to create folders and download inputs for new days:

* Log in to AOC in a browser
* Run aocd-token in a console. This searches for the session cookie of your login and stores it in `~/.config/aocd/token`. It's used to download the current days input (see https://pypi.org/project/advent-of-code-data/).
* Now you can use `python create.py` to download the next available day.

### Running

To run all days, just run:

`python main.py`

To run just one day, run:

`python main.py <number_of_day>`, e.g. `python main.py 11`