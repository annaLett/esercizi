input_venv : str = ""

while True:
    input_venv = input("(venv) $")
    if input_venv == "deactivate":
        break
    print("Ancora in esecuzione")

print("uscito dal venv")