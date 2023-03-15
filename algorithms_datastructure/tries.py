
# nodes of the Trie data object
class TrieNode:
    def __init__(self) -> None:
        self.children = {}

# the overall class object
class Trie:
    def __init__(self)->None:
        self.root = TrieNode()
    
    def search(self, word:str):
        currentNode = self.root
        
        # for each character in word 
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            
            else:
                return None
            
        return currentNode
    
    def insertion(self, word:str):
        currentNode = self.root
        
        # for each character in word search if it already exists
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = TrieNode()
                currentNode.children[char] = newNode
                currentNode = newNode
                
        currentNode.children["*"] = None
    
    def collect_words(self, node=None, word='', words=[]):
        # first argument is the node we start from
        # second argument is the word we are building
        # third argument is the list of words we built
        
        currentNode = node or self.root
        
        for key, childNode in currentNode.children.items():
            if key == '*':
                words.append(word)
            else:
                self.collect_words(childNode, word+key, words)
        
        return words
    
    def autocomplete(self, prefix:str):
        currentNode = self.search(prefix)
        
        if not currentNode:
            return None

        return self.collect_words(currentNode)

    def traverse_all(self, node=None):
        # traverse each node and print each key
        currentNode = node or self.root
        
        for key, childnode in currentNode.children.items():
            print(key)
            
            if key != "*":
                self.traverse_all(childnode)
    
    def autocorrect(self, text:str):
        currentNode = self.search(text)
        
        # if the text is not in the trie, return the word with longest prefix
        if not currentNode:
            for sub_prefix in text[::-1]:
                if self.search(sub_prefix):
                    word_ends = self.collect_words(self.search(sub_prefix))
                    return [sub_prefix + word_end for word_end in word_ends]
        
        if currentNode:
            return text
        
if __name__ == "__main__":
    
    trie = Trie()
    
    # test insertion
    trie.insertion("can")
    trie.insertion("cat")
    trie.insertion("bad")
    trie.insertion("bake")
    
    # test auto-complete
    # print(trie.autocomplete('ca'))
    
    # print(trie.autocorrect("can"))
    
    # test auto_correct
    print(trie.autocorrect("cap"))