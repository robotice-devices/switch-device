#!/srv/robotice/bin/python

import sys
from oslo.config import cfg
from oslo.config import types

try:
    import sensor
    import actuator
except Exception, e:
    raise e

common_opts = [
    cfg.StrOpt('port',
               short='p',
               default='P9_40',
               help='Port for action.'),
    cfg.Opt('mode',
            short='m',
            default="get",
            help='get or set value on the port.'),
    cfg.Opt('value',
            short='v',
            default=0,
            help='for set method mus be provided value.'),
    cfg.Opt('name',
            short='n',
            default="Sensor",
            help='Device name')
]

CONF = cfg.CONF
CONF.register_cli_opts(common_opts)
CONF(sys.argv[1:])

print(sensor.get_data(CONF))