import voluptuous as vol
from pyasic.network import ping_miner
from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS
import homeassistant.helpers.config_validation as cv


async def validate_miner_ip(ip):
    m = ping_miner(ip)
    if m:
        return True, None
    else:
        return False, "no response"


class AsicMinerConfigFlow(config_entries.ConfigFlow, domain="asic_miner"):
    """Asic Miner config flow."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        err = None
        if user_input is not None:
            # Validate the IP address.
            ip_address = user_input[CONF_IP_ADDRESS]
            result, err = await validate_miner_ip(ip_address)
            if result:
                # If the IP address is valid, create the config entry.
                return self.async_create_entry(title=ip_address, data=user_input)

        # Show the form to the user.
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Required(CONF_IP_ADDRESS): cv.string}
            ),
            errors=err
        )

    async def async_step_import(self, import_config):
        """Import a configuration from configuration.yaml."""
        # If there's already a config entry for this IP address, return it.
        for entry in self._async_current_entries():
            if entry.data[CONF_IP_ADDRESS] == import_config[CONF_IP_ADDRESS]:
                return self.async_abort(reason="already_configured")

        # Create the config entry for this IP address.
        return self.async_create_entry(
            title=import_config[CONF_IP_ADDRESS], data=import_config
        )
