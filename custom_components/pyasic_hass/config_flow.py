from .const import DOMAIN, CONF_IP
from homeassistant import config_entries
import voluptuous as vol


INIT_MINER_SCHEMA = vol.Schema(
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
        pass
