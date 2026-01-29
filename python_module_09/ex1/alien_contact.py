# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  alien_contact.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 15:43:55 by alebaron        #+#    #+#               #
#  Updated: 2026/01/29 16:54:01 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+

from typing_extensions import Self
from enum import Enum
from datetime import datetime
from typing import Optional

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError:
    print("Error: Install pydantic before execute this program.")
    exit(2)

# +----------------------------------------------------------------+
# |                            Enum                                |
# +----------------------------------------------------------------+

class ContactType(Enum):
    RADIO = "Radio"
    VISUAL = "Visual"
    PHYSICAL = "Physical"
    TELEPATHIC = "Telepathic"

# +----------------------------------------------------------------+
# |                           Modèles                              |
# +----------------------------------------------------------------+

class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        if self.contact_id.startswith("AC") is False:
            raise ValueError("Contact_id must start with \"AC\".")
        if self.contact_type == ContactType.PHYSICAL and self.is_verified is False:
            raise ValueError("Physical contact must be verified.")
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses.")
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should include received messages")

        return self

# +----------------------------------------------------------------+
# |                           Méthodes                             |
# +----------------------------------------------------------------+

def create_contact(data: dict) -> AlienContact | None:

    try:
        contact = AlienContact(**data)
        return contact
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])
        return None

def print_contact(contact: AlienContact | None) -> None:

    if (contact is not None):

        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes%")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: {contact.message_received}")

# +----------------------------------------------------------------+
# |                             Main                               |
# +----------------------------------------------------------------+

if __name__ == "__main__":

    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")

    # === Test 1 : Contact Valide ===

    data = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2003-04-23T22:42:06Z',
        'contact_type': ContactType.RADIO,
        'location': 'Area 51, Nevada',
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 5,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': True
    }

    contact = create_contact(data)
    print_contact(contact)

    print("======================================")

    data = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2003-04-23T22:42:06Z',
        'contact_type': ContactType.TELEPATHIC,
        'location': 'Area 51, Nevada',
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 2,
        'message_received': None,
        'is_verified': False
    }

    contact = create_contact(data)
    print_contact(contact)
