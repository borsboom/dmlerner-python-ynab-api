"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.sub_transaction import SubTransaction
from openapi_client.model.transaction_detail_all_of import TransactionDetailAllOf
from openapi_client.model.transaction_summary import TransactionSummary
globals()['SubTransaction'] = SubTransaction
globals()['TransactionDetailAllOf'] = TransactionDetailAllOf
globals()['TransactionSummary'] = TransactionSummary
from openapi_client.model.transaction_detail import TransactionDetail


class TestTransactionDetail(unittest.TestCase):
    """TransactionDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionDetail(self):
        """Test TransactionDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()