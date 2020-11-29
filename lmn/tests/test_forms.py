from django.test import TestCase

from django.contrib.auth.models import User
from lmn.forms import VenueSearchForm, ArtistSearchForm, NoteSearchForm, NewNoteForm, UserRegistrationForm, ProfileForm
import string

# Test that forms are validating correctly, and don't accept invalid data


class NewNoteFormTests(TestCase):

    def test_missing_title_is_invalid(self):
        form_data = {"text": "blah blah"}
        form = NewNoteForm(form_data)
        self.assertFalse(form.is_valid())

        invalid_titles = list(string.whitespace) + ['   ', '\n\n\n', '\t\t\n\t']

        for invalid_title in invalid_titles:
            form_data = {"title": invalid_title, "text": "blah blah"}
            form = NewNoteForm(form_data)
            self.assertFalse(form.is_valid())

    def test_missing_text_is_invalid(self):
        form_data = {"title": "blah blah"}
        form = NewNoteForm(form_data)
        self.assertFalse(form.is_valid())

        invalid_texts = list(string.whitespace) + ['   ', '\n\n\n', '\t\t\n\t']

        for invalid_text in invalid_texts:
            form_data = { "title": "blah blah", "text": invalid_text}
            form = NewNoteForm(form_data)
            self.assertFalse(form.is_valid())

    def test_title_too_long_is_invalid(self):
        # Max length is 200
        form_data = {"title": "a" * 201}
        form = NewNoteForm(form_data)
        self.assertFalse(form.is_valid())

    def test_text_too_long_is_invalid(self):
        # Max length is 1000
        form_data = {"title": "a" * 1001}
        form = NewNoteForm(form_data)
        self.assertFalse(form.is_valid())

    def test_ok_title_and_length_is_valid(self):
        form_data = {"title": "blah blah", "text": "blah, blah, blah."}
        form = NewNoteForm(form_data)
        self.assertTrue(form.is_valid())


class RegistrationFormTests(TestCase):

    # missing fields

    def test_register_user_with_valid_data_is_valid(self):
        form_data = {'username': 'bob', 'email': 'bob@bob.com', 'first_name' : 'bob', 'last_name' : 'whatever', 'password1': 'q!w$er^ty6ui7op', 'password2' : 'q!w$er^ty6ui7op'}
        form = UserRegistrationForm(form_data)
        self.assertTrue(form.is_valid())

    def test_register_user_with_missing_data_fails(self):
        form_data = {'username': 'bob', 'email' : 'bob@bob.com', 'first_name' : 'bob', 'last_name' : 'whatever', 'password1': 'q!w$er^ty6ui7op', 'password2' : 'q!w$er^ty6ui7op'}
        # Remove each key-value from dictionary, assert form not valid
        for field in form_data.keys():
            data = dict(form_data)
            del(data[field])
            form = UserRegistrationForm(data)
            self.assertFalse(form.is_valid())

    def test_register_user_with_password_mismatch_fails(self):
        form_data = {'username': 'another_bob', 'email': 'bob@bob.com', 'first_name' : 'bob', 'last_name': 'whatever', 'password1': 'q!w$er^ty6ui7op', 'password2': 'dr%$ESwsdgdfh'}
        form = UserRegistrationForm(form_data)
        self.assertFalse(form.is_valid())

    def test_register_user_with_email_already_in_db_fails(self):

        # Create a user with email bob@bob.com
        bob = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        bob.save()

        # attempt to create another user with same email
        form_data = {'username': 'another_bob', 'email': 'bob@bob.com', 'first_name': 'bob', 'last_name': 'whatever', 'password1': 'q!w$er^ty6ui7op', 'password2': 'q!w$er^ty6ui7op'}
        form = UserRegistrationForm(form_data)
        self.assertFalse(form.is_valid())

    def test_register_user_with_username_already_in_db_fails(self):

        # Create a user with username bob
        bob = User(username='bob', email='bob@bob.com')
        bob.save()

        # attempt to create another user with same username
        form_data = { 'username': 'bob', 'email': 'another_bob@bob.com', 'first_name': 'bob', 'last_name': 'whatever', 'password1': 'q!w$er^ty6ui7op', 'password2': 'q!w$er^ty6ui7op'}
        form = UserRegistrationForm(form_data)
        self.assertFalse(form.is_valid())

    # TODO make this test pass!
    def test_register_user_with_username_already_in_db_case_insensitive_fails(self):

        # Create a user with username bob
        bob = User(username='bob', email='bob@bob.com')
        bob.save()

        invalid_username = ['BOB', 'BOb', 'Bob', 'bOB', 'bOb', 'boB']

        for invalid in invalid_username:
            # attempt to create another user with same username
            form_data = {'username': invalid, 'email': 'another_bob@bob.com', 'first_name': 'bob', 'last_name': 'whatever', 'password1': 'q!w$er^ty6ui7op', 'password2': 'q!w$er^ty6ui7opq!w$er^ty6ui7op'}
            form = UserRegistrationForm(form_data)
            self.assertFalse(form.is_valid())

    # TODO make this test pass!
    def test_register_user_with_email_already_in_db_case_insensitive_fails(self):

        # Create a user with username bob
        bob = User(username='bob', email='bob@bob.com')
        bob.save()

        invalid_email = ['BOB@bOb.com', 'BOb@bob.cOm', 'Bob@bob.coM', 'BOB@BOB.COM', 'bOb@bob.com', 'boB@bob.com']

        for invalid in invalid_email:
            # attempt to create another user with same username
            form_data = {'username': 'another_bob', 'email': invalid, 'first_name': 'bob', 'last_name': 'whatever', 'password1' : 'q!w$er^ty6ui7op', 'password2': 'q!w$er^ty6ui7op'}
            form = UserRegistrationForm(form_data)
            self.assertFalse(form.is_valid())


