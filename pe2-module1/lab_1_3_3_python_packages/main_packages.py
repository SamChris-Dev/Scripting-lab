# main_packages.py
from sys import path

path.append('./packages')

import extra.iota
import extra.good.alpha as alpha
from extra.good.best.sigma import FunS

print("Accessing top-level module:", extra.iota.FunI())  
print("Accessing sub-package module:", alpha.FunA())     
print("Accessing deep sub-package:", FunS())             


import extra.good.best.tau as tau
print("Deepest module function:", tau.FunT())            