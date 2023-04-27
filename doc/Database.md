# Database.py Documentation

This documentation provides an overview of the `database.py` file, its classes, methods, and usage.

## Table of Contents

- [Classes](#classes)
  - [Database](#database)
  - [DatabaseUtils](#databaseutils)
- [Usage](#usage)
- [License](#license)

## Classes

### Database

The `Database` class is responsible for handling the database connection and operations.

#### Methods

- `__init__(self) -> None`

  Initializes the database connection.

- `_initialize_firestore(self) -> None`

  Initializes the firestore connection.

- `get_pyxpic(self, pyxpic_id: str) -> dict`

  Gets a pyxpic from the database.

  - `pyxpic_id (str)`: The id of the pyxpic.
  - Returns: `dict`: The pyxpic data.

- `add_pyxpic(self, pyxpic_id: str, owner_id: str, raw_image: list) -> str`

  Adds a pyxpic to the database.

  - `pyxpic_id (str)`: The id of the pyxpic.
  - `owner_id (str)`: The id of the owner.
  - `raw_image (list)`: The raw image data.
  - Returns: `str`: The pyxpic id.

- `update_pyxpic(self, pyxpic_id: str, data: dict) -> None`

  Updates a pyxpic in the database.

  - `pyxpic_id (str)`: The id of the pyxpic.
  - `data (dict)`: The data to update.

- `delete_pyxpic(self, pyxpic_id: str) -> None`

  Deletes a pyxpic from the database.

  - `pyxpic_id (str)`: The id of the pyxpic.

- `fetch_all_pyxpic(self) -> dict`

  Fetches all pyxpic from the database.

  - Returns: `dict`: The pyxpic data.

- `fetch_user_pyxpic(self, user_id: str) -> dict`

  Fetches all pyxpic from the database for a specific user.

  - `user_id (str)`: The id of the user.
  - Returns: `dict`: The pyxpic data.

- `is_uuid_already_used(self, pyxpic_id: str) -> bool`

  Checks if a pyxpic id is already used.

  - `pyxpic_id (str)`: The id of the pyxpic.
  - Returns: `bool`: True if the id is already used, False otherwise.

### DatabaseUtils

The `DatabaseUtils` class is a collection of utility functions for the `Database` class.

#### Methods

- `create_random_pyxpic_id() -> str`

  Creates a random pyxpic id.

  - Returns: `str`: The pyxpic id.

## Usage

Here's an example of how to use the `Database` class:

```python
from database import Database

# Initialize the database connection.
db = Database()

# Create a random pyxpic id.
pyxpic_id = DatabaseUtils.create_random_pyxpic_id()

# Add a new pyxpic to the database.
owner_id = "user123"
raw_image = [["#", "@", "$"], ["%", "&", "*"]]
db.add_pyxpic(pyxpic_id, owner_id, raw_image)

# Get the pyxpic data.
pyxpic_data = db.get_pyxpic(pyxpic_id)
print(pyxpic_data)

# Update the pyxpic data.
new_data = {"raw_image": [["#", "@", "$"], ["%", "&", "#"]]}
db.update_pyxpic(pyxpic_id, new_data)

# Delete the pyxpic from the database.
db.delete_pyxpic(pyxpic_id)
```

This example will create a random pyxpic id, add a new pyxpic to the database, get and update the pyxpic data, and delete the pyxpic from the database.

## License

This program is free software under the terms of the GNU General Public License v3.0.