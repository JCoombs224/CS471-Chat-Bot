class actor:
    def __init__(self, phone_number):
        self.phone = phone_number
        self.prev_msgs = []
        self.state = "begin"

    def save_msg(self, msg):
        self.prev_msgs.append(msg)

    def change_state(self, new_state):
        self.state = new_state

