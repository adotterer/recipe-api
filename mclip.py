#! python3
# mclip.py - A multi-clipboard program.

import sys
import pyperclip

TEXT = {'agree': """Yes, I am available to play. Thank you for contacting me!""",
        'busy': """I'm sorry, I already have another commitment at that time.""",
        'beggar': """Assuming this is a paid opporunity-- what is your rate?""",
        'upsell': """Would you consider """}


if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]       # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
