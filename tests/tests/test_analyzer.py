import unittest
import pandas as pd
from c3p.analyzer import analyze_data

class TestAnalyzer(unittest.TestCase):
    def test_analyze_data(self):
        # Criar um DataFrame de teste
        test_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        
        # Testar a função de análise
        insights = analyze_data([test_df], "Regras de teste")
        
        # Verificar se retorna uma lista
        self.assertIsInstance(insights, list)
        
        # Verificar se a lista não está vazia
        self.assertTrue(len(insights) > 0)

if __name__ == '__main__':
    unittest.main()