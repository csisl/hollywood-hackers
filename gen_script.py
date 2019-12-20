#!/usr/bin/env python

# a script to throw some verbs and programming terms together
# for that perfect hollywood movie 

from random import randint, choice

def get_prog_noun():

	prog_nouns = [ "IP", "firewall", "blockchain",
			       "encryption", "decryption", "GUI",
				   "interface", "root", "database",
				   "SQL", "Java", "Python", "script",
				   "admin", "RAM", "mainframe",
				   "terminal", "hard drive", "SSL",
				   "port", "URL", "router" ]

	return prog_nouns[randint(0, len(prog_nouns)-1)]


def get_prog_verb():

	prog_verbs = [ "hack", "brute force", "scan",
			       "decrypt", "encrypt", "load",
				   "test", "decompile", "compile",
				   "tunnel", "VPN", "execute",
				   "sudo", "link", "download",
				   "upload", "inject" ]

	return prog_verbs[randint(0, len(prog_verbs)-1)]


def get_garbage_sentence():

	# v = verb, n = noun when naming the lists

	vnn = [ "I need to %s into %s with the %s",
			"CRAP! We're screwed. They did a %s on our %s with a %s", 
			"Can't you just %s into their %s with %s?!",
			"This is insane. I've never seen someone %s with %s and no %s",
			"I don't know how to %s a %s like this. They must be using %s" ]

	nnvn = [ "Give me a sec! The have %s in their %s. This will be tricky, " \
			    "but if I can just %s in their %s we'll be golden!",
			"I don't have a %s or %s but if I can just %s then I will have " \
			    "access to their %s",
			"Wow. I've never seen a %s like this. They even used a %s to %s into the %s",
			"Sure I can get access to their %s. I just need a %s to %s and I'm golden." \
				"Go get me %s",
			"I need more time to get access to their %s. They have a %s setup that is " \
				"making me need to %s to see their %s" ]


	mapping = { vnn[randint(0, len(vnn)-1)] : "vnn",
			    nnvn[randint(0, len(nnvn)-1)] : "nnvn" }

	return choice(list(mapping.items()))


def main():

	sentence, sen_type = get_garbage_sentence()

	while True:
		if sen_type == "vnn":
			print(sentence % (get_prog_verb(), get_prog_noun(), get_prog_noun()))
		elif sen_type == "nnvn":
			print(sentence % (get_prog_noun(), get_prog_noun(),
		              		  get_prog_verb(), get_prog_noun()))
		input("Press Enter to continue or ctrl-c to stop")
		sentence, sen_type = get_garbage_sentence()
	

if __name__ == "__main__":
	main()

