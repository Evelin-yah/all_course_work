sentence = input().split()
command = input()

while command != "Stop":
    if command.startswith('Delete'):
        current_command, index = command.split()
        index = int(index)
        if index + 1 < len(sentence):
            del sentence[index + 1]
    elif command.startswith('Swap'):
        current_command, word1, word2 = command.split()
        if word1 in sentence and word2 in sentence:
            for index in range(len(sentence)):
                if sentence[index] == word1:
                    sentence[index] = word2
                elif sentence[index] == word2:
                    sentence[index] = word1
    elif command.startswith('Put'):
        current_command, word, index = command.split()
        index = int(index)
        if index - 1 >= 0:
            if len(sentence) >= index:
                sentence.insert(index - 1, word)
            if len(sentence) == index:
                sentence.insert(index, word)
    elif command == 'Sort':
        sentence.sort()
        sentence.reverse()
    elif command.startswith('Replace'):
        current_command, word1, word2 = command.split()
        if word2 in sentence:
            for i in range(len(sentence)):
                if sentence[i] == word2:
                    sentence[i] = word1
    command = input()

print(' '.join(sentence))
