# my_main.py
# Author: Simone Menchini

from my_assistant import StudioAssistant
from my_tool import FAQTool

FAQ_DATA = {
    "hours": "We are open daily from 6:00 am to 9:00 pm.",
    "membership": "Monthly memberships are $45 with no annual contract.",
    "towels": "Complimentary workout towels are provided at the front desk.",
}

faq_tool = FAQTool(FAQ_DATA)
assistant = StudioAssistant(
    "coachBot",
    "You help members of Bayshore Fitness Studio with common studio questions.",
    faq_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
