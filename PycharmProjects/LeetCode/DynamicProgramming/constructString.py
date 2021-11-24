
def constr(targetString, wordBank):

    if targetString == '': return True
    for word in wordBank:
        #Do not remove characters from the middle of the string
        #If the word in array is a prefix of our targetstring then index will be 0
        if targetString.find(word)==0:
            suffix = targetString.replace(word,'')
            result = constr(suffix, wordBank)
            if result:
                return True
    return False

def constrDP(targetString, wordBank, memo={}):
    if targetString in memo: return memo[targetString]
    if targetString == '': return True
    for word in wordBank:
        #Do not remove characters from the middle of the string
        #If the word in array is a prefix of our targetstring then index will be 0
        if targetString.find(word)==0:
            suffix = targetString.replace(word,'')
            result = constrDP(suffix, wordBank, memo)
            if result:
                memo[targetString] = True
                return True
    memo[targetString] = False
    return False

print('Recursive result= ',constr('abcdef',[ 'ab','abc','cd','def','abcd']))
print('Recursive result= ',constrDP('abcdef',[ 'ab','abc','cd','def','abcd']))

print('Recursive result= ',constr('skateboard',[ 'bo','rd','ate','t','ska','sk','boar']))
print('Recursive result= ',constrDP('skateboard',[ 'bo','rd','ate','t','ska','sk','boar']))
