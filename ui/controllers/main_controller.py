
def open_settings(self):
    """Inside the main window class open a settings dialog window"""
    dialog = Settings_Window(self)

    if dialog.exec() == QDialog.DialogCode.Accepted:
        username = dialog.username.text()
        print(username)