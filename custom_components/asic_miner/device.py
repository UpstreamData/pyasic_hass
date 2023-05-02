from homeassistant.helpers.entity import Entity

from .const import MINER_ATTRS, ATTR_MINER_HASHRATE

import logging
from pyasic.network import ping_and_get_miner

_LOGGER = logging.getLogger(__name__)

class MinerDevice(Entity):
    def __init__(self, ip):
        self.ip = ip
        self._miner_info = {}
        self._available = True

    @property
    def available(self):
        return self._available

    @property
    def name(self):
        return f"ASIC Miner ({self.ip})"

    @property
    def state(self):
        return self._miner_info.get(ATTR_MINER_HASHRATE)

    @property
    def device_state_attributes(self):
        attributes = {}
        attributes["available"] = self._available
        return attributes

    async def async_update(self):
        miner = await ping_and_get_miner(self.ip)
        if not miner:
            self._available = False
            return
        self._available = True
        data = await miner.get_data()
        for item in MINER_ATTRS:
            try:
                self._miner_info[item] = data[item]
            except KeyError:
                _LOGGER.exception(f"Could not collect key {item} for data")

class MinerAttribute(Entity):
    def __init__(self, miner_device, attribute):
        self._miner_device = miner_device
        self._attribute = attribute

    @property
    def name(self):
        return f"{self._miner_device.name} - {self._attribute}"

    @property
    def state(self):
        return self._miner_device._miner_info.get(self._attribute)

    @property
    def device_state_attributes(self):
        attributes = {}
        attributes["available"] = self._miner_device.available
        return attributes

    async def async_update(self):
        await self._miner_device.async_update()
        self.async_schedule_update_ha_state(True)
