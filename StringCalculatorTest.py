##### Test
import unittest

from StringCalculator import StringCalculator

class Test_StringCalculator(unittest.TestCase):
    
    def testAdd_EmptyString_Returns0(self):
        
        calc = StringCalculator()

        result = calc.add("")
        
        self.assertEqual(0, result)
        

    def testAdd_Zero(self):
        
        calc = StringCalculator()

        result = calc.add("0")

        self.assertEqual(0, result)

    def testAdd_One(self):
        
        calc = StringCalculator()

        result = calc.add("1")

        self.assertEqual(1, result)
        
    def testAdd_Numbers(self):
        
        calc = StringCalculator()

        result = calc.add("1,2")
                
        self.assertEqual(result, 3)
    

    def testAllow_UnknownAmountOfNumbers(self):
        
        calc = StringCalculator()

        result = calc.add("1,2,3,4,5,6")

        self.assertEqual(result, 21)

    def testNegative_NotAllowed(self):
        
        calc = StringCalculator()

        with self.assertRaises(ValueError):
            result = calc.add("-1")

    def testNegativeInputs_NotAllowed(self):

        calc = StringCalculator()

        with self.assertRaises(ValueError):
            result = calc.add("1000, -1")    

    def testIgnore_NumsGreaterThan1000(self):
        calc = StringCalculator()

        result = calc.add("1001, 2")

        self.assertEqual(result, 2)
      
    

if __name__ == "__main__":
    unittest.main()
