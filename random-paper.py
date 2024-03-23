#!/Users/nbbaier/.pyenv/versions/3.11.0/bin/python3

import argparse
import os
import random


# Set up the arguments in
parser = argparse.ArgumentParser()
parser.add_argument("num", type=int, nargs="?", default=5)  # This added a
parser.add_argument("-o", "--open", action="store_true")
args = parser.parse_args()

# :dir: directory to look in for papers
# :papers: list of files in dir
# :index: length of the list of files
dir = "/Users/nbbaier/My Drive/literature"
papers = os.listdir(dir)
index = len(papers)
os.chdir(dir)


def get_papers():
    """Loops througy an enumerated of files drawn from the list of papers
    This list is randomly generated and has its length set by args.num (default 5)
    If the -o/--open flag is provided, the papers are opened, if not, they're just printed
    """
    for i, paper in enumerate(papers[random.randint(0, index)] for _ in range(args.num)):
        print(f"{i+1} \t {paper}")
        if args.open:
            file = paper.replace(" ", "\ ")
            os.system(f"open {file}")


if __name__ == "__main__":
    get_papers()
