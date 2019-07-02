"""
FREEIPA HealthCheck log - files matching ``/var/log/TBD``
================================================

"""

from .. import parser, LogFileOutput
from datetime import datetime
from insights.specs import Specs
from insights import JSONParser


@parser(Specs.freeipa_healthcheck_log)
class FreeIPAHealthCheckLog(LogFileOutput):
    # use JSONParser there
    pass
