# First install pyjokes if not already installed
# pip install pyjokes

import pyjokes

# Get a random joke
joke = pyjokes.get_joke()

print("Here’s a joke for you:")
print(joke)

