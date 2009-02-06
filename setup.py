#!/usr/bin/env python

def configuration():
    from numpy.distutils.misc_util import Configuration, dict_append
    from numpy.distutils.system_info import system_info

    config = Configuration(package_name = 'numexpr')

    #try to find configuration for MKL, either from environment or site.cfg
    mkl_config_data = config.get_info('mkl')
    #some version of MKL need to be linked with libgfortran, for this, use
    #entries of DEFAULT section in site.cfg
    default_config = system_info()
    dict_append(mkl_config_data,
                libraries = default_config.get_libraries(),
                library_dirs = default_config.get_lib_dirs() )

    #setup information for C extension
    extension_config_data = {'sources': ['numexpr/interpreter.c'],
                             'depends': ['numexpr/interp_body.c',
                                         'numexpr/complex_functions.inc'],
                             'extra_compile_args': ['-funroll-all-loops'],}
    dict_append(extension_config_data, **mkl_config_data)
    config.add_extension('interpreter',
                         **extension_config_data)

    config.make_config_py()
    config.add_data_files( ('', '*.txt'),
                           #('', 'site.cfg.example'),
                           #('numexpr', 'VERSION'),
                           )
    config.add_subpackage('tests', 'numexpr/tests')

    #version handling
    config.make_svn_version_py()
    config.get_version('numexpr/version.py')
    return config

def setup_package():
    import os
    from numpy.distutils.core import setup


    setup(name='numexpr',
          description='Fast numerical expression evaluator for NumPy',
          author='David M. Cooke, Tim Hochberg, Francesc Alted, Ivan Vilata',
          author_email='david.m.cooke@gmail.com, faltet@pytables.org',
          url='http://code.google.com/p/numexpr/',
          license = 'MIT',
          packages = ['numexpr'],
          configuration = configuration,
          #**extra_setup_opts
          )

#some old code I was not able to use with numpy.distutils

## setuptools should be able to find out by itself the right option for zip_save
#     try:
#         import setuptools
#     except ImportError:
#         setuptools = None

#     extra_setup_opts = {}
#     if setuptools:
#         extra_setup_opts['zip_safe'] = False

## building on windows: who knows?
# class build_ext(old_build_ext):
#     def build_extension(self, ext):
#         # at this point we know what the C compiler is.
#         c = self.compiler
#         old_compile_options = None
#         if ext is interpreter_ext:
#             # For MS Visual C, we use /O1 instead of the default /Ox,
#             # as /Ox takes a long time (~20 mins) to compile.
#             # The speed of the code isn't noticeably different.
#             if c.compiler_type == 'msvc':
#                 if not c.initialized:
#                     c.initialize()
#                 old_compile_options = c.compile_options[:]
#                 if '/Ox' in c.compile_options:
#                     c.compile_options.remove('/Ox')
#                 c.compile_options.append('/O1')
#                 ext.extra_compile_args = []
#         old_build_ext.build_extension(self, ext)
#         if old_compile_options is not None:
#             self.compiler.compile_options = old_compile_options

# extra_setup_opts['cmdclass'] = {'build_ext': build_ext}

if __name__ == '__main__':
    setup_package()
