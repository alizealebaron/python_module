# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_station.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 10:57:29 by alebaron        #+#    #+#               #
#  Updated: 2026/01/29 17:24:54 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


import sys
from datetime import datetime
from typing import Optional
try:
    from pydantic import BaseModel, Field, ValidationError
except ModuleNotFoundError:
    print("Error: Install pydantic before execute this program.")
    sys.exit(2)


# +----------------------------------------------------------------+
# |                           Modèles                              |
# +----------------------------------------------------------------+

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


# +----------------------------------------------------------------+
# |                           Méthodes                             |
# +----------------------------------------------------------------+

def create_station(data: dict) -> SpaceStation | None:

    try:
        station = SpaceStation(**data)
        return station
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])
        return None


def print_station(station: SpaceStation | None) -> None:

    if (station is not None):
        ope = ('Operational'
               if station.is_operational else 'Nonoperational')

        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {ope}")


def main():

    date = datetime.now()

    # === Test 1 : Bonne configuration ===

    station_list = {
        'station_id': 'ISS001',
        'name': 'International Space Station',
        'crew_size': 6,
        'power_level': 85.5,
        'oxygen_level': 92.3,
        'last_maintenance': date,
        'is_operational': True
    }

    station = create_station(station_list)
    print_station(station)

    print("\n========================================")

    station_list = {
        'station_id': 'ISS001',
        'name': 'International Space Station',
        'crew_size': 25,
        'power_level': 85.5,
        'oxygen_level': 92.3,
        'last_maintenance': date,
        'is_operational': True
    }

    station = create_station(station_list)
    print_station(station)


# +----------------------------------------------------------------+
# |                             Main                               |
# +----------------------------------------------------------------+

if __name__ == "__main__":

    print("Space Station Data Validation")
    print("========================================")

    main()
