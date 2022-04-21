import datetime
import time
from errors import *


class OneNote:
    def __init__(self, note_id, memo, tags, time):
        self.note_id = note_id
        self.memo = memo
        self.tags = tags
        self.date = datetime.date.today()
        self.time = datetime.datetime.today()


class NotesApp:

    def __init__(self):
        self.last_id = 1
        self.Notes = []

    def search_for_notes(self, search_filter):
        result = [note for note in sorted(self.Notes, key=lambda x: x.time, reverse=True) if
                  search_filter in note.memo or search_filter in note.tags]
        if len(result) == 0:
           raise NoNotesFoundError()
        return result

    def show_notes(self, content=None):
        if content is None:
            content = []

            if not content:
                content = list(sorted(self.Notes, key=lambda x: x.time, reverse=True))
            if len(content) == 0:
                raise NoNotesError()
            for note in content:
                print(f"""Note id: {note.note_id}
                      Note tags: {note.tags}
                      Note text: {note.memo}
                      Note time: {note.time}
                      """)

        return content

    def min_notes(self, left, right):
        right = datetime.datetime.today()
        left = datetime.datetime.today() + datetime.timedelta(minutes=10)
        content = list(sorted(self.Notes, key=lambda x: x.time, reverse=True))

        mn = right
        res_id = -1
        for i in range(len(content)):
            if left <= content[i].time <= right:
                if content[i].time < mn:
                    res_id = i
                    mn = content[i].time
        print(f"""Note id: {content[res_id].note_id}
                  Note tags: {content[res_id].tags}
                  Note text: {content[res_id].memo}
                  Note time: {content[res_id].time}
                  """)

    def min(self):
        left, right = input(), input()
        self.min_notes(left, right)

    def search_notes(self):
        k = input("Search for: ")
        note = self.search_for_notes(k)
        self.show_notes(note)

    def add_note(self, memo=None, tags=None):
        if not memo:
            memo = input("Enter a memo: ")
        if not tags:
            tags = input("Enter tag: ")
        self.Notes.append(OneNote(self.last_id, memo, tags, time=datetime.datetime.now()))
        self.last_id += 1
        print("Your note has been added.")
        # time.sleep(10)
        return self.Notes[self.last_id - 2]

    def modify_note(self, note_id=None, memo=None, tags=None):

        if not note_id:
            note_id = int(input("Enter a note id: "))
        if not memo:
            memo = input("Enter a memo: ")
        if not tags:
            tags = input("Enter tags: ")
        for i in self.Notes:
            note = i
            if note.note_id == note_id:
                if memo:
                    note.memo = memo
                    note.time = datetime.datetime.now()
                if tags:
                    note.tags = tags
                    note.time = datetime.datetime.now()
        return self.Notes[self.last_id - 2]
