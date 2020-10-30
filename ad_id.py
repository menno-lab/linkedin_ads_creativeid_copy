import re, pyperclip

# Regex for ad id

creativeRegex = re.compile(r'''
(
\d\d\d\d\d\d\d\d # first 8 digits
)
''', re.VERBOSE)

# Gets the text off the clipboard

text = pyperclip.paste()

# Extracts the ad id from the text

extracted_creativeid = creativeRegex.findall(text)

addCreativeIDs = []
for creativeID in extracted_creativeid:
    addCreativeIDs.append(creativeID)

# Removes duplicates

newAdCreatives = set(addCreativeIDs)

# Copies the extracted ids to the clipboard

length = str(len(newAdCreatives))
results = str('\n'.join(newAdCreatives))

output = length + ' ads:' + '\n' + results

#print(output)

pyperclip.copy(output)
