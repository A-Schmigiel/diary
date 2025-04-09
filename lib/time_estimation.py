import math

def time_estimation(text_to_read):
    if type(text_to_read) is not str:
        raise Exception("I can only check strings, sorry!")
    words = text_to_read.split()
    minutes = int(round((len(words)/200), 0))
    if minutes < 60:  # formatting for when there is less than one hour's worth of reading
        if minutes < 1:
            return 'This text will take you less than 1 minute to read.'
        elif minutes == 1:
            return 'This text will take you approximately 1 minute to read.'
        elif minutes < 55:
            return f"This text will take you approximately {minutes} minutes to read."
        else: # rounding up to 1 hour and formatting grammar.
            return "This text will take you approximately 1 hour to read."
    else: # formatting for when there is one hour or more of reading
        hours = int(math.floor((minutes/60)))
        minutes = int(minutes % 60)
        if hours == 1:  
            if minutes < 5:
                return f"This text will take you approximately 1 hour to read."
            elif minutes < 55:
                return f"This text will take you approximately 1 hour and {minutes} minutes to read."
            else: # to round up if over 55 minutes
                return f"This text will take you approximately 2 hours to read."
        else:
            if minutes < 5:
                return f"This text will take you approximately {hours} hours to read."
            elif minutes < 55:
                return f"This text will take you approximately {hours} hours and {minutes} minutes to read."
            else:
                hours = hours + 1
                return f"This text will take you approximately {hours} hours to read."

# I feel like the formatting could be better handled with functions for minutes and hours, but I know I'm getting derailed with nitpicking the grammar here, as that isn't the point of the exercise.