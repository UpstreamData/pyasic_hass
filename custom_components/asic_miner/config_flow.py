from .const import DOMAIN, CONF_IP
from homeassistant import config_entries
import voluptuous as vol
from copy import deepcopy
import logging
from typing import Any, Dict, Optional

from homeassistant import config_entries, core
from homeassistant.const import CONF_ACCESS_TOKEN, CONF_NAME, CONF_PATH, CONF_URL
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity_registry import (
    async_entries_for_config_entry,
    async_get,
)

MINER_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_IP): str,
    }
)


async def validate_miner_exists():
    pass


class MinerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            print(user_input)

        return self.async_show_menu(
            step_id="user",
            menu_options={"Scan Network": "scan", "Add Manually": "manual"},
        )

    async def async_step_scan(self, user_input=None):
        if user_input is not None:
            print(user_input)

        return self.async_show_menu(
            step_id="user",
            menu_options={"Scan Network": "scan", "Add Manually": "manual"},
        )
