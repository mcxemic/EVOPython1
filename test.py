import unittest

from optimize import optimize_data


class TestOptimize(unittest.TestCase):
    def test(self):
        template = 'Python version: {languages[python][latest_version]}'

        data = {
            'languages': {
                'python': {
                    'latest_version': '3.6',
                    'site': 'http://python.org',
                },
                'rust': {
                    'latest_version': '1.17',
                    'site': 'https://rust-lang.org',
                },
            },
        }
        self.assertEqual(optimize_data(template, data), {'Python version: 3.6'})


if __name__ == '__main__':
    unittest.main()
