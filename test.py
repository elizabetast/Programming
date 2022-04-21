import time
import unittest
from unittest import TestCase
from notes_applic import NotesApp
from errors import *


class Testing(TestCase):

    def setUp(self) -> None:
        self.note = NotesApp()

    def test_add_note(self):
        self.assertEqual(self.note.add_note("lizaveta", "me").memo, "lizaveta")
        self.assertEqual(self.note.Notes[0].tags, "me")
        self.assertEqual(self.note.Notes[0].note_id, 1)

    def test_modify_note(self):
        self.note.add_note("katerina", "sister")
        self.assertEqual(self.note.modify_note(1, "lizaveta", "me").memo, "lizaveta")
        self.assertEqual(self.note.Notes[0].tags, "me")
        self.assertEqual(self.note.Notes[0].note_id, 1)

    def test_notes_sort(self):
        self.note.add_note("lizaveta", "me")
        self.note.add_note("katerina", "sister")
        time.sleep(1)
        self.note.modify_note(1, "tatsiana", "mommy")
        self.assertEqual(self.note.show_notes()[0].note_id, 1)

    def test_search_error(self):
        with self.assertRaises(NoNotesFoundError):
            self.note.search_for_notes("1")


if __name__ == '__main__':
    unittest.main()
