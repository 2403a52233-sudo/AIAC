import re
import unicodedata

def slugify(text: str) -> str:
   
    text = unicodedata.normalize('NFKD', text)
    
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    text = text.lower()
    
    text = text.replace('_', '-')
   
    text = re.sub(r'[^a-z0-9\s-]', '', text)
   
    text = re.sub(r'[\s-]+', '-', text)

    text = text.strip('-')
    return text

# Sample input
sample_input = ['Hello World!', 'AI & You', 'Set1-C2']

# Generate slugified output
sample_output = [slugify(item) for item in sample_input]

print(sample_output)
