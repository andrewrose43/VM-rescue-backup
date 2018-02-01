import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args() #this is when the arguments become PARSED and therefore usable! only after here can you do stuff using the arguments. Note that this function will not run if you don't give it that echo argument at runtime.
print(args.echo)
