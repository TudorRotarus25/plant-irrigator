from typing import List

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll, VerticalGroup
from textual.widgets import Header, Footer, Button, Label

from config import PumpConfig, PUMPS_CONFIG, PlantConfig
from services.pump_service import PumpService


class PlantContainer(VerticalGroup):
  plant_config: PlantConfig

  def compose(self) -> ComposeResult:
    yield Label(self.plant_config["name"], classes="plant-title")
    yield HorizontalGroup(
        Label("Last watered: ", id="plant-watered-timestamp-label"),
        Label("2 days ago", id="plant-watered-timestamp-value")
    )
    yield HorizontalGroup(
        Label("Needs watering: ", id="plant-needs-watering-label"),
        Label("YES", id="plant-needs-watering-value")
    )


class PumpListItem(HorizontalGroup):
  pump_config: PumpConfig

  def _on_water_start(self, pump_service: PumpService) -> None:
    self.add_class("watering")
    pump_service.start_watering()

  def _on_water_end(self, pump_service: PumpService) -> None:
    self.remove_class("watering")
    pump_service.stop_watering()

  def on_button_pressed(self, event: Button.Pressed) -> None:
    print(f"pressed {event.button.id}")
    pump_service = PumpService(self.pump_config["gpio_pin"])
    self._on_water_start(pump_service)
    self.set_timer(self.pump_config["seconds_to_run"], lambda : self._on_water_end(pump_service))

  def compose(self) -> ComposeResult:
    for plant in self.pump_config["plants"]:
      container = PlantContainer()
      container.plant_config = plant
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
