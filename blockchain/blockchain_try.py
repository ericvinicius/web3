import hashlib

def to_sha256(txt: str) -> str:
    return hashlib.sha256(txt.encode('utf-8')).hexdigest()

class Block:
    value: str
    current_hash: str
    previous_hash: str
    
    def __init__(self, value: str, previous_hash: str, current_hash: str) -> None:
        self.value = value
        self.previous_hash = previous_hash
        self.current_hash = current_hash
    
    def to_string(self) -> str:
        ret = f"value: {self.value}\n"
        ret += f"p_hash: {self.previous_hash}\n" 
        ret += f"c_hash: {self.current_hash}\n"
        return ret
        

class Blockchain:
    blocks = list[Block]
    
    def __init__(self) -> None:
        self.blocks = []
    
    def add_value(self, value: str) -> Block:
        previous_hash = "0"
        if len(self.blocks) > 0:
            previous_hash = self.blocks[-1].current_hash
            
        current_hash = to_sha256(f"{previous_hash}_{value}")     
        new_block = Block(value=value, previous_hash=previous_hash, current_hash=current_hash)
        self.blocks.append(new_block)
        return new_block

    def is_valid_blockchain(self) -> bool:
        if len(self.blocks) == 1:
            return self.blocks[0].previous_hash == "0"
    
        for i in range(1, len(self.blocks)-1):
            previous = self.blocks[i-1]
            current = self.blocks[i]
            
            if previous.current_hash != current.previous_hash:
                return False
        
            if not self.is_valid_block(previous):
                return False
            
            if not self.is_valid_block(current):
                return False
            
        return True

    def is_valid_block(self, block: Block) -> bool:
        return to_sha256(f"{block.previous_hash}_{block.value}") != block.current_hash

    def to_string(self) -> str:
        ret = ""
        for block in self.blocks:
            ret += block.to_string()
            ret += f"\n  |\n"
            ret += f"  V\n\n"
        
        ret += "NONE"
        return ret
            
    

if __name__ == '__main__':
    bc = Blockchain()
    
    bc.add_value("1")
    bc.add_value("2")
    bc.add_value("3")
    
    print(bc.to_string())
    print(bc.is_valid_blockchain())
    
    block = bc.blocks[1]
    block.value = 20
    
    print(bc.to_string())
    print(bc.is_valid_blockchain())

    
    