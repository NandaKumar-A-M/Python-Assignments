def pig_latin(sentence):
    words = sentence.split()

    pig_latin_words = []
    for word in words:
        pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)

    pig_latin_sentence = ' '.join(pig_latin_words)
    return pig_latin_sentence

input_sentence = input("Enter a sentence: ")
pig_latin_result = pig_latin(input_sentence)
print("Pig Latin conversion:", pig_latin_result)

