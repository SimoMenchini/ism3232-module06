# appointment_tool.py
# Author: Simone Menchini

# appointment_tool.py


class AppointmentBook:
    def __init__(self, slots=None):
        self.slots = slots if slots is not None else {}

    def is_available(self, time_slot):
        return self.slots.get(time_slot, True)

    def book(self, time_slot):
        if self.is_available(time_slot):
            self.slots[time_slot] = False
            return True
        return False
