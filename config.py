from typing import TypedDict, List, Dict


class PlantConfig(TypedDict):
  id: str
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
        "id": "orchid",
        "name": "Orchid",
        "moisture_sensor_id": None,
      },
      {
        "id": "succulent",
        "name": "Succulent",
        "moisture_sensor_id": "moisture-sensor-2",
      },
    ],
  },
  "pump-2": {
    "id": "pump-2",
    "name": "Pump 2",
    "gpio_pin": 12,
    "seconds_to_run": 10,
    "recommended_watering_days": 25,
    "plants": [
      {
        "id": "big-snake",
        "name": "Big Snake Plant",
        "moisture_sensor_id": None,
      },
      {
        "id": "little-snake",
        "name": "Little Snake Plant",
        "moisture_sensor_id": "moisture-sensor-1",
      },
    ],
  },
  "pump-3": {
    "id": "pump-3",
    "name": "Pump 3",
    "gpio_pin": 13,
    "seconds_to_run": 20,
    "recommended_watering_days": 12,
    "plants": [
      {
        "id": "fern",
        "name": "Fern",
        "moisture_sensor_id": "moisture-sensor-3",
      },
      {
        "id": "spider",
        "name": "Spider Plant",
        "moisture_sensor_id": "moisture-sensor-5",
      },
    ],
  },
  "pump-4": {
    "id": "pump-4",
    "name": "Pump 4",
    "gpio_pin": 15,
    "seconds_to_run": 10,
    "recommended_watering_days": 26,
    "plants": [
      {
        "id": "wax-flower",
        "name": "Waxflower",
        "moisture_sensor_id": "moisture-sensor-4",
      },
    ],
  },
}

MOISTURE_SENSORS_CONFIG: Dict[str, MoistureSensorConfig] = {
  "moisture-sensor-1": {
    "id": "moisture-sensor-1",
    "gpio_pin": 16,
  },
  "moisture-sensor-2": {
    "id": "moisture-sensor-2",
    "gpio_pin": 18,
  },
  "moisture-sensor-3": {
    "id": "moisture-sensor-3",
    "gpio_pin": 22,
  },
  "moisture-sensor-4": {
    "id": "moisture-sensor-4",
    "gpio_pin": 7,
  },
  "moisture-sensor-5": {
    "id": "moisture-sensor-5",
    "gpio_pin": 3,
  },
}
