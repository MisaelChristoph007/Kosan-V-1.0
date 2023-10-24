import tkinter as tk
from tkinter import ttk

class CRUDDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("IbuKost 1.0")

        self.data = []

        self.create_gui()

    def create_gui(self):
        # Label
        label = ttk.Label(self.root, text="IbuKost 1.0", font=("Monospace", 16))
        label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Input Fields
        self.nama_var = tk.StringVar()
        self.tanggal_var = tk.StringVar()
        self.uang_var = tk.StringVar()
        self.asal_var = tk.StringVar()
        self.status_var = tk.StringVar()

        ttk.Label(self.root, text="Nama:").grid(row=1, column=0, padx=10)
        ttk.Entry(self.root, textvariable=self.nama_var).grid(row=1, column=1, padx=10)

        ttk.Label(self.root, text="Tanggal Masuk:").grid(row=2, column=0, padx=10)
        ttk.Entry(self.root, textvariable=self.tanggal_var).grid(row=2, column=1, padx=10)

        ttk.Label(self.root, text="Jumlah Uang Dibayar:").grid(row=3, column=0, padx=10)
        ttk.Entry(self.root, textvariable=self.uang_var).grid(row=3, column=1, padx=10)

        ttk.Label(self.root, text="Asal Daerah:").grid(row=4, column=0, padx=10)
        ttk.Entry(self.root, textvariable=self.asal_var).grid(row=4, column=1, padx=10)

        ttk.Label(self.root, text="Status Pembayaran:").grid(row=5, column=0, padx=10)
        ttk.Combobox(self.root, textvariable=self.status_var, values=["Belum Lunas", "Lunas"]).grid(row=5, column=1, padx=10)

        # Buttons
        ttk.Button(self.root, text="Tambah", command=self.add_data).grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Edit", command=self.edit_data).grid(row=7, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Hapus", command=self.delete_data).grid(row=8, column=0, columnspan=2, pady=10)

        ttk.Label(self.root, text="").grid(row=7, column=0, padx=10)

        # Table
        columns = ("Nama", "Tanggal Masuk", "Jumlah Uang Dibayar", "Asal Daerah", "Status Pembayaran")
        self.table = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col)
        self.table.grid(row=9, column=0, columnspan=2, padx=10)
        self.table.bind("<ButtonRelease-1>", self.on_select)

    def add_data(self):
        nama = self.nama_var.get()
        tanggal = self.tanggal_var.get()
        uang = self.uang_var.get()
        asal = self.asal_var.get()
        status = self.status_var.get()

        if nama and tanggal and uang and asal and status:
            self.data.append((nama, tanggal, uang, asal, status))
            self.update_table()
            self.clear_inputs()

    def update_table(self):
        self.table.delete(*self.table.get_children())
        for row in self.data:
            self.table.insert("", "end", values=row)

    def clear_inputs(self):
        self.nama_var.set("")
        self.tanggal_var.set("")
        self.uang_var.set("")
        self.asal_var.set("")
        self.status_var.set("")

    def on_select(self, event):
        item = self.table.selection()
        if item:
            selected_data = self.table.item(item, "values")
            self.nama_var.set(selected_data[0])
            self.tanggal_var.set(selected_data[1])
            self.uang_var.set(selected_data[2])
            self.asal_var.set(selected_data[3])
            self.status_var.set(selected_data[4])

    def edit_data(self):
        item = self.table.selection()
        if item:
            selected_data = self.table.item(item, "values")
            if selected_data:
                index = self.data.index(selected_data)
                self.data[index] = (self.nama_var.get(), self.tanggal_var.get(), self.uang_var.get(), self.asal_var.get(), self.status_var.get())
                self.update_table()
                self.clear_inputs()

    def delete_data(self):
        item = self.table.selection()
        if item:
            selected_data = self.table.item(item, "values")
            if selected_data:
                self.data.remove(selected_data)
                self.update_table()
                self.clear_inputs()

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDDemo(root)
    root.mainloop()
