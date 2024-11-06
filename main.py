import tkinter as tk

from Controller.user_controller import UsuarioController
from View.user_view import UsuarioView
from Model.user_model import UsuarioModel


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciamento de Usuários")
    root.geometry("400x300")

    model = UsuarioModel()
    view = UsuarioView(root)
    controller = UsuarioController(view, model)

    root.mainloop()
    model.fechar_conexao()