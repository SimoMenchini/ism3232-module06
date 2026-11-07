from appointment_tool import AppointmentBook

from appointment_bot import AppointmentHelper
from mock_model import MockModel


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_helper():
    """Build a fresh helper with its own tool for each test."""
    book = AppointmentBook({"monday": "9:00 am and 2:30 pm", "friday": "none"})
    return AppointmentHelper("Robin", "Be clear.", book, MockModel())


def test_unknown_request_gets_a_safe_reply():
    book = AppointmentBook({"monday": "9:00 am and 2:30 pm"})
    helper = AppointmentHelper("Robin", "Be clear.", book, SilentModel())
    assert "try again" in helper.respond("What is your favorite color?")


def test_other_messages_go_to_the_model():
    helper = make_helper()
    assert helper.respond("hello") == "Hello! How can I help you today?"
