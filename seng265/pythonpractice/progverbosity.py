import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help = "increase output velocity", action = "store_true")
args = parser.parse_args()
if args.verbose:
	print("verbosity turned on")

