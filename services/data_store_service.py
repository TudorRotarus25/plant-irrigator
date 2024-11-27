from datetime import datetime
import sqlite3
import time
from sqlite3 import Connection, Cursor

import uuid


class DataStoreService:
  connection: Connection

  def __init__(self):
    self.connection = sqlite3.connect("plant.db")

  def __del__(self):
    self.connection.close()

  def record_watering(self, pump_id: str) -> None:
    cursor: Cursor = self.connection.cursor()

    record_id: str = str(uuid.uuid4())
    timestamp: int = int(round(time.time()))
    cursor.execute(
      "INSERT INTO watering_log(id, timestamp, pump_id) VALUES (?, ?, ?)",
      (record_id, timestamp, pump_id,))

    self.connection.commit()

  def get_latest_watering(self, pump_id: str) -> datetime | None:
    cursor: Cursor = self.connection.cursor()

    result = cursor.execute(
      "SELECT timestamp FROM watering_log WHERE pump_id = ? ORDER BY timestamp DESC",
      (pump_id,))
    fetched = result.fetchone()

    if not fetched:
      return None

    return datetime.fromtimestamp(int(fetched[0]))
