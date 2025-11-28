input_vev : str = ""
while True :
	input_venv = input("(venv) $")
	if input_venv == "deactivate":
		break
	print("Ancora in esecuzione")
print("Uscito dal venv")
