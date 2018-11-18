#https://www.m3tech.blog/entry/python-snippets


def output():
	import sys
	print("HELLO")
	print("ERROR!", file=sys.stderr)

def log():
	import logging
	logging.basicConfig(level=logging.INFO, format="%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s",)
	logger = logging.getLogger(__name__)
	logger.error("ERROR!")

output()
log()
