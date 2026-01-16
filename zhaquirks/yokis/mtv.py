from zigpy.quirks.v2 import add_to_registry_v2
from zigpy.zcl.clusters.general import Basic, Identify, OnOff

(
    add_to_registry_v2("YOKIS", "MTR1300E-UP")
    .also_applies_to("YOKIS", "MTR2000E-UP")
    .adds(Basic.cluster_id)
    .adds(OnOff.cluster_id)
    .adds(Identify.cluster_id)
    .device_automation_triggers(
        {
            (SHORT_PRESS, BUTTON): {COMMAND: COMMAND_TOGGLE},
            (DOUBLE_PRESS, BUTTON): {COMMAND: COMMAND_ON},
            (LONG_PRESS, BUTTON): {COMMAND: COMMAND_OFF},
        }
    )
)
