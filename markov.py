import sys
import random


def make_chains(the_file):
    """Takes input text as string; returns dictionary of markov chains."""
    file_object = open(the_file)
    all_text = file_object.read()
    corpus_text = all_text.replace("\n", " ").split(" ")
    
    chain_dict = {}
    i = 0
    for i in range(len(corpus_text)-2):
        key = tuple([corpus_text[i], corpus_text[i +1]])
        value = corpus_text[i + 2]
       
        chain_dict.setdefault(key, []).append(value)
        i += 1

    return chain_dict 

# make_chains(sys.argv[1])


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # random_key = random.choice(chains.keys())
    # print random_key
    # random_words = []

    # for word in random_key:
    #     random_words.append(word) 
    
    # print random_words

    random_key = random.choice(chains.keys())
    random_val = random.choice(chains[random_key])
    print random_key[0] + " " + random_key[1] + " " + random_val



     # # for word in chains[random_key]:

    #     random_value = random.choice(chains[random_key][word])
    #     random_words.append(random_value)
    # print random_words

        # for item in list_item
        #     choose a random value
        #     random_value = the random value chosen

    # random_value = random.choice(chains[.value())
    # random_key + " " + random_value


    # return "Here's some random text."


make_text(make_chains(sys.argv[1]))
make_text(make_chains(sys.argv[1]))
make_text(make_chains(sys.argv[1]))
make_text(make_chains(sys.argv[1]))


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "sys.argv"

# Get a Markov chain
# chain_dict = make_chains(input_text)

# Produce random text
# random_text = make_text(chain_dict)

# print random_text
