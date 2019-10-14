import unittest
import affinityJenkins.compute_highest_affinity as compute_highest_affinity

class ControlledTests(unittest.TestCase):
    def test1(self):
        site_list = ["a.com", "b.com", "a.com", "b.com", "a.com", "c.com"]

        user_list = ["andy", "andy", "bob", "bob", "charlie", "charlie"]
        time_list = [1238972321, 1238972456, 1238972618, 1238972899, 1248472489, 1258861829]
        computed_result = compute_highest_affinity.highest_affinity(site_list, user_list, time_list)
        expected_result = ("a.com", "b.com")
        self.assertEqual(computed_result, expected_result)

    def test4(self):
        a = "a"
        b = "b"
        c = "c"
        d = "d"
        e = "e"
        f = "f"
        g = "g"
        h = "h"

        A = "A"
        B = "B"
        C = "C"
        D = "D"
        E = "E"
        F = "F"
        G = "G"
        H = "H"
        site_list = [a, a, a, a, b, b, b, b, c, c, c, d, d, d, d, d]
        user_list = [B, D, E, F, A, B, C, F, B, D, E, A, B, C, D, F]
        time_list = range(0, 16)

        computed_result = compute_highest_affinity.highest_affinity(
            site_list, user_list, time_list)
        expected_result = (b, d)
        self.assertEqual(computed_result, expected_result)