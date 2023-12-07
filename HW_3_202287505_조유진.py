def replace_first_word(sentence, word_to_replace, replacement_word):
    new_sentence = ""
    replaced = False
    words = sentence.split(" ")
    for word in words:
        if word == word_to_replace and not replaced:
            new_sentence += replacement_word + " "
            replaced = True
        else:
            new_sentence += word + " "

    if word_to_replace not in sentence:
        print("The word you entered is not in the sentence.")
    else:
        print(new_sentence.strip())


sentence = input("Enter a sentence: ")
word_to_replace = input("Enter word to replace: ")
replacement_word = input("Enter replacement word: ")

replace_first_word(sentence, word_to_replace, replacement_word)