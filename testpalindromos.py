from palindromos import is_palindrome
import unittest


class TestPalindrome(unittest.TestCase):

    def test_a(self):
        resultado = is_palindrome("a")
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome ("aa")
        self.assertEqual(resultado,(True))
  
    def test_as(self):
        resultado = is_palindrome ("as")
        self.assertEqual(resultado, False)

    def test_aca(self):
        resultado = is_palindrome("ana")
        self.assertEqual(resultado, True)

    def test_apta(self):
        resultado = is_palindrome("apta")
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_neu_quen(self):
        resultado = is_palindrome("neu quen")
        self.assertEqual(resultado, True)

    def test_quequen(self):
        resultado = is_palindrome("quequen")
        self.assertEqual(resultado, False)

    def test_yo_soy(self):
        resultado = is_palindrome("yo soy")
        self.assertEqual(resultado, True)

    def test_son_robos_o_sobornos(self):
        resultado = is_palindrome("son robos o sobornos")
        self.assertEqual(resultado, True)

    def test_son_robos_o_son_sobornos(self):
        resultado = is_palindrome("son robos o son sobornos")
        self.assertEqual(resultado, False)
    


unittest.main()