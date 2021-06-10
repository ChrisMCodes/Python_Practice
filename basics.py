#!/usr/bin/env python

def get_sentence():
    sentences = []
    sentence = ""
    while sentence != "stop.":
        sentence = input("Type a sentence or question: ")
        if sentence == "stop":
            break

        question_words = ("who", "what", "where", "when", "why", "how")
        if sentence.lower().startswith(question_words):
            sentence += "?"
        else:
            sentence += "."

        sentences.append(sentence.capitalize())

    for s in sentences:
        print(f"{s} ", end="")


get_sentence()
