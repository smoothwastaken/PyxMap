# PyxMap
# Copyright © 2023 Cléry Arque-Ferradou, Nathanaël Lejuste, De Beaumont du Repaire Carla, Chasseigne Ulysse

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import json
from google.cloud import firestore
from google.oauth2 import service_account
from datetime import datetime
import uuid
import random


class Database(object):

    def __init__(self) -> None:
        """Initialize the database connection.
        """
        self._initialize_firestore()

    def _initialize_firestore(self) -> None:
        """Initialize the firestore connection.
        """

        # Get the credentials from the json file.
        credentials_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "resources", "database_credentials.json"
        )

        # Create the credentials.
        with open(credentials_file_path, "r") as f:
            credentials_raw = f.read()
            credentials_json = json.loads(credentials_raw)
            credentials = service_account.Credentials.from_service_account_info(
                credentials_json)

        # Create the firestore client.
        self.db = firestore.Client(credentials=credentials)

    def get_pyxpic(self, pyxpic_id: str) -> dict:
        """Get a pyxpic from the database.

        Args:
            pyxpic_id (str): The id of the pyxpic.

        Returns:
            dict: The pyxpic data.
        """

        # Get the pyxpic from the database.
        doc_ref = self.db.collection("pyxpic").document(pyxpic_id)

        # Return the pyxpic data.
        doc = doc_ref.get()
        return doc.to_dict()

    def add_pyxpic(self, pyxpic_id: str, owner_id: str, raw_image: list) -> str:
        """Add a pyxpic to the database.

        Args:
            pyxpic_id (str): The id of the pyxpic.
            owner_id (str): The id of the owner.
            raw_image (list): The raw image data.
        
        Returns:
            str: The pyxpic id.
        """

        # Verify if the pyxpic id is already used.
        while True:
            if self.is_uuid_already_used(pyxpic_id):
                pyxpic_id = DatabaseUtils.create_random_pyxpic_id()
            else:
                break

        # Add the pyxpic to the database.
        doc_ref = self.db.collection("pyxpic").document(pyxpic_id)
        doc_ref.set(
            {
                "owner_id": owner_id,
                "order_number": len(self.fetch_all_pyxpic()),
                "raw_image": raw_image,
                "date": datetime.now()
            })

        return pyxpic_id

    def update_pyxpic(self, pyxpic_id: str, data: dict) -> None:
        """Update a pyxpic in the database.

        Args:
            pyxpic_id (str): The id of the pyxpic.
            data (dict): The data to update.
        """

        # Get the pyxpic from the database.
        doc_ref = self.db.collection("pyxpic").document(pyxpic_id)

        # Update the pyxpic with the new data.
        doc_ref.update(data)

    def delete_pyxpic(self, pyxpic_id: str) -> None:
        """Delete a pyxpic from the database.

        Args:
            pyxpic_id (str): The id of the pyxpic.
        """

        # Get the pyxpic from the database.
        doc_ref = self.db.collection("pyxpic").document(pyxpic_id)

        # Delete the fetched pyxpic.
        doc_ref.delete()

    def fetch_all_pyxpic(self) -> dict:
        """Fetch all pyxpic from the database.

        Returns:
            dict: The pyxpic data.
        """

        # Get all the pyxpic from the database.
        col_ref = self.db.collection("pyxpic")
        docs = col_ref.stream()

        # Return the all pyxpic data in a dictionary.
        return {doc.id: doc.to_dict() for doc in docs}

    def fetch_user_pyxpic(self, user_id: str) -> dict:
        """Fetch all pyxpic from the database.

        Args:
            user_id (str): The id of the user.

        Returns:
            dict: The pyxpic data.
        """

        # Get all the pyxpic collection.
        col_ref = self.db.collection("pyxpic")

        # Select only the pyxpic of the user.
        docs = col_ref.where("owner_id", "==", user_id).stream()

        # Return the all pyxpic data in a dictionary.
        return {doc.id: doc.to_dict() for doc in docs}

    def is_uuid_already_used(self, pyxpic_id: str) -> bool:
        """Check if a pyxpic id is already used.

        Args:
            pyxpic_id (str): The id of the pyxpic.

        Returns:
            bool: True if the id is already used, False otherwise.
        """

        # Check if the pyxpic id is already used by comparing it to None.
        return self.get_pyxpic(pyxpic_id) is not None


class DatabaseUtils(object):

    @staticmethod
    def create_random_pyxpic_id() -> str:
        """Create a random pyxpic id.

        Returns:
            str: The pyxpic id.
        """

        # Create a random pyxpic id using uuid python module.
        return str(uuid.uuid4())


if __name__ == "__main__":
    db = Database()
    all_pyxpic = db.fetch_all_pyxpic()
    for pyxpic_id, pyxpic_data in all_pyxpic.items():
        db.delete_pyxpic(pyxpic_id)
