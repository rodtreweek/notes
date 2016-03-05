#!/usr/bin/python3
'''
The Robots have found an encrypted message. We cannot decrypt it at the moment, but we can take the first steps towards doing so. You have a set of "words", all in lower case, and each word contains symbols in "alphabetical order". (it's not your typical alphabetical order, but a new and different order.) We need to determine the order of the symbols from each "word" and create a single "word" with all of these symbols, placing them in the new alphabetial order. In some cases, if we cannot determine the order for several symbols, you should use the traditional latin alphabetical order. For example: Given words "acb", "bd", "zwa". As we can see "z" and "w" must be before "a" and "d" after "b". So the result is "zwacbd".

Input: Words as a list of strings.

Output: The order as a string.

Example:

    checkio(["acb", "bd", "zwa"]) == "zwacbd"
    checkio(["klm", "kadl", "lsm"]) == "kadlsm"
    checkio(["a", "b", "c"]) == "abc"
    checkio(["aazzss"]) == "azs"
    checkio(["dfg", "frt", "tyg"]) == "dfrtyg"
'''

'''
for c in each ele see if c's position when compared to all characters in ahead
of it lines up with the normal alphabet. If not, move it in front of offending
character and move all other characters down (listy.insert(index, "blah")))
then iterate over new alphabet and print if char is in a joined + uniq'd input
string (eg: "acbbdzwa")
'''

def checkio(crypto):
  alphabet='abcdefghijklmnopqrstuvwxyz'
  allchars = ''.join(crypto)
  # generate an indexed ranking of letters. Spread has to be greater
  # than the longest input list element, ie 100 is good for 100 chars.
  alpharank = {}
  hundreds = 100
  for index, char in enumerate(alphabet):
    alpharank[char] = (index+1) * hundreds

  def setrank():
    for chars in crypto:
      # Mark the first character as our "pivot" comparison. Always compare it
      # against the last character in the string, then recurse again with the
      # formerly last character removed.
      def recurse(rchars, rremaining):
        if alpharank[rchars[0]] > alpharank[rchars[-1]]:
          alpharank[rchars[0]] = alpharank[rchars[-1]] - rremaining
        rremaining -= 1
        if rremaining > 1:
          recurse(rchars[:-1], rremaining)
  
      # Pass the recursion function a slice from current iteration character
      # to end of the string.
      for i, c in enumerate(chars):
        recurse(chars[i:], len(chars[i:]))

  # Rank until no more changes
  # Do the dict.copy() or you'll just end up with a new binding
  # to the exact same object.
  while True:
    oldrank = alpharank.copy()
    setrank()
    if oldrank == alpharank:
      break


  # Since we're determining character rank for multiple elements, it is
  # possible for two characters to end up with the same rank (value),
  # eg ["zwa","xya"] makes z=97,x=97,w=98,y=98
  # Should this happen, we should sort first by value and then by character.
  # sorted() does this tie breaker for us, just pass key a tuple
  sortedchars = [x[0] for x in sorted(alpharank.items(), key=lambda x: (x[1],x[0]))]

  # concatenate input characters, uniq them (order doesn't matter), 
  # then print them in ranked order as mapped in alpharank.

  # set() will uniq the chars, but the result won't be ordered the same as
  # the input. Try OrderedDict if uniq+preserve input order is desired
  allchars = ''.join(set(allchars))
  ret = []
  for a in sortedchars:
    if a in allchars:
      ret.append(a)
  print(''.join(ret))



if __name__ == '__main__':
  checkio(["hfecba","hgedba","hgfdca"])  # "hgfedcba"
  checkio(["dfg", "frt", "tyg"]) # "dfrtyg"
  #checkio(["acb", "bd", "zwa"])
  #checkio(["klm", "kadl", "lsm"])
  #checkio(["a", "b", "c"])
  #checkio(["aazzss"])
