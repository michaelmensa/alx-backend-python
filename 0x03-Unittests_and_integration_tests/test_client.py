#!/usr/bin/env python3
'''
Module test_client: test module for client.py
'''
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    ''' class to test client.GithubOrgClient
    '''

    @parameterized.expand([
        ('google',),
        ('abc',)
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        ''' method to test client.org and returns the correct
        value
        '''
        github_client = GithubOrgClient(org_name)
        result = github_client.org
        expected_url = GithubOrgClient.ORG_URL.format(org=org_name)
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, mock_get_json.return_value)

    @parameterized.expand([
        ('url_one', {'repos_url': 'http://url_one.com'}),
        ('url_two', {'repos_url': 'http://url_two.com'})
        ])
    def test_public_repos_url(self, url_name, url):
        ''' test method fo GitHubOrgClient._public_repos_url '''
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=url)):
            result = GithubOrgClient(url_name)._public_repos_url

            self.assertEqual(result, url.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        ''' test method for client.GithubOrgClient.public_repos '''
        mock_payload = {
                'repos_url': 'https://api.github.com/orgs/testorg/repos',
                'repos': [
                    {'id': 23, 'name': 'repo1', 'license': {'key': 'MIT'}},
                    {'id': 12, 'name': 'repo2', 'license': {'key': 'Apache'}},
                    {'id': 45, 'name': 'repo3', 'license': {'key': 'Nginx'}}
                    ]
                }
        mock_get_json.return_value = mock_payload['repos']

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = mock_payload['repos_url']
            client = GithubOrgClient('testorg')
            repos = client.public_repos()

            self.assertEqual(repos, ['repo1', 'repo2', 'repo3'])
            mock_get_json.assert_called_once()
            mock_property.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
        ])
    def test_has_license(self, repo, license, expected_result):
        ''' test method for GithubOrgClient.has_license '''
        client = GithubOrgClient('testorg')

        result = client.has_license(repo, license)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
        },
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    ''' integration test class for GithubOrgClient '''

    @classmethod
    def setUpClass(cls):
        ''' sets up the test requirements '''
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
                MockResponse(cls.org_payload),
                MockResponse(cls.repos_payload),
                MockResponse(cls.apache2_repos)
                ]

    @classmethod
    def tearDownClass(cls):
        ''' tears down the integration test requirements '''
        cls.get_patcher.stop()


class MockResponse():
    ''' class for MockResponse '''
    def __init__(self, json_data):
        ''' constructor '''
        self.json_data = json_data

    def json(self):
        ''' return json_data '''
        return self.json_data


if __name__ == '__main__':
    unittest.main()