class LoginFormTests(TestCase):

    # TODO username not case sensitive - bob and BOB and Bob are the same
   
    pass

class SearchFormTests(TestCase):

    def setUp(self):
        self.empty_name = {"search_name": ""}
        self.long_string = {"search_name": 201 * 'a'}
        self.normal_string = {"search_name": "search something"}

    def test_missing_venue_search_is_invalid(self):
        form = VenueSearchForm(self.empty_name)
        self.assertFalse(form.is_valid())

    def test_long_venue_search_is_invalid(self):
        form = VenueSearchForm(self.long_string)
        self.assertFalse(form.is_valid())

    def test_venue_search_is_valid(self):
        form = VenueSearchForm(self.normal_string)
        self.assertTrue(form.is_valid())

    def test_missing_artist_search_is_invalid(self):
        form = ArtistSearchForm(self.empty_name)
        self.assertFalse(form.is_valid())

    def test_long_artist_search_is_invalid(self):
        form = ArtistSearchForm(self.long_string)
        self.assertFalse(form.is_valid())

    def test_artist_search_is_valid(self):
        form = ArtistSearchForm(self.normal_string)
        self.assertTrue(form.is_valid())

    def test_missing_note_search_is_invalid(self):
        form = NoteSearchForm(self.empty_name)
        self.assertFalse(form.is_valid())

    def test_long_note_search_is_invalid(self):
        form = NoteSearchForm(self.long_string)
        self.assertFalse(form.is_valid())

    def test_note_search_is_valid(self):
        form = NoteSearchForm(self.normal_string)
        self.assertTrue(form.is_valid())


class ProfileFormTests(TestCase):
    def test_more_than_500_characters_is_invalid(self):
        five01 = 'a' * 501
        form_data = { "bio": five01 }
        form = ProfileForm(form_data)
        self.assertFalse(form.is_valid())

    def test_empty_is_invalid(self):
        empty = ''
        form_data = { "bio": empty }
        form = ProfileForm(form_data)
        self.assertTrue(form.is_valid())
