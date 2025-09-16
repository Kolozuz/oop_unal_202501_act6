import tkinter as tk
from tkinter import *
from tkinter import ttk
from math import ceil

from models.client import Client

DATABASE_PATH = "data/clients.txt"
ADD_BUTTON_ICON_PATH = "media/user-plus-solid.png"
NUMBER_OF_COLUMNS = 3

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Client Management App")
        self.add_button = None
        self.clients = [Client]
        self.client_frames = []
        self.client_images = []
        self.setup_ui()

    def setup_ui(self):

        client_register_window = ttk.Frame(self.root, borderwidth=2, relief=GROOVE)
        selected_client = StringVar()
        pfp_picker_values = ["avatar1.png", "avatar2.png", "avatar3.png"]
        ttk.OptionMenu(client_register_window, selected_client, *pfp_picker_values).pack()
        ttk.Label(client_register_window, text="Name").pack()
        ttk.Label(client_register_window, text="Email").pack()

        main_window = ttk.Frame(self.root, borderwidth=2, relief=GROOVE)
        self.add_button_icon = tk.PhotoImage(file=ADD_BUTTON_ICON_PATH)
        self.add_button = ttk.Button(
            main_window, image=self.add_button_icon, command=client_register_window.tkraise
        )
        self.add_button.grid(column=0, row=0, padx=10, pady=10)

        self.load_clients(main_window)

        # Stack frames
        main_window.grid(column=1, row=0, sticky=NSEW)
        client_register_window.grid(column=1, row=0)

        # Center window content
        self.root.columnconfigure(0, weight=1)

    def load_clients(self, main_window):
        """
        Creates and displays a card for each client with a profile picture and buttons for actions.
        Currently displayed cards are removed before new ones are created.
        """

        clients = [
            {
                "profile_pic": "media/avatar1.png",
                "name": "John Doe",
                "email": "jdoe@hipnet.es",
            },
            {
                "profile_pic": "media/avatar2.png",
                "name": "Jane Smith",
                "email": "jsmith@hipnet.es",
            },
            {
                "profile_pic": "media/avatar3.png",
                "name": "Alice Johnson",
                "email": "ajohnson@hipnet.es",
            },
            {
                "profile_pic": "media/avatar4.png",
                "name": "Bob Brown",
                "email": "bbrown@hipnet.es",
            },
            {
                "profile_pic": "media/avatar5.png",
                "name": "Michael Smith",
                "email": "msmith@hipnet.es",
            },
        ]
        # clients = []

        row = 0
        col = 0

        for client in clients:

            new_frame = Frame(
                main_window, width=200, height=200, borderwidth=2, relief=GROOVE
            )
            profile_picture = tk.PhotoImage(file=client["profile_pic"])
            ttk.Label(
                new_frame, text=client["name"], image=profile_picture, compound=TOP
            ).pack()
            ttk.Label(new_frame, text=client["email"]).pack()

            self.client_images.append(new_frame)
            self.client_frames.append(profile_picture)

            buttons_container = ttk.Frame(new_frame)
            ttk.Button(buttons_container, text="🖉").pack(side=LEFT)
            ttk.Button(buttons_container, text="🗑").pack()
            buttons_container.pack()

            new_frame.grid(row=row, column=col, padx=10, pady=10)

            if col == NUMBER_OF_COLUMNS - 1:
                col = 0
                row += 1

            else:
                col += 1
        
        # Recalculate the position for the "Add Client" button
        if len(self.client_frames) % NUMBER_OF_COLUMNS == 0:
            add_button_row = ceil(len(self.client_frames) / NUMBER_OF_COLUMNS)
            add_button_col = 1
        else:
            add_button_row = ceil(len(self.client_frames) / NUMBER_OF_COLUMNS) - 1
            add_button_col = len(self.client_frames) % NUMBER_OF_COLUMNS

        self.add_button.grid(
            row=int(add_button_row), column=int(add_button_col), padx=10, pady=10
        )

    def add_client(self):
        # Show Client Registration Form
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
