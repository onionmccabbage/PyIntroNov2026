# We may need to format printed strings
data = {
'guesses': 0,
'target' : 94,
'player' : 'Oenid',
'temperature' : 12.97545682
}
# To retrieve members from a dict we use [] notation
# use f'' to inject any Python statement into a string
print (f'''Ready player {data['player']} 
you have made {data['guesses']} attempts. 
The target is {data['target']}
Temperature is {data['temperature']:0.2f}''')  # :0.2f means 2 decimal places for a floating point value

# we may occasionaly meet these kinds of string
# r'' treats it as a 'raw' string (exactly as we write it)
f = r'this is a raw string \n which includes escape characters'
# b'' will make a string of characters into a byte string
g = b'this is a byte string'

