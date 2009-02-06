from __config__ import show as show_config, get_info
if get_info('mkl'):
    use_vml = True
    from numexpr.interpreter import set_vml_accuracy_mode, set_num_threads
else:
    use_vml = False

import os.path
from numexpr.info import __doc__
from numexpr.expressions import E
from numexpr.necompiler import numexpr, disassemble, evaluate
from numexpr.tests import test

import version

dirname = os.path.dirname(__file__)

__version__ = version.version

