# import sys

# the_file = sys.argv
# corpus = the_file.read().split("")


# all_text = the_file.read()
# corpus = all_text.split(" ") 

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    file_object = open(corpus)
    all_text = file_object.read()
    corpus_text = all_text.replace("\n", " ").split(" ")
    
    chain_dict = {}
    i = 0
    for i in range(len(corpus_text)-1):
        key = tuple([corpus_text[i], corpus_text[i +1]])
        value = []
        chain_dict[key] = value
        value.append(corpus_text[i + 2])
        chain_dict[key] = value
        i += 1

        
    return chain_dict 




make_chains("green-eggs.txt")





        
        # if key in chains: 
        #     value = word[i+2]
        # else: 
        #     key = value.append(word[i+2])
            

        # for blank in blank: 
        #     if key[0][1] == word:



        #     chains[key[x][y]] = value 





    #         words_after = {}
    #         x = 0

    # for word[x] in corpus:
    #     value.append(word[x+1])
    # x += 1
    # return value




        


    # return chains


# def make_text(chains):
    # """Takes dictionary of markov chains; returns random text."""

    # return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "Some text"

# Get a Markov chain
# chain_dict = make_chains(input_text)

# Produce random text
# random_text = make_text(chain_dict)

# print random_text
