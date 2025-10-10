# given a string, replace every letter with its position in the alphabet.


def alphabet_position(text):
    return " ".join(str(ord(c.lower()) - 96) for c in text if c.isalpha())


print(alphabet_position("Jamisha Bade H"))

"""
.join()- joins the number with spaces
ord()= gives the unicode value for the alphas 

"""
