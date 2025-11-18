#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
    pass

def make_exclamation(sentence_list):
    return[ex + "!" for ex in sentence_list if ex[-1:] != "!"]