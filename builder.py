text = "welcome"
parts = ['<p>', text, '</p>']
print(''.join(parts))

# Now I want an HTML list with 2 words in it .

words =['hello','world']
parts = ['<ul>']
for w in words:
    parts.append(f' <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))