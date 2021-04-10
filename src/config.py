# absolute paths to specific files
# ex: /home/name/athena/temp/athena.pid

paths = {
    'RESOURCES':'',
    'TEMP':'',
    'MODEL':''
}

try:
    from . import local_config as local
    paths = local.paths
except:
    pass