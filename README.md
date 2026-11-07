## Mini-Project: Bayshore Fitness Studio FAQ Assistant

`StudioAssistant` is a small business assistant for a fitness studio that answers common visitor questions about gym hours, membership pricing, and towel service using a separate `FAQTool` lookup class. The assistant is a mock because it does not connect to an AI language model; instead, it relies on `if` statements and lowercase keyword matching to choose pre-written responses. Requests mentioning keywords like `cancel`, `refund`, `billing`, or `injury` are immediately handed off to a human studio manager because financial changes and medical advice carry legal and financial risks that require human judgment. Keeping the FAQ dictionary inside `FAQTool` rather than inside `StudioAssistant` separates the studio's data from the conversation logic. If this system were connected to real customer data without proper authentication, a simple keyword rule could accidentally expose private member billing records or allow one user to cancel another member's account.



## Assistant Reflection

The model answered well when asked "Where is the office?", correctly stating it is at 40 Harbor Street on the second floor. When asked an unsupported question like "Do you prepare business returns?", it appropriately refused by stating it did not know. Schedule checks and booking actions ("book", "cancel", "reschedule") were kept entirely in code rather than handed to the model. Keeping these actions in code prevents hallucinations that could falsely confirm appointments or offer slots that do not exist.

# Run assistant
python3 appointment_main.py