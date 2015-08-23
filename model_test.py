from model import *
import json

def run_test():
	new_issue('boyilun','i never use boyilun.',0,0,True)
	print json.dumps(list(get_issue(16)),sort_keys=True,indent=2)



if __name__ == '__main__':
	run_test()
