import tkinter as tk
from tkinter import messagebox
import database
import openpyxl


def add_destination():
    macro = macro_entry.get()
    uf = uf_entry.get()
    regiao_turistica = regiao_turistica_entry.get()
    municipio = municipio_entry.get()
    cluster = cluster_entry.get()

    if macro and uf and regiao_turistica and municipio and cluster:
        database.insert_destination(macro, uf, regiao_turistica, municipio, cluster)
        messagebox.showinfo("Success", "Destination added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")


def clear_entries():
    macro_entry.delete(0, tk.END)
    uf_entry.delete(0, tk.END)
    regiao_turistica_entry.delete(0, tk.END)
    municipio_entry.delete(0, tk.END)
    cluster_entry.delete(0, tk.END)


def see_all_destinations():
    destinations = database.get_all_destinations()
    destinations_text.config(state=tk.NORMAL)
    destinations_text.delete(1.0, tk.END)
    for destination in destinations:
        destinations_text.insert(tk.END, f"{destination}\n")
    destinations_text.config(state=tk.DISABLED)


def export_to_excel():
    destinations = database.get_all_destinations()
    if destinations:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Destinations"

        # Add headers
        headers = ["ID", "Macro", "UF", "Touristic Region", "Municipality", "Cluster"]
        sheet.append(headers)

        # Fill in data
        for destination in destinations:
            sheet.append(
                [destination[0], destination[1], destination[2], destination[3], destination[4], destination[5]])

        # Save the Excel file
        workbook.save("destinations.xlsx")
        messagebox.showinfo("Success", "Data exported to destinations.xlsx")
    else:
        messagebox.showwarning("Warning", "No data to export.")


# Create the main window
root = tk.Tk()
root.title("Tourism in Brazil App")

# Labels
macro_label = tk.Label(root, text="Macro:")
uf_label = tk.Label(root, text="UF:")
regiao_turistica_label = tk.Label(root, text="Touristic Region:")
municipio_label = tk.Label(root, text="Municipality:")
cluster_label = tk.Label(root, text="Cluster:")

macro_label.grid(row=0, column=0)
uf_label.grid(row=1, column=0)
regiao_turistica_label.grid(row=2, column=0)
municipio_label.grid(row=3, column=0)
cluster_label.grid(row=4, column=0)

# Entry fields
macro_entry = tk.Entry(root)
uf_entry = tk.Entry(root)
regiao_turistica_entry = tk.Entry(root)
municipio_entry = tk.Entry(root)
cluster_entry = tk.Entry(root)

macro_entry.grid(row=0, column=1)
uf_entry.grid(row=1, column=1)
regiao_turistica_entry.grid(row=2, column=1)
municipio_entry.grid(row=3, column=1)
cluster_entry.grid(row=4, column=1)

# Buttons
add_button = tk.Button(root, text="Add Destination", command=add_destination)
see_all_button = tk.Button(root, text="See All Destinations", command=see_all_destinations)
export_button = tk.Button(root, text="Export to Excel", command=export_to_excel)

add_button.grid(row=5, column=0, columnspan=2)
see_all_button.grid(row=6, column=0, columnspan=2)
export_button.grid(row=7, column=0, columnspan=2)

# Text box to display destinations
destinations_text = tk.Text(root, state=tk.DISABLED, width=40, height=10)
destinations_text.grid(row=8, column=0, columnspan=2)

# Start the GUI
root.mainloop()
