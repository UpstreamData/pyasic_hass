import voluptuous as vol
from homeassistant

DOMAIN = "asic_miner"

CONF_IP = "ip"

MINER_SCHEMA = vol.Schema(
    {vol.Required(CONF_IP)}
)
