from distutils.core import setup, Extension

bell_yespower_module = Extension('bell_yespower',
                            sources = ['yespower-module.c',
                                       'yespower.c',
                                       'yespower-opt.c',
                                       'yespower-platform.c',
                                       'yespower-ref.c',
                                       'sha256.c'
                                       ],
                            extra_compile_args=['-march=native', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'bell_yespower',
       version = '1.0',
       description = 'Bindings for yespower-1.0 proof of work used by bellcoin',
       ext_modules = [bell_yespower_module])
