
import unittest
import sys
import AlgoTests

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTests(loader.loadTestsFromModule(AlgoTests))

if __name__ == '__main__':

    runner = unittest.TextTestRunner(resultclass=unittest.TestResult)
    res = runner.run(suite)

    nr_errors = len(res.errors)
    nr_failures = len(res.failures)

    if nr_errors > 0:
        print("======== Errors ==========")
        for err, msg in res.errors:
            print("In ", err, ":\n\n", msg)
    if nr_failures > 0:
        print("=========== Failures ============== ")
        for err, msg in res.failures:
            print("In ", err, ":\n\n", msg)
    if len(res.skipped) > 0:
        print("=========== Skipped ============== ")
        for err, msg in res.skipped:
            print("In ", err, ":\n\n", msg)

    # Print summary
    if nr_errors > 0:
        print('\n\n')
        print("Errors in:\n\n")
        for err, msg in res.errors:
            print(err, '\n')

    print()
    if nr_failures > 0:
        print('\n\n')
        print("Failures in\n\n")
        for err, msg in res.failures:
            print(err, '\n')
    print()

    sys.exit(nr_errors + nr_failures)
