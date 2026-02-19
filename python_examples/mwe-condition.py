from datetime import datetime, timezone


# Define the attribute class with a creation_date field
class Attributes:
    def __init__(self, creation_date=None):
        self.creation_date = creation_date


# Define the file class with an attributes field
class File:
    def __init__(self, attributes=None):
        self.attributes = attributes


# Generate a fake creation timestamp (current UTC time)
fake_creation_timestamp = datetime.now(tz=timezone.utc).timestamp()

# Create a file object with attributes containing the creation_date
file = File(attributes=Attributes(creation_date=fake_creation_timestamp))

ctime = None
if file.attributes:
    if file.attributes.creation_date:
        ctime = datetime.fromtimestamp(
            file.attributes.creation_date, tz=timezone.utc
        )
        print(ctime)
