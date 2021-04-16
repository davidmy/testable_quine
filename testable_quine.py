import os, sys

body = "\nif sys.argv[1:] == ['--test']:\n    print(test.format(repr(os.path.split(__file__)[-1])))\nelse:\n    print('import os, sys\\n')\n    print('body = '+repr(body))\n    print('test = '+repr(test))\n    print(body)\n\n# Usage:\n#   $ python testable_quine.py\n#   $ python testable_quine.py --test\n"
test = "import sys, subprocess, unittest\n\nquine_fn = {}\n\nclass TestableQuineTest(unittest.TestCase):\n    def test_quine(self):\n        with open(quine_fn, 'rb') as f:\n            expected = f.read()\n        p = subprocess.Popen([sys.executable, quine_fn], stdout=subprocess.PIPE)\n        result,_ = p.communicate()\n        self.assertEqual(result, expected)\n\nif __name__ == '__main__':\n    unittest.main()\n"

if sys.argv[1:] == ['--test']:
    print(test.format(repr(os.path.split(__file__)[-1])))
else:
    print('import os, sys\n')
    print('body = '+repr(body))
    print('test = '+repr(test))
    print(body)

# Usage:
#   $ python testable_quine.py
#   $ python testable_quine.py --test

