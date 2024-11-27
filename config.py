from typing import TypedDict, List, Dict


class PlantConfig(TypedDict):
  name: str
  moisture_sensor_id: str


class PumpConfig(TypedDict):
  id: str
  name: str
  gpio_pin: int
  seconds_to_run: int
  recommended_watering_days: int
  plants: List[PlantConfig]


class MoistureSensorConfig(TypedDict):
  id: str
  gpio_pin: int


PUMPS_CONFIG: Dict[str, PumpConfig] = {
  "pump-1": {
    "id": "pump-1",
    "name": "Pump 1",
    "gpio_pin": 11,
    "seconds_to_run": 5,
    "recommended_watering_days": 15,
    "plants": [
      {
        "name": "Orchid",
        "moisture_sensor_id": "",
      },
      {
        "name": "Succulent",
        "moisture_sensor_id": "",
      },
    ],
  },
  "pump-2": {
    "id": "pump-2",
    "name": "Pump 2",
    "gpio_pin": 12,
    "seconds_to_run": 5,
    "recommended_watering_days": 25,
    "plants": [
      {
        "name": "Big Snake Plant",
        "moisture_sensor_id": "",
      },
      {
        "name": "Little Snake Plant",
        "moisture_sensor_id": "",
      },
    ],
  },
  "pump-3": {
    "id": "pump-3",
    "name": "Pump 3",
    "gpio_pin": 13,
    "seconds_to_run": 5,
    "recommended_watering_days": 12,
    "plants": [
      {
        "name": "Fern",
        "moisture_sensor_id": "",
      },
      {
        "name": "Spider Plant",
        "moisture_sensor_id": "",
      },
    ],
  },
  "pump-4": {
    "id": "pump-4",
    "name": "Pump 4",
    "gpio_pin": 15,
    "seconds_to_run": 5,
    "recommended_watering_days": 26,
    "plants": [
      {
        "name": "Waxflower",
        "moisture_sensor_id": "",
      },
    ],
  },
}

MOISTURE_SENSORS_CONFIG: Dict[str, MoistureSensorConfig] = {
  "moisture-sensor-1": {
    "id": "moisture-sensor-1",
    "gpio_pin": 29,
  },
  "moisture-sensor-2": {
    "id": "moisture-sensor-2",
    "gpio_pin": 31,
  },
  "moisture-sensor-3": {
    "id": "moisture-sensor-3",
    "gpio_pin": 33,
  },
  "moisture-sensor-4": {
    "id": "moisture-sensor-4",
    "gpio_pin": 35,
  },
  "moisture-sensor-5": {
    "id": "moisture-sensor-5",
    "gpio_pin": 37,
  },
}
