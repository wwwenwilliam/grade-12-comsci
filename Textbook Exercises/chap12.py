#Chapter 12-dictonaries
# Exercise # 1
def findAllChars(string):
    string = string.upper()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letterdict = {}
    
    for char in string:
        if char in letters:
            if char in letterdict:
                letterdict[char] += 1
            else:
                letterdict[char] = 1
    return letterdict

# Exercise # 2
def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity

    return inventory

# Exercise # 5
def createPirateDict():
    piratedict = {}
    piratedict['sir'] = 'matey'
    piratedict['hotel'] = 'fleabag inn'
    piratedict['student'] = 'swabbie'
    piratedict['boy'] = 'matey'
    piratedict['restaurant'] = 'galley'
    piratedict['hello'] = 'avast'
    piratedict['students'] = 'swabbies'
    piratedict['are'] = 'be'
    piratedict['lawyer'] = 'foul blaggart'
    piratedict['the'] = "th'"
    piratedict['restroom'] = 'head'
    piratedict['my'] = 'me'
    piratedict['hello'] = 'avast'
    piratedict['is'] = 'be'
    piratedict['man'] = 'matey'
    return piratedict
    
def translator(worddict, sentence):
    words = sentence.split(" ")
    for i in range(len(words)):
        if words[i] in worddict:
            words[i] = worddict[words[i]]
            
    newsentence = ""
    for word in words:
        newsentence += word + " "
        
    return newsentence
    

#test code --------------------------------------

# Exercise # 1 Call code
# letterdict = findAllChars("hello")
# keys = sorted(letterdict.keys())
# for char in keys:
#     print(char, letterdict[char])
    
# Exercise # 2 Call code
# # make these tests work...
# new_inventory = {}
# add_fruit(new_inventory, 'strawberries', 10)
# #  test that 'strawberries' in new_inventory
# print('strawberries' in new_inventory)
# #  test that new_inventory['strawberries'] is 10
# print(new_inventory['strawberries'])
# add_fruit(new_inventory, 'strawberries', 25)
# #  test that new_inventory['strawberries'] is now 35)
# print(new_inventory['strawberries'])

# Exercise # 5 Call code
# piratedict = createPirateDict()
# sentence = "hello there students"
# print(translator(piratedict, sentence))
