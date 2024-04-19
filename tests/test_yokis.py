"""Tests for Yokis quirks."""


import zhaquirks.yokis.mtr

zhaquirks.setup()

def test_yokis_signature(assert_signature_matches_quirk):
    """Test Yokis signature matching to its quirk."""

    signature = {
        "node_descriptor": "NodeDescriptor(logical_type=<LogicalType.Router: 1>, complex_descriptor_available=0, user_descriptor_available=0, reserved=0, aps_flags=0, frequency_band=<FrequencyBand.Freq2400MHz: 8>, mac_capability_flags=<MACCapabilityFlags.FullFunctionDevice|MainsPowered|RxOnWhenIdle|AllocateAddress: 142>, manufacturer_code=4909, maximum_buffer_size=82, maximum_incoming_transfer_size=82, server_mask=11264, maximum_outgoing_transfer_size=82, descriptor_capability_field=<DescriptorCapability.NONE: 0>, *allocate_address=True, *is_alternate_pan_coordinator=False, *is_coordinator=False, *is_end_device=False, *is_full_function_device=True, *is_mains_powered=True, *is_receiver_on_when_idle=True, *is_router=True, *is_security_capable=False)",
        "endpoints": {
            "1": {
                "profile_id": 0x0104,
                "device_type": "0x0100",
                "input_clusters": [
                    "0x0000",
                    "0x0003",
                    "0x0004",
                    "0x0005",
                    "0x0006",
                    "0x1000",
                    "0xfc01",
                    "0xfc02",
                    "0xfc03",
                    "0xfc04",
                    "0xfc05",
                    "0xfc06",
                    "0xfcf0"
                ],
                "output_clusters": [
                    "0x0003",
                    "0x0006",
                    "0x0019",
                    "0x1000",
                    "0xfc01",
                    "0xfc06"
                ]
            },
            "242": {
                "profile_id": 0xa1e0,
                "device_type": "0x0066",
                "input_clusters": [
                    "0x0021"
                ],
                "output_clusters": [
                    "0x0021"
                ]
            }
        },
        "manufacturer": "YOKIS",
        "model": "MTR500E-UP",
        "class": "zigpy.device.Device"
    }

    assert_signature_matches_quirk(zhaquirks.yokis.mtr.MTR, signature)
