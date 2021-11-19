from .utils import get_difficulty_string, print_message, convert_to_sha256
from datetime import datetime


class Block:
    hash = None
    previous_hash = None
    data = None
    timestamp = None
    nonce = 0

    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.hash = self.calculated_hash()

    def calculated_hash(self):
        text_to_hash = self.previous_hash + str(self.timestamp) + str(self.nonce) + str(self.data)
        calculated_hash = convert_to_sha256(text_to_hash, True)
        return calculated_hash

    def mine_block(self,difficulty, current_mining_block):
        print_message('Trying to mine the Block ' + str(current_mining_block))

        target_difficulty = get_difficulty_string(difficulty)

        while (self.hash[0:difficulty] != target_difficulty):
            self.nonce +=1
            self.hash = self.calculated_hash()

        print('Block',current_mining_block,'is mined',self.hash)

