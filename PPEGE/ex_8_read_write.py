def writeToFile(filename:str, text:str):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def appendToFile(filename:str, text:str):
    with open(filename, 'a', encoding = 'utf-8') as file:
        file.write(text)

def readFromFile(filename:str):
    with open(filename, 'r') as file:
        return file.read()
    

if __name__ == "__main__":
    writeToFile('greet.txt', 'Hello!\n')
    appendToFile('greet.txt', 'Goodbye!\n')
    assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'