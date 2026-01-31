# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_crew.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 16:55:35 by alebaron        #+#    #+#               #
#  Updated: 2026/01/31 11:25:50 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from enum import Enum
from datetime import datetime

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
    from typing_extensions import Self
except ModuleNotFoundError:
    print("Error: Install pydantic before execute this program.")
    exit(2)


# +----------------------------------------------------------------+
# |                            Enum                                |
# +----------------------------------------------------------------+

class Rank(Enum):
    CADET = "Cadet"
    OFFICER = "Officer"
    LIEUTENANT = "Lieutenant"
    CAPTAIN = "Captain"
    COMMANDER = "Commander"

# +----------------------------------------------------------------+
# |                           Modèles                              |
# +----------------------------------------------------------------+


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=3, max_length=150)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember]
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_validation(self) -> Self:
        if self.mission_id.startswith("M") is False:
            raise ValueError("Mission_id must start with \"M\".")

        nb_high_rank = 0
        experienced = 0

        for crew in self.crew:
            if crew.rank == Rank.CAPTAIN or crew.rank == Rank.COMMANDER:
                nb_high_rank += 1
            if crew.years_experience >= 5:
                experienced += 1
            if crew.is_active is False:
                raise ValueError("All crew members must be active.")

        if nb_high_rank < 1:
            raise ValueError("Must have at least one Commander or Captain.")

        if self.duration_days > 365 and experienced / len(self.crew) < 0.5:
            raise ValueError("Long missions (> 365 days) need 50% "
                             "experienced crew (5+ years)")

        return self


# +----------------------------------------------------------------+
# |                          Méthodes                              |
# +----------------------------------------------------------------+

def create_mission(data: dict) -> SpaceMission | None:

    try:
        mission = SpaceMission(**data)
        return mission
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])
        return None


def print_mission(mission: SpaceMission | None) -> None:

    if (mission is not None):

        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: €{mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for crew in mission.crew:
            print(f"- {crew.name} ({crew.rank.value}) - {crew.specialization}")


# +----------------------------------------------------------------+
# |                            Main                                |
# +----------------------------------------------------------------+

if __name__ == "__main__":

    print("Space Mission Crew Validation")
    print("=========================================")

    # === Test 1 : mission Valide ===
    data = {
        'mission_id': 'M2024_Mars',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': datetime.now(),
        'duration_days': 900,
        'crew': [
            {
                'member_id': 'Saconnor',
                'name': 'Sarah Connor',
                'rank': Rank.COMMANDER,
                'age': 35,
                'specialization': 'Mission Command',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'Josmith',
                'name': 'John Smith',
                'rank': Rank.LIEUTENANT,
                'age': 65,
                'specialization': 'Navigation',
                'years_experience': 9,
                'is_active': True
            },
            {
                'member_id': 'Aljohnson',
                'name': 'Alice Johnson',
                'rank': Rank.OFFICER,
                'age': 23,
                'specialization': 'Engineering',
                'years_experience': 5,
                'is_active': True
            }
        ],
        'mission_status': 'in progress',
        'budget_millions': 2500.0
    }

    mission = create_mission(data)
    print_mission(mission)

    print("=========================================")

    # === Test 1 : mission Invalide ===

    data = {
        'mission_id': 'M2024_Mars',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': datetime.now(),
        'duration_days': 900,
        'crew': [
            {
                'member_id': 'Saconnor',
                'name': 'Sarah Connor',
                'rank': Rank.LIEUTENANT,
                'age': 35,
                'specialization': 'Mission Command',
                'years_experience': 9,
                'is_active': True
            },
            {
                'member_id': 'Josmith',
                'name': 'John Smith',
                'rank': Rank.LIEUTENANT,
                'age': 65,
                'specialization': 'Navigation',
                'years_experience': 6,
                'is_active': True
            },
            {
                'member_id': 'Aljohnson',
                'name': 'Alice Johnson',
                'rank': Rank.OFFICER,
                'age': 23,
                'specialization': 'Engineering',
                'years_experience': 6,
                'is_active': True
            }
        ],
        'mission_status': 'in progress',
        'budget_millions': 2500.0
    }

    mission = create_mission(data)
    print_mission(mission)
