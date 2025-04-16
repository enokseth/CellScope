def get_french_lai_codes():
    # Codes MCC et MNC pour la France
    mcc = 208
    mncs = [1, 2, 10, 11, 13, 14, 15, 16, 20, 21, 22, 23, 24, 25, 26, 30, 33, 36, 88]
    
    # Exemples de LAC réels pour différentes régions
    lacs = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
        # Ajoutez plus de LAC réels ici
    ]
    
    lai_list = []
    for mnc in mncs:
        for lac in lacs:
            lai = f"LAI = {mcc}-{mnc}-{lac}"
            lai_list.append(lai)
    
    return lai_list

# Example of how to use this function
if __name__ == "__main__":
    lai_list = get_french_lai_codes()
    for lai in lai_list:
        print(lai)
