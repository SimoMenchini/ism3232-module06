# my_tool.py
# Author: Simone Menchini


class FAQTool:
    """A tool that looks up answers to common fitness studio questions."""

    def __init__(self, faq_data):
        """Store the dictionary of topics and answers."""
        # Save the dictionary passed in as an instance attribute on self
        self.faq_data = faq_data

    def find_topic(self, text):
        """Return the first known FAQ topic mentioned in text, or None."""
        # Loop through each topic key stored in our dictionary
        for topic in self.faq_data:
            # Convert the user's text to lowercase to match topics case-insensitively
            if topic in text.lower():
                return topic
        # Return None if no known topic keyword appears in the text
        return None

    def answer_for(self, topic):
        """Return the FAQ answer for one topic, or None if the topic is unknown."""
        # Check if the requested topic exists in the dictionary before looking it up
        if topic in self.faq_data:
            return self.faq_data[topic]
        return None
