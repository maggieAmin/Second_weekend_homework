class Venue:
    def __init__(self, input_rooms, input_entry_fee):
        self.rooms = input_rooms
        self.entry_fee = input_entry_fee

    def check_guest_in(self, guest, room_name):
        if guest.can_afford(self.entry_fee):
            room = self.rooms[room_name]
            room.check_guest_in(guest)
            guest.remove_money(self.entry_fee)
