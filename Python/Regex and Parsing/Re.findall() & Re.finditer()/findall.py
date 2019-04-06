import re

VOWELS = '[aeiou]'
CONSONANTS = '[QWRTYPSDFGHJKLZXCVBNM]'
REGEX = '(?<=' + CONSONANTS + ')(' + VOWELS + '{2,})' + CONSONANTS

match = re.findall(REGEX, input(), re.I)
print('\n'.join(match or ['-1']))