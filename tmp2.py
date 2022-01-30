import sys, site
print('sys:', sys.version, sys.version_info, sys.api_version, sys.prefix, sys.exec_prefix, '\nsite:',
    site.getsitepackages(), site.getusersitepackages(), site.getuserbase(), sep='\n')
list