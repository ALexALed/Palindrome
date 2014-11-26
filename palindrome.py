#encoding: utf-8
__author__ = 'alex'


def is_palindrome(word):
    """
    Функция получает строку и определяет является ли строка палиндромом
    """
    if (not word or len(word)==1):
        return False

    wrong_symbols = (',', '.', ' ', '?', '!', u'ь')
    symbols = [symb.lower() for symb in word if symb not in wrong_symbols]
    comparison_nums = len(symbols) // 2
    word_is_palindrome = True
    for i in xrange(0, comparison_nums):
        if symbols[i] != symbols[-(i+1)]:
            word_is_palindrome = False
    return word_is_palindrome

if __name__ == '__main__':
    print(is_palindrome('E'))
    print(is_palindrome('Ee'))
    print(is_palindrome('Ec'))
    print(is_palindrome('Eve'))
    print(is_palindrome(u'Кукси, кум, мук и скук'))
    print(is_palindrome(u'Чин зван мечем навзничь.'))
    print(is_palindrome('Sum summus mus'))
    print(is_palindrome(u'а это не палиндром'))
    print(is_palindrome(u'и это не он'))

