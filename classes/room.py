class Room:
    def __init__(self, input_name, input_space):
        self.name = input_name
        self.space = input_space
        self.guest_list = []
        self.now_playing = ""
    
    def is_guest_in_room(self, guest):
        if guest in self.guest_list:
            return True
        else:
            return False

    def check_guest_in(self, guest):
        if self.space > 0:
            self.space -= 1
            self.guest_list.append(guest)

    def check_guest_out(self, guest):
        if self.is_guest_in_room(guest):
            self.guest_list.remove(guest)
            self.space += 1

    def add_song(self, song):
        self.now_playing = song.name
