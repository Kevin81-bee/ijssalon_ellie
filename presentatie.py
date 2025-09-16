def presenteer(dictionary, totaal):
    for key in dictionary:
        print(f"{key} : {dictionary[key]} euro")
    print("=" * 30)
    print(f"Totaal : {totaal} euro")
