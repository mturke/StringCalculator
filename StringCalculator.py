class StringCalculator:

    def add(self, str):
        count = 0
        if len(str) == 0:
            return 0

        
        result = str.split(",")
        
        for x in result:
            if int(x) < 0:
                raise ValueError("Negatives not allowed!")

            if int(x) < 1000:
                count += int(x)
        return count

        
        

