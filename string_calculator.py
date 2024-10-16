import re

class StringCalculator:

    def add(self, numbers):
        if not numbers:
            return 0
        
        delimiters = [",", "\n"]
        if numbers.startswith("//"):
            numbers = self._extract_custom_delimiters(numbers, delimiters)
        
        delimiter_pattern = "|".join(map(re.escape, delimiters))
        
        num_list = re.split(delimiter_pattern, numbers)
        
        return self._calculate_sum(num_list)
    
    def _extract_custom_delimiters(self, numbers: str, delimiters: list) -> str:
        """Extract custom delimiters and modify the input string."""
        match = re.match(r"//(.+)\n(.*)", numbers)
        if match:
            delimiter_part = match.group(1)
            numbers = match.group(2)
            delimiters.extend(re.findall(r"\[(.*?)\]", delimiter_part) or [re.escape(delimiter_part)])
        return numbers
    
    def _calculate_sum(self, num_list: list) -> int:
        result = 0
        
        for num in num_list:
            if num.strip():
                value = int(num)
                if value <= 1000:
                    result += value
        return result