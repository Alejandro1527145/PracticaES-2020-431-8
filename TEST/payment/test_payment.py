import os
import sys
import tempfile
import unittest

# TO BE ABLE TO DEBUG THE TEST 2 WAYS:
# 1: Configure PYTHONPATH
# 2: Add path to src folder manually (copy at the header of each test)
    # TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    # PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR,os.pardir))
    # PROJECT_DIR = os.path.join(PROJECT_DIR, '..','src')
    # if not PROJECT_DIR is sys.path:
    #   sys.path.insert(0, PROJECT_DIR)

from SRC.PaymentData import PaymentData

class TestPayment(unittest.TestCase):

    def test_tipus(self):
        self.Payment = PaymentData()
        assert self.Payment.type == ""
        assert not self.Payment.type == "VISA"
        self.Payment.type = "VISA"
        assert self.Payment.type == "VISA"
        self.Payment.setType("MASTERCARD")
        assert not self.Payment.type == "MASTERCARD"
        self.Payment.setType("MasterCard")
        assert self.Payment.type == "MasterCard"
        self.Payment.setType(123)
        assert not self.Payment.type == 123



