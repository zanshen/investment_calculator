"""
program: investmentgui.py
"""

from breezypythongui import EasyFrame

class TextAreaDemo(EasyFrame):
	"""An investment calculator that demonstrates the use of multi-line text area."""

	def __init__(self):
		"""Sets up the window and widgets."""
		EasyFrame.__init__(self, "Investment Calculator")
		self.addLabel(text = "Initial Amount", row = 0, column = 0)
		self.addLabel(text = "Number of Years", row = 1, column = 0)
		self.addLabel(text = "Interest Rate in %", row = 2, column = 0)
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addIntegerField(value = 0, row = 2, column = 1)

		self.outputArea = self.addTextArea("", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)

	# Event handling method
	def compute(self):
		"""Computes the investment schedule based on the inputs and outputs the schedule."""
		# Obtain and validate the inputs
		startBalance = self.amount.getNumber()
		rate = self.rate.getNumber() / 100
		years = self.period.getNumber()
		if startBalance == 0 or rate == 0 or years == 0:
			return

		# Set the header for the table
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")

		# Compute and append the results for each year
		totalInterest = 0.0
		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest

		# Append the totals for the period
		result += "Ending balance: $%0.2\n" % endBalance
		result += "Total interest earned: $%0.2f\n" %  totalInterest

		# Output the result while preserving read-only status    *important for test*
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"

def main():
	TextAreaDemo().mainloop()
	
main()
