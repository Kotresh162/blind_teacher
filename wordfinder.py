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

    def build_interactive_sequence(self) -> str:
        current_node = self.root
        sequence = ""

        while True:
            ch = input("Enter next character (or press Enter to finish sequence): ").strip()
            if not ch:
                print(" Input ended for this character.")
                break

            if ch in current_node.children:
                sequence += ch
                current_node = current_node.children[ch]
                print(f" '{ch}' is valid. Current sequence: '{sequence}'")
                if current_node.char:
                    print(f"✔️ Sequence '{sequence}' maps to: '{current_node.char}'")
            else:
                print(f" '{ch}' is invalid. Trying suggestions...")
                self.suggest_nearest_completions(sequence)
                return sequence  # stop early if invalid
        return sequence

    def get_final_char(self, sequence: str) -> str | None:
        node = self.root
        for ch in sequence:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node.char

    def suggest_nearest_completions(self, sequence: str):
        node = self.root
        for ch in sequence:
            if ch not in node.children:
                print(f"Cannot continue from '{sequence}'. No such path.")
                return
            node = node.children[ch]

        suggestions = []

        def dfs(n, path):
            if n.char:
                suggestions.append(("".join(path), n.char))
            for ch, child in n.children.items():
                dfs(child, path + [ch])

        dfs(node, list(sequence))

        if suggestions:
            print(f" Suggestions for prefix '{sequence}':")
            for s, val in suggestions:
                print(f"🔹 '{s}' → '{val}'")
        else:
            print(f" No suggestions found for '{sequence}'")


def build_string_from_input(trie: TrieModel) -> str:
    result = ""
    print("\n Start entering characters (custom sequences). One mapped character per sequence.\n")
    while True:
        sequence = trie.build_interactive_sequence()
        if not sequence:
            break
        final_char = trie.get_final_char(sequence)
        if final_char:
            result += final_char
        else:
            print(f"No exact mapping for '{sequence}', skipping.")
    return result


if __name__ == "__main__":
    trie = TrieModel()

    # Insert your language rules
    trie.insert("d", "a")
    trie.insert("dw", "b")
    trie.insert("dk", "c")
    trie.insert("do", "e")
    trie.insert("dko", "d")
    trie.insert("dkw", "f")
    trie.insert("dkwo", "g")
    trie.insert("dwo", "h")
    trie.insert("kw", "i")
    trie.insert("kow", "j")
    trie.insert("dq", "k")
    trie.insert("dwq", "l")
    trie.insert("dkq", "m")
    trie.insert("dkoq", "n")
    trie.insert("doq", "o")
    trie.insert("dwqk", "p")
    trie.insert("dwqko", "q")
    trie.insert("dwqo", "r")
    trie.insert("kwq", "s")
    trie.insert("kwqo", "t")
    trie.insert("dqp", "u")
    trie.insert("dwqp", "v")
    trie.insert("kowp", "w")
    trie.insert("dkqp", "x")
    trie.insert("dkoqp", "y")
    trie.insert("doqp", "z")

    final_string = build_string_from_input(trie)
    print(f"\n Final end string is : '{final_string}' ")
