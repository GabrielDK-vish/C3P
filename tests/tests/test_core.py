import unittest
import pandas as pd
from c3p import SmartAnalytic

class TestSmartAnalytic(unittest.TestCase):
    def setUp(self):
        self.analyzer = SmartAnalytic()
        self.test_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    def test_load_dataframes(self):
        self.analyzer.load_dataframes(self.test_df)
        self.assertEqual(len(self.analyzer.dataframes), 1)
        
    def test_analyze(self):
        self.analyzer.load_dataframes(self.test_df)
        insights = self.analyzer.analyze()
        self.assertIsInstance(insights, list)

if __name__ == '__main__':
    unittest.main()