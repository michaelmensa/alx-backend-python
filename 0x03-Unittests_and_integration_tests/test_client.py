#!/usr/bin/env python3
'''
Module test_client: test module for client.py
'''
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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


if __name__ == '__main__':
    unittest.main()
