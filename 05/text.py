text = "cião"

print(text)
text_bytes = text.encode('utf-8')
print(text_bytes)

# new_text = text_bytes.decode('utf-16')
new_text = text_bytes.decode('utf-8')
print(new_text)
