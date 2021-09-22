#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	if len(string) % 2 == 0:
		return True


def get_num_char(string, char):
	compteur = 0
	for c in string:
		if c == char:
			compteur += 1
	return compteur


def get_first_part_of_name(name):
	premier_prénom = ""
	for c in range(len(name)):
		if name[c] == "-":
			break
		premier_prénom += name[c]
	return premier_prénom


def get_random_sentence(animals, adjectives, fruits):
	nb1 = random.randint(0, len(animals)-1)
	nb2 = random.randint(0, len(adjectives)-1)
	nb3 = random.randint(0, len(fruits)-1)
	animal = animals[nb1]
	adjectif = adjectives[nb2]
	fruit = fruits[nb3]
	return "Aujourd'hui j'ai vu un "+animal+" s'emparer d'un panier "+adjectif+" plein de "+fruit


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
