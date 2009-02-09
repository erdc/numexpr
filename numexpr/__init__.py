from __config__ import show as show_config, get_info
if get_info('mkl'):
    use_vml = True
    from numexpr.interpreter import _set_vml_accuracy_mode, _set_vml_num_threads
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

def set_vml_accuracy_mode(mode):
    """
    set the accuracy mode for VML operations

    'high': high accuracy mode (HA), <1 least significant bit
    'low': low accuracy mode (LA), typically 1-2 least significant bits
    'fast': enhanced performance mode (EP)
    None: mode settings are ignored

    returns old accuracy settings
    """
    if use_vml:
        acc_dict = {None: 0, 'low': 1, 'high': 2, 'fast': 3}
        acc_reverse_dict = {1: 'low', 2: 'high', 3: 'fast'}
        if mode not in acc_dict.keys():
            raise ValueError("mode argument must be one of: None, 'high', 'low', 'fast'")
        retval = _set_vml_accuracy_mode(acc_dict.get(mode, 0))
        return acc_reverse_dict.get(retval)
    else:
        return None
    
def set_vml_num_threads(nthreads):
    """
    set maximum number of threads used for VML operations.
    """
    if use_vml:
        _set_vml_num_threads(nthreads)
