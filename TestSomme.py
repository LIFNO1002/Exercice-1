#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import CorrSomme as correct
import sommetest as student


class TestSomme(unittest.TestCase):

    def test1_sommetest(self):
        args = [2, 5, 20, 100]
        rep = _(
            "Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la reponse attendue est {}")
        for n in args:
            try:
                student_ans = student.somme_n_premiers_nbrs(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'erreur {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.somme_n_premiers_nbrs(n)
            self.assertEqual(student_ans, correct_ans, rep.format(student_ans, n, correct_ans))


if __name__ == '__main__':
    unittest.main()
