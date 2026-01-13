"""
Fichier : stream_processor.py
Auteur  : alebaron
Date    : 2026/01/12
"""


# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


# +----------------------------------------------------------------+
# |                       Classe abstraite                         |
# +----------------------------------------------------------------+

class StreamBase(ABC):

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self, stream_id: str, type_event: str):
        super().__init__()
        self.__stream_id = stream_id
        self.__type_event = type_event

    # +------------------------------------------------------------+
    # |                         Accesseurs                         |
    # +------------------------------------------------------------+

    def get_stream_id(self) -> str:
        return self.__stream_id

    def get_type_event(self) -> str:
        return self.__type_event

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is not None:
            data_batch = [item for item in data_batch if criteria in item]

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.__stream_id, "type": self.__type_event}

# +----------------------------------------------------------------+
# |                       Classe Héritaire                         |
# +----------------------------------------------------------------+

class SensorStream(StreamBase):

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self, stream_id: int):
        super().__init__(f"SENSOR_{stream_id:03d}", "Environmental Data")

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def process_batch(self, data_batch: List[Any]) -> str:

        lst_temp = []
        
        for data in data_batch:
            if type(data) is str and data.startswith("temp"):
                data_split = data.split(":")

                if len(data_split) == 2:
                    try:
                        temp = float(data_split[1])
                        lst_temp.append(temp)
                    except ValueError:
                        print("Erreur lors de la conversion de la température.")
                
        if len(lst_temp) == 0:
            return (f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"avg temp: no temperature data found")
        else:
            return (f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"avg temp: {sum(lst_temp) / len(lst_temp)}°C")


class TransactionStream(StreamBase):

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self, stream_id: int):
        super().__init__(f"TRANS_{stream_id:03d}", "Financial Data")

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def process_batch(self, data_batch: List[Any]) -> str:

        lst_sell = []
        lst_buy = []
        
        for data in data_batch:

            data_split = data.split(":")

            if type(data) is str:
                
                if len(data_split) == 2:
                    try:
                        temp = int(data_split[1])
                        
                        if data.startswith("sell"):
                            lst_sell.append(temp)
                        elif data.startswith("buy"):
                            lst_buy.append(temp)
                    except ValueError:
                        pass
        
        if len(lst_sell) == 0 & len(lst_buy) == 0:
            return (f"Transaction analysis: {len(data_batch)} readings processed, "
                    f"net flow: no data")
        else:
            return (f"Transaction analysis: {len(data_batch)} readings processed, "
                    f"net flow: {sum(lst_buy) - sum(lst_sell)} units")

class EventStream(StreamBase):

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self, stream_id: int):
        super().__init__(f"EVENT_{stream_id:03d}", "System Events")

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def process_batch(self, data_batch: List[Any]) -> str:

        nb_error = 0
        
        for data in data_batch:
            if type(data) is str and data == ("error"):
                nb_error += 1
                
        return (f"Event analysis: {len(data_batch)} events, "
                f"{nb_error} error detected")


# +----------------------------------------------------------------+
# |                         Autres classes                         |
# +----------------------------------------------------------------+

class StreamProcessor():

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self):
        self.__streams = []

    # +------------------------------------------------------------+
    # |                         Accesseurs                         |
    # +------------------------------------------------------------+

    def get_streams(self) -> List[StreamBase]:
        return self.__streams

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def add_streams(self, stream: StreamBase) -> None:
        self.__streams.append(stream)

    def process(self, batch_data: Dict[str, List[any]]) -> None:
        print("Batch 1 Results:")

        for stream in self.__streams:
            stream_data = batch_data.get(stream.get_stream_id())
            if stream_data is not None:
                result = stream.process_batch(stream_data)
                print(f"- {result}")
            else:
                print(f"- No data found for stream {stream.get_stream_id()}")

# +----------------------------------------------------------------+
# |                             Main                               |
# +----------------------------------------------------------------+

if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    # === Test 1 : SensorStream ===

    print("Initializing Sensor Stream...")

    data_sensor = ["temp:30.2", "temp:22.5", "humidity:65", "pressure:1013"]
    formatted_data = ", ".join(data_sensor)

    processor_sensor = SensorStream(1)
    stats = processor_sensor.get_stats()
    result = processor_sensor.process_batch(data_sensor)

    print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
    print(f"Processing sensor batch: [{formatted_data}]")
    print(result)

    # === Test 2 : Transaction Stream ===

    print("\nInitializing Transaction Stream...")

    data_sensor = ["buy:100", "sell:150", "buy:75"]
    formatted_data = ", ".join(data_sensor)

    processor_transaction = TransactionStream(1)
    stats = processor_transaction.get_stats()
    result = processor_transaction.process_batch(data_sensor)

    print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
    print(f"Processing sensor batch: [{formatted_data}]")
    print(result)

    # === Test 3 : Event Stream ===

    print("\nInitializing Event Stream...")

    data_sensor = ["login", "error", "logout"]
    formatted_data = ", ".join(data_sensor)

    processor_event = EventStream(1)
    stats = processor_event.get_stats()
    result = processor_event.process_batch(data_sensor)

    print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
    print(f"Processing sensor batch: [{formatted_data}]")
    print(result)

    # === Test 4 : Polymorph Stream ===

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_streams(processor_sensor)
    processor.add_streams(processor_transaction)
    processor.add_streams(processor_event)

    batch_data = {
        "SENSOR_001": ["temp:22.5", "humidity:65"],
        "TRANS_001": ["buy:100", "sell:150", "buy:75", "buy:20"],
        "EVENT_001": ["login", "error", "logout"]
    }

    processor.process(batch_data=batch_data)

    print("\nStream filtering active: High-priority data only")
    crit_sensors = processor_sensor.filter_data(batch_data["SENSOR_001"])
    large_trans = processor_transaction.filter_data(batch_data["TRANS_001"],
                                                    criteria="150")
    print(f"Filtered results: {len(crit_sensors)} critical sensor alerts, "
          f"{len(large_trans)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
