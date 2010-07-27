"""
Numexpr is a fast numerical expression evaluator for NumPy.  With it,
expressions that operate on arrays (like "3*a+4*b") are accelerated
and use less memory than doing the same calculation in Python.

See:

http://code.google.com/p/numexpr/

for more info about it.

"""

from __config__ import show as show_config, get_info

if get_info('mkl'):
    use_vml = True
else:
    use_vml = False

from cpuinfo import cpu
if cpu.is_AMD() or cpu.is_Intel():
    is_cpu_amd_intel = True
else:
    is_cpu_amd_intel = False

import os.path
from numexpr.expressions import E
from numexpr.necompiler import NumExpr, disassemble, evaluate
from numexpr.tests import test, print_versions
from numexpr.utils import (
    get_vml_version, set_vml_accuracy_mode, set_vml_num_threads,
    set_num_threads)

# Initialize the number of threads to be used
set_num_threads(2)   # XXX use an automatic detection of the number of cores

import version

dirname = os.path.dirname(__file__)

__version__ = version.version


