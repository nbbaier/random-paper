import argparse
import os
import random
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int, nargs="?", default=5)
parser.add_argument("-o", "--open", action="store_true")
parser.add_argument("-d", "--directory", help="Directory containing papers")
args = parser.parse_args()

directory = (
    args.directory
    or os.environ.get("PAPERS_DIR")
    or f"{Path.home()}/My Drive/literature"
)

if not os.path.exists(directory):
    print(f"Error: Directory '{directory}' does not exist.")
    print(
        "Please specify a valid directory using --directory flag or PAPERS_DIR environment variable."
    )
    exit(1)

papers = os.listdir(directory)
index = len(papers) - 1
os.chdir(directory)


def get_papers():
    """
    Selects a random set of papers from a list and prints their names. Optionally, opens the selected papers.

    The function performs the following steps:
    1. Randomly selects a specified number of papers from the 'papers' list.
    2. Prints the name of each selected paper.
    3. If the 'open' argument is set, opens each selected paper using the default system application.
    """
    for paper in random.sample(papers, args.number):
        print(f"* {paper}")
        if args.open:
            subprocess.run(["open", paper])


if __name__ == "__main__":
    get_papers()
