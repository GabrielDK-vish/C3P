import unittest
from c3p.pdf_parser import extract_text_from_pdf

class TestPDFParser(unittest.TestCase):
    def test_extract_text_from_pdf(self):
        # Teste simples para verificar se a função retorna uma string
        result = extract_text_from_pdf("dummy_path.pdf")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()