def canCreateWordFromLetters(letters, word):
    for character in word:
        if character not in letters:
            return False
        else:
            letters = letters.replace(character, "", 1)
    return True

def main():
    task = open("challenge.txt", "r")
    for line in task:
        args = line.split()
        print(canCreateWordFromLetters(args[0], args[1]))
    task.close()

main()
