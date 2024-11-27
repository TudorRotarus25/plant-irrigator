from typing import List

from datetime import datetime, timedelta

from textual.app import App, ComposeResult, RenderResult
from textual.containers import HorizontalGroup, VerticalScroll, VerticalGroup
from textual.widgets import Header, Footer, Button, Label
from textual.reactive import reactive

from config import PumpConfig, PUMPS_CONFIG, PlantConfig
from services.data_store_service import DataStoreService
from services.pump_service import PumpService

data_store_service = DataStoreService()


class PlantContainer(VerticalGroup):
  plant_config: PlantConfig
  pump_config: PumpConfig
  last_watering_message = reactive("")

  def watch_last_watering_message(self):
    print(f"last_watering_message changed: {self.last_watering_message}")

  def compose(self) -> ComposeResult:
    yield Label(self.plant_config["name"], classes="plant-title")
    yield HorizontalGroup(
        Label("Last watered: ", id="plant-watered-timestamp-label"),
        Label(self.last_watering_message, id="plant-watered-timestamp-value")
    )

    water_recommendation = f"{self.pump_config['recommended_watering_days']} days"

    yield HorizontalGroup(
        Label("Should water every: ", id="plant-watered-recommended-label"),
        Label(water_recommendation, id="plant-watered-recommended-value")
    )
    yield HorizontalGroup(
        Label("Moisture level: ", id="plant-needs-watering-label"),
        Label("None", id="plant-needs-watering-value")
    )


class PumpListItem(HorizontalGroup):
  pump_config: PumpConfig

  def _on_water_start(self, pump_service: PumpService) -> None:
    self.add_class("watering")
    pump_service.start_watering()

  def _get_last_watered_message(self) -> str:
    last_watering: datetime = data_store_service.get_latest_watering(
        self.pump_config["id"])

    if last_watering is None:
      return ""

    datetime_diff: timedelta = datetime.now() - last_watering

    if datetime_diff.days < 1:
      minutes_ago: int = int(round(datetime_diff.seconds / 60))
      return f"{minutes_ago} minutes ago"

    return f"{datetime_diff.days} days ago"

  def _on_water_end(self, pump_service: PumpService) -> None:
    self.remove_class("watering")
    pump_service.stop_watering()
    data_store_service.record_watering(self.pump_config["id"])
    for container in self.query(PlantContainer):
      print(container)
      container.last_watering_message = "just now"

  def on_button_pressed(self, event: Button.Pressed) -> None:
    print(f"pressed {event.button.id}")
    pump_service = PumpService(self.pump_config["gpio_pin"])
    self._on_water_start(pump_service)
    self.set_timer(self.pump_config["seconds_to_run"],
                   lambda: self._on_water_end(pump_service))

  def compose(self) -> ComposeResult:
    for plant in self.pump_config["plants"]:
      container = PlantContainer(id=f"plant-item-{plant['id']}")
      container.plant_config = plant
      container.pump_config = self.pump_config
      container.last_watering_message = self._get_last_watered_message()
      yield container

    yield Button("Water", id="water", variant="success")


class PlantApp(App):
  CSS_PATH = "plant-irrigation.tcss"
  BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

  def compose(self) -> ComposeResult:
    pump_items: List[PumpListItem] = []

    for pump_config in PUMPS_CONFIG.values():
      item = PumpListItem()
      item.pump_config = pump_config
      pump_items.append(item)

    yield Header()
    yield Footer()
    yield VerticalScroll(*pump_items, id="main-container")

  def action_toggle_dark(self) -> None:
    self.theme = (
      "textual-dark" if self.theme == "textual-light" else "textual-light"
    )


if __name__ == '__main__':
  app = PlantApp()
  app.run()
