# inkshell

import readline
import rlcompleter
import atexit
import os
import sys
from colorama import Fore
from colorama import Style


class INKSH:
	def __init__(self):
		self.cmd_line()

	def help_list(self):
		print('\nHelp list')

	def cmd_list(self, cmd):
		print(cmd)

	def cmd_line(self):
		try:
			while True:
				print(f'colored {Fore.GREEN} asdf {Syle.RESET_ALL adsf'})
				current_path = os.system('pwd')
				cmd = str(input(f"[{os.getcwd()}]"))
				self.cmd_execution(cmd)
				self.where_am_i()
		except KeyboardInterrupt:
			print("\nER:")


	def cmd_execution(self, cmd):
		print(os.system(f'{cmd}'))

	def where_am_i(self):
		print("Current Script Path" + os.path.realpath(__file__))



if __name__ == "__main__":
	INKSH()
	# tab complete
	readline.parse_and_bind('tab: complete')

	# history file
	histfile = os.path.join(os.environ['HOME'], '.pythonhistory')

	try:
		readline.read_history_file(histfile)
	except IOError:
		pass

	atexit.register(readline.write_history_file, histfile)
	del os, histfile, readline, rlcompleter
