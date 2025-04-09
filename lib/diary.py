# building a personal diary system

def make_snippet(string):
    words = string.split()
    if len(words) <= 5:
        return ' '.join(words)
    else:
        return (' '.join(words[:5])) + '...'
    
def count_words(string):
    words = string.split()
    return len(words)

