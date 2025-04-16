import math
# building a personal diary system

class Diary_Entry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.still_to_read = contents.split()
 
    def format(self):
        return f"{self.title.title()}:  {self.contents}"    
        
    def count_words(self, wpm):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return int(round((self.count_words(wpm)/wpm), 0))
    
    def reading_chunk(self, wpm, minutes):
        enough_time_for = wpm * minutes
        if len(self.still_to_read) <= enough_time_for:
            result = ' '.join(self.still_to_read)
            self.still_to_read = []
        else:
            result = (' '.join(self.still_to_read[:enough_time_for])) + '...'
            self.still_to_read = self.still_to_read[enough_time_for:]
        return result

