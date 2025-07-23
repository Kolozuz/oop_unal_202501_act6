import tkinter as tk
from tkinter import *
from tkinter import ttk
#from models.client import Client

DATABASE_PATH = "data/clients.txt"

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Client Management App")
        #self.clients = [Client]
        self.client_frames = []
        self.client_images = []
        self.setup_ui()

    def setup_ui(self):

        self.load_clients()

        self.add_button_icon = tk.PhotoImage(
            file="media/user-plus-solid.png"
        )  # Keep a reference!
        add_button = ttk.Button(
            self.root, text="wtf", image=self.add_button_icon
        )
        add_button_row = (len(self.client_frames) / 2) - 1
        add_button_col = len(self.client_frames) + (len(self.client_frames) % 2) - 1
        add_button.grid(
            row=int(add_button_row), column=int(add_button_col), padx=10, pady=10
        )

    def load_clients(self):
        """
        Creates and displays a card for each client with a profile picture and buttons for actions.
        Currently displayed cards are removed before new ones are created.
        """

        clients = [
            {
                "profile_pic": "media/avatar1.png",
                "name": "John Doe",
                "email": "",
            },
            {"profile_pic": "media/avatar2.png", "name": "Jane Smith", "email": ""},
            {"profile_pic": "media/avatar3.png", "name": "Alice Johnson", "email": ""},
            {"profile_pic": "media/avatar4.png", "name": "Bob Brown", "email": ""},
            {"profile_pic": "media/avatar5.png", "name": "Michael Smith", "email": ""},
        ]

        row = 0
        col = 0

        for client in clients:

            # Create and place a new frame for each client
            new_frame = Frame(
                self.root, width=200, height=200, borderwidth=1, relief=SOLID
            )
            profile_picture = tk.PhotoImage(file=client["profile_pic"])
            ttk.Label(
                new_frame, text=client["name"], image=profile_picture, compound=TOP
            ).pack()

            self.client_images.append(new_frame)
            self.client_frames.append(profile_picture)

            buttons_container = ttk.Frame(new_frame)
            ttk.Button(buttons_container, text="🖉").pack(side=LEFT)
            ttk.Button(buttons_container, text="🗑").pack()
            buttons_container.pack()

            new_frame.grid(row=row, column=col, padx=10, pady=10)

            if col == 1:
                col = 0
                row += 1

            else:
                col += 1
    
    def add_client(self):
        pass

    def remove_client(self):
        pass 

    def update_client(self, client):
        """Opens a form to update the client's details."""

        print(f"Opening update form for {client.name}")


    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
