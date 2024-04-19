"""Yokis MTR500E-UP."""
from zigpy.profiles import zgp, zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import (
    Basic,
    GreenPowerProxy,
    Groups,
    Identify,
    OnOff,
    Ota,
    Scenes,
)
from zigpy.zcl.clusters.lightlink import LightLink

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.yokis import (
    Manufacturer_ID,
    Manufacturer_Name,
    manuSpecificYokisDevice,
    manuSpecificYokisEntryConfigurator,
    manuSpecificYokisInput,
    manuSpecificYokisLightControl,
    manuSpecificYokisLoadManager,
    manuSpecificYokisStats,
    manuSpecificYokisSubSystem,
)


class MTR(CustomDevice):
    """Yokis MTR devices."""

    manufacturer_id_override = Manufacturer_ID

    signature = {
        MODELS_INFO: [(Manufacturer_Name, "MTR500E-UP")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    LightLink.cluster_id,
                    manuSpecificYokisDevice.cluster_id,
                    manuSpecificYokisInput.cluster_id,
                    manuSpecificYokisEntryConfigurator.cluster_id,
                    manuSpecificYokisSubSystem.cluster_id,
                    manuSpecificYokisLoadManager.cluster_id,
                    manuSpecificYokisLightControl.cluster_id,
                    manuSpecificYokisStats.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    Ota.cluster_id,
                    LightLink.cluster_id,
                    manuSpecificYokisDevice.cluster_id,
                    manuSpecificYokisLightControl.cluster_id,
                ],
            },
            242: {
                PROFILE_ID: zgp.PROFILE_ID,
                DEVICE_TYPE: zgp.DeviceType.COMBO_BASIC,
                INPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    LightLink.cluster_id,
                    manuSpecificYokisDevice,
                    manuSpecificYokisInput,
                    manuSpecificYokisEntryConfigurator,
                    manuSpecificYokisSubSystem,
                    manuSpecificYokisLightControl,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    Ota.cluster_id,
                    LightLink.cluster_id,
                    manuSpecificYokisDevice,
                    manuSpecificYokisLightControl,
                ],
            },
        },
    }

