"""GitHub sensor platform."""
from __future__ import annotations

import pyasic
from pyasic.network import ping_and_get_miner
from collections.abc import Callable
from datetime import timedelta
import logging
from typing import Any

from homeassistant import config_entries, core
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    ATTR_NAME,
    CONF_ACCESS_TOKEN,
    CONF_NAME,
    CONF_PATH,
    CONF_URL,
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.typing import (
    ConfigType,
    DiscoveryInfoType,
    HomeAssistantType,
)
import voluptuous as vol

from .const import (
    DOMAIN,
CONF_IP,
CONF_MINERS,
MINER_ATTRS
)

_LOGGER = logging.getLogger(__name__)
# SCAN_INTERVAL = timedelta(minutes=10)

MINER_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_IP): str,
    }
)



async def async_setup_entry(
    hass: core.HomeAssistant,
    config_entry: config_entries.ConfigEntry,
    async_add_entities,
) -> None:
    """Setup sensors from a config entry created in the integrations UI."""
    config = hass.data[DOMAIN][config_entry.entry_id]
    if config_entry.options:
        config.update(config_entry.options)
    sensors = [MinerSensor(m) for m in config[CONF_MINERS]]
    async_add_entities(sensors, update_before_add=True)


async def async_setup_platform(
    hass: HomeAssistantType,
    config: ConfigType,
    async_add_entities: Callable,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""
    sensors = [MinerSensor(m) for m in config[CONF_MINERS]]
    async_add_entities(sensors, update_before_add=True)


class MinerSensor(Entity):
    """Representation of a GitHub Repo sensor."""

    def __init__(self, ip: str):
        super().__init__()
        self.ip = ip
        self._name = "Unknown"
        self._available = True
        self.attrs = {}

    @property
    def name(self) -> str:
        """Return the name of the entity."""
        return self._name

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        return self.attrs

    async def async_update(self) -> None:
        """Update all sensors."""

        miner = await ping_and_get_miner(self.ip)
        if not miner:
            self._available = False
            return
        self._available = True
        data = await miner.get_data()
        for item in MINER_ATTRS:
            try:
                self.attrs[item] = data[item]
            except KeyError:
                _LOGGER.exception(f"Could not collect key {item} for data")
