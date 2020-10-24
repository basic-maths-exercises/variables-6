import unittest
import main

class UnitTests(unittest.TestCase) :
    def test_code_runs(self) :
       self.assertTrue( a1==( c3 + e5 ) / ( f6 + d4 ), "The code does not work correctly" )
       self.assertTrue( b2==e5*c3, , "The code does not work correctly" )
       self.assertTrue( c3==4, "The code does not work correctly" )
       self.assertTrue( d4==c3/f6, "The code does not work correctly" )
       self.assertTrue( e5==c3+5, "The code does not work correctly" )
       self.assertTrue( f6==(b2 + e5), "The code does not work correctly" )
