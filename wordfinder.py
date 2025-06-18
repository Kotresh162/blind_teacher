

class TrieNode:
    def __init__(self):
        self.children = {}
        self.char = None

class TrieModel:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, sequence: str, value: str):
        node = self.root
        for ch in sequence:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.char = value

    def get_final_char(self, sequence: str):
        node = self.root
        for ch in sequence:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node.char

    def decode_input_string(self, input_string: str):
        result = ""
        i = 0
        while i < len(input_string):
            node = self.root
            j = i
            last_valid_char = None
            last_valid_pos = i
            while j < len(input_string) and input_string[j] in node.children:
                node = node.children[input_string[j]]
                j += 1
                if node.char:
                    last_valid_char = node.char
                    last_valid_pos = j
            if last_valid_char:
                result += last_valid_char
                i = last_valid_pos
            else:
                i += 1 
        return result

def build_default_trie():
    trie = TrieModel()
    mappings = {
        "d": "a", "dw": "b", "dk": "c", "do": "e", "dko": "d", "dkw": "f", "dkwo": "g",
        "dwo": "h", "kw": "i", "kow": "j", "dq": "k", "dwq": "l", "dkq": "m", "dkoq": "n",
        "doq": "o", "dwqk": "p", "dwqko": "q", "dwqo": "r", "kwq": "s", "kwqo": "t",
        "dqp": "u", "dwqp": "v", "kowp": "w", "dkqp": "x", "dkoqp": "y", "doqp": "z"
    }
    for k, v in mappings.items():
        trie.insert(k, v)
    return trie
