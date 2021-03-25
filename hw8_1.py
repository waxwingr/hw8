def acro(phrase):
    es = ""
    final = []
    x = phrase.split(" ")
    for word in x:
        final.append(word[0].upper())
    print(final)

    output = "".join(final)
    return output
