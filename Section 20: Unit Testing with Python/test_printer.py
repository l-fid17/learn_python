from unittest import TestCase
from printer import Printer

class TestPrinter(TestCase):
    def setUp(self): # this one will run before each test runs (so the printer object is a new object for every test function)
        self.printer = Printer(pages_per_s=2.0, capacity=300)
    """"""""""""""""""
    # if we instead want to run it once and preserve it throughout the execution of all tests (sharing the same object between all test cases) we could do
    @classmethod
    def setUpClass(cls) -> None:
        cls.printer = Printer(pages_per_s=2.0, capacity=300)
    """"""""""""""""""
    def test_print_with_capacity(self):
        # printer = Printer(pages_per_s=2.0, capacity=300) # because this is repeated for each test case we could extract it to a spearate method

        # message = printer.print(25) # and printer.print() becomes
        message = self.printer.print(25)
        self.assertEqual(f"Printed 25 pages in 12.50 seconds.", message)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 10
        expected = "Printed 10 pages in 5.00 seconds."

        result = self.printer.print(pages)
        self.assertEqual(result, expected)

    def test_speed_always_two_decimals(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected = "Printed 11 pages in 3.67 seconds."

        result = fast_printer.print(pages)
        self.assertEqual(result, expected)

    def test_multiple_print_runs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

    def test_multiple_print_runs_error(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

        with self.assertRaises(PrinterError):
            self.printer.print(1)