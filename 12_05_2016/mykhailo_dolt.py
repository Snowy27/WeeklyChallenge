def canCreateWordFromLetters(letters, word):
    lettersList = list(letters)
    for character in word:
        if character not in lettersList:
            return False
        else:
            lettersList.remove(character)
    return True

def main():
    task = open("challenge.txt", "r")
    for line in task:
        args = line.split()
        print(canCreateWordFromLetters(args[0], args[1]))
    task.close()

main()
