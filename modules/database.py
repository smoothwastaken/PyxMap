import os
import json
from google.cloud import firestore
from google.oauth2 import service_account
from datetime import datetime
import uuid


class Database(object):

    def __init__(self) -> None:
        """Initialize the database connection.
        """
        self._initialize_firestore()

    def _initialize_firestore(self):
        """Initialize the firestore connection.
        """
        credentials_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..", "resources", "database_credentials.json"
        )

        with open(credentials_file_path, "r") as f:
            credentials_raw = f.read()
            credentials_json = json.loads(credentials_raw)
            credentials = service_account.Credentials.from_service_account_info(
                credentials_json)

        self.db = firestore.Client(credentials=credentials)

    def get_pyxpic(self, pyxpic_id):
        """Get a pyxpic from the database.

        Args:
            pyxpic_id (str): The id of the pyxpic.

        Returns:
            dict: The pyxpic data.
        """
        doc_ref = self.db.collection("pyxpic").document(pyxpic_id)
        doc = doc_ref.get()
        return doc.to_dict()

    def add_pyxpic(self, pyxpic_id, owner_id, raw_image):
        """Add a pyxpic to the database.

        Args:
            pyxpic_id (str): The id of the pyxpic.
            owner_id (str): The id of the owner.
            raw_image (list): The raw image data.
        
        Returns:
            str: The pyxpic id.
        """
        doc_ref = self.db.collection("pyxpic").document(pyxpic_id)
        doc_ref.set(
            {
                "owner_id": owner_id,
                "raw_image": raw_image,
                "date": datetime.now()
            })

        return pyxpic_id

    def update_pyxpic(self, pyxpic_id, data):
        """Update a pyxpic in the database.

        Args:
            pyxpic_id (str): The id of the pyxpic.
            data (dict): The data to update.
        """
        doc_ref = self.db.collection("pyxpic").document(pyxpic_id)
        doc_ref.update(data)

    def delete_pyxpic(self, pyxpic_id):
        """Delete a pyxpic from the database.

        Args:
            pyxpic_id (str): The id of the pyxpic.
        """
        doc_ref = self.db.collection("pyxpic").document(pyxpic_id)
        doc_ref.delete()

    def fetch_all_pyxpic(self):
        """Fetch all pyxpic from the database.

        Returns:
            dict: The pyxpic data.
        """
        col_ref = self.db.collection("pyxpic")
        docs = col_ref.stream()
        return {doc.id: doc.to_dict() for doc in docs}

    def fetch_user_pyxpic(self, user_id):
        """Fetch all pyxpic from the database.

        Args:
            user_id (str): The id of the user.

        Returns:
            dict: The pyxpic data.
        """
        col_ref = self.db.collection("pyxpic")
        docs = col_ref.where("owner_id", "==", user_id).stream()
        return {doc.id: doc.to_dict() for doc in docs}


class DatabaseUtils(object):

    @staticmethod
    def create_random_pyxpic_id():
        """Create a random pyxpic id.

        Returns:
            str: The pyxpic id.
        """
        return str(uuid.uuid4())


if __name__ == "__main__":
    db = Database()
    all_pyxpic = db.fetch_all_pyxpic()
