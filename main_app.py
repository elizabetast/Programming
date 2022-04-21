from app_handler import NotesHandler
from notes_applic import NotesApp

app = NotesApp()
notes_handler = NotesHandler(app)
notes_handler.handler_app()
