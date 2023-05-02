import voluptuous as vol

DOMAIN = "asic_miner"

CONF_IP = "ip"
CONF_MINERS = "miners"

ATTR_MINER_HASHRATE = "hashrate"
ATTR_MINER_NOMINAL_HASHRATE = "nominal_hashrate"
ATTR_MINER_MODEL = "model"
ATTR_MINER_MAKE = "make"
ATTR_MINER_TEMPERATURE = "temperature_avg"
ATTR_MINER_WATTAGE = "wattage"
ATTR_MINER_WATTAGE_LIMIT = "wattage_limit"
ATTR_MINER_FAN_1 = "fan_1"
ATTR_MINER_FAN_2 = "fan_2"
ATTR_MINER_FAN_3 = "fan_3"
ATTR_MINER_FAN_4 = "fan_4"
ATTR_MINER_TOTAL_CHIPS = "total_chips"
ATTR_MINER_IDEAL_CHIPS = "ideal_chips"
ATTR_MINER_EFFICIENCY = "efficiency"

MINER_ATTRS = [
    ATTR_MINER_HASHRATE,
    ATTR_MINER_NOMINAL_HASHRATE,
    ATTR_MINER_MODEL,
    ATTR_MINER_MAKE,
    ATTR_MINER_TEMPERATURE,
    ATTR_MINER_WATTAGE,
    ATTR_MINER_WATTAGE_LIMIT,
    ATTR_MINER_FAN_1,
    ATTR_MINER_FAN_2,
    ATTR_MINER_FAN_3,
    ATTR_MINER_FAN_4,
    ATTR_MINER_TOTAL_CHIPS,
    ATTR_MINER_IDEAL_CHIPS,
    ATTR_MINER_EFFICIENCY,
]

MINER_SCHEMA = vol.Schema({vol.Required(CONF_IP)})
