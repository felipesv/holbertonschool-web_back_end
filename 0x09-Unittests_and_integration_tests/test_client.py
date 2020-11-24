#!/usr/bin/env python3
"""
Unittest client.py
Run: python3 -m unittest test_client | tail -1
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test Cases
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_class):
        """
        test the org function
        """
        client = GithubOrgClient(org_name)
        _return = client.org
        self.assertEqual(_return, mock_class.return_value)
        mock_class.assert_called_once()
