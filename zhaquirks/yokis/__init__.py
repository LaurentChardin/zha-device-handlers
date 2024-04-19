"""Quirks for Yokis devices."""
from zigpy import types as t
from zigpy.quirks import CustomCluster

Manufacturer_Name = "YOKIS"
Manufacturer_ID = 0x132D

class manuSpecificYokisDevice(CustomCluster):
    """Allows you to manage the parameters related to the device."""

    cluster_id = 0xFC01

    attributes = {
        # Indicate if the device configuration has changed. 0 to 0xFFFE -> No Change, 0xFFFF -> Change have been detected
        0x0005: ("configurationChanged", t.enum16, True), # (name, type, manuspec)
    }

class manuSpecificYokisInput(CustomCluster):
    """Cluster used to configure the different inputs options of a device (NO/NC, ContactMode …)."""

    cluster_id = 0xFC02

    attributes = {
        #Indicate how the input should be handle: 0 -> Unknown, 1 -> Push button, 2 -> Switch, 3 -> Relay, 4 -> FP_IN
        0x0000: ('inputMode', t.enum8, True),
        #Indicate the contact nature of the entry: 0 -> NC, 1 -> NO
        0x0001: ('contactMode', t.Bool, True),
        #Indicate the last known state of the local BP (Bouton Poussoir, or Push Button)
        0x0002: ('lastLocalCommandState', t.Bool, True),
        #Indicate the last known state of the Bp connect
        0x0003: ('lastBPConnectState', t.Bool, True),
        #Indicate the last known state of the Bp connect
        0x0004: ('backlightIntensity', t.uint8_t, True)
    }

class manuSpecificYokisEntryConfigurator(CustomCluster):
    """Cluster used to configure press duration, time between press,..."""

    cluster_id = 0xFC03

    attributes = {
        #Use to enable short press action
        0x0001: ('eShortPress', t.Bool, True),
        #Use to enable long press action
        0x0002: ('eLongPress', t.Bool, True),
        #Define long Press duration in milliseconds. Default: 0x0BB8, Min-Max: 0x00 - 0x1388
        0x0003: ('longPressDuration', t.uint16_t, True),
        #Define the maximum time between 2 press to keep in a sequence (In milliseconds). Default: 0x01F4, Min-Max: 0x0064 - 0x0258
        0x0004: ('timeBetweenPress', t.uint16_t, True),
        #Enable R12M Long Press action
        0x0005: ('eR12MLongPress', t.Bool, True),
        #Disable local configuration
        0x0006: ('eLocalConfigLock', t.Bool, True)
    }

class manuSpecificYokisSubSystem(CustomCluster):
    """Define specific behavior of device sub system."""

    cluster_id = 0xFC04

    attributes = {
        #Define the device behavior after power failure : 0 -> LAST STATE, 1 -> OFF, 2 -> ON, 3-> BLINK
        0x0001: ("powerFailureMode", t.enum8, True),
    }

class manuSpecificYokisLoadManager(CustomCluster):
    """Cluster used to define values of LoadManager on the device."""

    cluster_id = 0xFC05

class manuSpecificYokisLightControl(CustomCluster):
    """Cluster used to create for complex On/Off commands. It expend the classic cluster On/Off (ID : 0x0006)."""

    cluster_id = 0xFC06

    attributes = {
        #Use to know which state is the relay
        0x0000: ('onOff', t.Bool, True),
        #Indicate the previous state before action
        0x0001: ('prevState', t.Bool, True),
        #Define the ON embedded timer duration in seconds.  Default: 0x00, Min-Max: 0x00 – 0x00409980
        0x0002: ('onTimer', t.uint32_t, True),
        #Enable (0x01) / Disable (0x00) use of onTimer.
        0x0003: ('eOnTimer', t.Bool, True),
        #Define the PRE-ON embedded delay in seconds.  Default: 0x00, Min-Max: 0x00 – 0x00409980
        0x0004: ('preOnDelay', t.uint32_t, True),
        #Enable (0x01) / Disable (0x00) use of PreOnTimer.
        0x0005: ('ePreOnDelay', t.Bool, True),
        #Define the PRE-OFF embedded delay in seconds.  Default: 0x00, Min-Max: 0x00 – 0x00409980
        0x0008: ('preOffDelay', t.uint32_t, True),
        #Enable (0x01) / Disable (0x00) PreOff delay.
        0x0009: ('ePreOffDelay', t.Bool, True),
        #Set the value of ON pulse length. Default: 0x01F4, Min-Max: 0x0014 – 0xFFFE
        0x000A: ('pulseDuration', t.uint16_t, True),
        #Indicates the current Type of time selected that will be used during push button configuration: 0x00 -> Seconds, 0x01 -> Minutes
        0x000B: ('timeType', t.enum8, True),
        #Set the value of the LONG ON embedded timer in seconds.  Default: 0x5460 (1h), Min-Max: 0x00 – 0x00409980
        0x000C: ('longOnDuration', t.uint32_t, True),
        #Indicates the operating mode: 0x00 -> Timer, 0x01 -> Staircase, 0x02 -> Pulse
        0x000D: ('operatingMode', t.enum8, True),
        #Time before goes off after the stop announce blinking. (In seconds).  Default: 0x0000, Min-Max: 0x00 – 0x00409980
        0x0013: ('stopAnnounceTime', t.uint32_t, True),
        #Enable (0x01) / Disable (0x00) the announcement before turning OFF.
        0x0014: ('eStopAnnounce', t.Bool, True),
        #Enable (0x01) / Disable (0x00) Deaf Actions.
        0x0015: ('eDeaf', t.Bool, True),
        #Enable (0x01) / Disable (0x00) Blink Actions.
        0x0016: ('eBlink', t.Bool, True),
        #Number of blinks done when receiving the corresponding order. One blink is considered as one ON step followed by one OFF step. Default: 0x03, Min-Max: 0x00 – 0x14
        0x0017: ('blinkAmount', t.uint8_t, True),
        #Duration for the ON time on a blink period (In millisecond).  Default: 0x000001F4, Min-Max: 0x00 – 0x00409980
        0x0018: ('blinkOnTime', t.uint32_t, True),
        #Duration for the OFF time on a blink period (In millisecond).  Default: 0x000001F4, Min-Max: 0x00 – 0x00409980
        0x0019: ('blinkOffTime', t.uint32_t, True),
        #Define number of blink to do when receiving the DEAF action. One blink is considered as one ON step followed by one OFF step. Default: 0x03, Min-Max: 0x00 – 0x14
        0x001A: ('deafBlinkAmount', t.uint8_t, True),
        #Define duration of a blink ON (In millisecond). Default: 0x0320, Min-Max: 0x0064– 0x4E20
        0x001B: ('deafBlinkTime', t.uint16_t, True),
        #Indicate which state must be apply after a blink sequence: 0x00 -> State before blinking, 0x01 -> OFF, 0x02 -> ON
        0x001C: ('stateAfterBlink', t.enum8, True),
        #Define the output relay as Normally close.
        0x001D: ('eNcCommand', t.Bool, True),
    }

class manuSpecificYokisDimmer(CustomCluster):
    """TBD."""

    cluster_id = 0xFC07

class manuSpecificYokisWindowCovering(CustomCluster):
    """TBD."""

    cluster_id = 0xFC08

class manuSpecificYokisChannel(CustomCluster):
    """TBD."""

    cluster_id = 0xFC09

class manuSpecificYokisPilotWire(CustomCluster):
    """TBD."""

    cluster_id = 0xFC0A

class manuSpecificYokisStats(CustomCluster):
    """TBD."""

    cluster_id = 0xFCF0
