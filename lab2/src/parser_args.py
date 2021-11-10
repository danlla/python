import argparse
import pathlib

class ParserArgs:
    def __init__(self):
        self.pars = argparse.ArgumentParser()
        self.pars.add_argument('--input','-i', type=pathlib.Path, required=True)
        self.pars.add_argument('--output','-o',  type=pathlib.Path, required=True)


    def get_args(self):
        return vars(self.pars.parse_args())
