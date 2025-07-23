import csv


class Client:
    def __init__(self, name, email, profile_picture, db_path="data/clients.txt"):
        self.id = None  # Placeholder for client ID
        self.name = name
        self.email = email
        self.profile_picture = profile_picture
        self.db_path = db_path

    def save(self):
        """Saves the client to the "database" file, appending a new row with the client's details."""

        with open(self.db_path, "a", encoding="utf-8") as db_file:
            db_file.write(f"{self.name},{self.email},{self.profile_picture}\n")
            print(f"Client {self.name} with email {self.email} saved.")

    def delete(self):
        """Deletes the client from the "database" file, by replacing the file's contents with all rows except the one with the client's ID."""

        # Read all rows from the database file
        rows_to_keep = []
        with open(self.db_path, "r", encoding="utf-8") as db_file:
            reader = csv.reader(db_file)
            for row in reader:
                client_id = row[0]
                if client_id != self.id:
                    rows_to_keep.append(row)

        # Write back all rows except the one with the client's ID
        with open(self.db_path, "w", encoding="utf-8") as db_file:
            writer = csv.writer(db_file)
            writer.writerows(rows_to_keep)

        print(f"Client {self.name} deleted.")

    def update(self, new_name=None, new_email=None):
        """Updates the client's details in the "database" file."""
        with open(self.db_path, "r", encoding="utf-8") as db_file:
            rows = db_file.readlines()
        with open(self.db_path, "w", encoding="utf-8") as db_file:
            for row in rows:
                if row.startswith(self.name):
                    if new_name:
                        self.name = new_name
                    if new_email:
                        self.email = new_email
                    db_file.write(f"{self.name},{self.email},{self.profile_picture}\n")
                else:
                    db_file.write(row)
        print(f"Client {self.name} deleted.")
