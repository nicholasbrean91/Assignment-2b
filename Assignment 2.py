# Created by: Nicholas Brean
# Created on: September 2017
# Created for: ICS3UR-1
# This program Calculates the height after an amount of seconds

import ui

def Calculation(sender):
	#input
	seconds = float(view['Seconds_TextField'].text)
	
	#constants
	g = 9.81
	
	#process 
	Height = 100 - 0.5*g*seconds**2
	
	#output
	view['answer_label'].text = 'The Area of the circle is: ' + str(Height) + ' cm'
	

view = ui.load_view()
view.present('sheet')
