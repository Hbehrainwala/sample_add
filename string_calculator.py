import re

class StringCalculator:

    def add(self, numbers):
        if not numbers:
            return 0
        
        delimiter_pattern = "|".join(map(re.escape, [",", "\n"]))
        
        num_list = re.split(delimiter_pattern, numbers)
        
        return sum([ int(val) if isinstance(val, str) else val for val in num_list])