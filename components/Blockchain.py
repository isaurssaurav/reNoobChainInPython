from components.utils import get_difficulty_string,print_message
from env import DIFFICULTY, SECRET_KEY


class Blockchain:

    def __init__(self):
        self.blocks =[]

    def add_block(self,block):
        current_mining_block = len(self.blocks) + 1
        block.mine_block(DIFFICULTY, current_mining_block)
        self.blocks.append(block)

    def validate_block_chain(self):
        for i in range(len(self.blocks)-1):
            current_block = self.blocks[i+1]
            prev_block = self.blocks[i]

            target_hash = get_difficulty_string(DIFFICULTY)

            if(current_block.hash != current_block.calculated_hash()):
                print('Current hash is not equal')
                return False

            if(prev_block.hash != current_block.previous_hash):
                print('Previous hash is not equal')
                return False

            if(current_block.hash[0:DIFFICULTY] != target_hash):
                print('This block hasnot been mined')
                return False

        return True

    def show_data(self,aes):
        for block in self.blocks:
            print_message(aes.decrypt(block.data,SECRET_KEY))