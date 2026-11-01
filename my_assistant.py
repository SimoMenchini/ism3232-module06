# my_assistant.py
# Author: Simone Menchini

HANDOFF_WORDS = ["cancel", "refund", "billing", "injury"]


class StudioAssistant:
    """A mock fitness studio FAQ assistant. Replies come from keyword rules."""

    def __init__(self, name, instructions, faq_tool):
        """Set up one assistant with its own name, instructions, tool, and history."""
        self.name = name  # Store the assistant's display name
        self.instructions = (
            instructions  # Store the system instructions for later modules
        )
        self.faq_tool = (
            faq_tool  # Composition: store the FAQTool object inside the assistant
        )
        self.history = []  # Initialize an empty list to record every conversation turn

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        # Append the incoming user message with its role to the conversation history
        self.history.append({"role": "user", "content": user_message})
        # Determine the appropriate response using our keyword rules
        reply = self.choose_reply(user_message)
        # Append the assistant's reply with its role to the conversation history
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""
        text = user_message.lower()
        # Check handoff words first so sensitive requests always go to a human
        if self.needs_human(text):
            return "I can't handle account billing or medical issues. I'm passing you to the studio manager."
        # Trigger the FAQ tool when the user asks a question or mentions faq/info
        if "faq" in text or "info" in text or "?" in text:
            return self.faq_reply(user_message)
        # Greet the user if they say hello
        if "hello" in text or "hi" in text:
            return f"Hello! I'm {self.name}. Ask me a question about hours, membership, or towels."
        # Safe fallback reply for unrecognized inputs
        return "I'm not sure how to help with that. Ask me a question about hours, membership, or towels."

    def needs_human(self, text):
        """Return True if the message asks about billing, cancellations, or injuries."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def faq_reply(self, user_message):
        """Use the FAQ tool to answer a question about the studio."""
        # Ask the tool to identify which topic the user is asking about
        topic = self.faq_tool.find_topic(user_message)
        # If no known topic is found, return a helpful prompt instead of crashing
        if topic is None:
            return "Which topic? I can answer questions about hours, membership, or towels."
        # Look up the answer for the matched topic and format the response
        answer = self.faq_tool.answer_for(topic)
        return f"Here is our info on {topic}: {answer}"
