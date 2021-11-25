from components.utils import convert_obj_to_string, print_message
from components.AESEncrypt import AESEncrypt
from components.AESEncryptCBC import AESEncryptCBC
from components.Blockchain import Blockchain
from components.Student import Student
from components.Block import Block
from env import DIFFICULTY, SECRET_KEY

blockchain = Blockchain()
# aes = AESEncrypt()
aesCBC = AESEncryptCBC()

def noob_chain():
    print_message('Difficulty level is ' + str(DIFFICULTY))

    make_student_and_add_to_blockchain(1, "Nikhil Lidl", "Psychology")
    make_student_and_add_to_blockchain(2, "Aslog Kaufland", "Business")
    make_student_and_add_to_blockchain(3, "Aristoteles Netto", "Literature")

    if blockchain.validate_block_chain():
        print_message('Block Chain is still valid!')

    blockchain.show_data()

def make_student_and_add_to_blockchain(student_id,student_name,student_major):
    # Make student object
    student = Student(student_id, student_name, student_major)
    # Encrypt student
    encrypted_student = aesCBC.encrypt(convert_obj_to_string(student), SECRET_KEY)
    # Add previous_hash if !isGenesis
    previous_hash = "0"  if len(blockchain.blocks) == 0 else blockchain.blocks[-1].hash
    # Add to block chain
    blockchain.add_block(Block(encrypted_student,previous_hash))

if __name__ == '__main__':
    noob_chain()

