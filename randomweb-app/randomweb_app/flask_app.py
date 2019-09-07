import os
from .create_app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    testmodules = [
        'bettermathlib_tests',
        'randomwebapp_tests',
    ]
    suite = unittest.TestSuite()
    for t in testmodules:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
    unittest.TextTestRunner(verbosity=2).run(suite)
