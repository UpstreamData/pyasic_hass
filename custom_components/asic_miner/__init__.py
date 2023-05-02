from .config_flow import AsicMinerConfigFlow
from .device import MinerDevice, MinerAttribute
from .const import MINER_ATTRS
CONFIG_FLOW_CLASS = AsicMinerConfigFlow


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the ASIC miner devices."""
    ip_address = config_entry.data["ip_address"]
    miner = MinerDevice(ip_address)
    entities = []
    for attr in MINER_ATTRS:
        entities.append(MinerAttribute(miner, attr))
    async_add_entities(entities)
