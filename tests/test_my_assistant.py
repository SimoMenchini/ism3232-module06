# test_my_assistant.py
# Author: Simone Menchini

from my_assistant import StudioAssistant
from my_tool import FAQTool


def make_assistant():
    """Build a fresh assistant with its own tool for each test."""
    tool = FAQTool(
        {
            "hours": "We are open daily from 6:00 am to 9:00 pm.",
            "membership": "Monthly memberships are $45 with no annual contract.",
        }
    )
    return StudioAssistant("CoachBot", "Be helpful.", tool)


def test_faq_question_uses_the_tool():
    assistant = make_assistant()
    reply = assistant.respond("What are your hours?")
    assert (
        reply == "Here is our info on hours: We are open daily from 6:00 am to 9:00 pm."
    )


def test_question_without_known_topic_asks_for_one():
    assistant = make_assistant()
    assert "Which topic?" in assistant.respond("Can you give me some info?")


def test_billing_request_goes_to_a_human():
    assistant = make_assistant()
    assert "studio manager" in assistant.respond(
        "Please cancel my membership and give me a refund"
    )


def test_unknown_request_gets_a_safe_reply():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("I like lifting weights")


def test_history_grows_by_two_each_turn():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("What are your hours?")
    assert len(assistant.history) == 4
