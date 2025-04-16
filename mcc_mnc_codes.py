# mcc_mnc_codes.py
def get_mobile_mcc_mnc_codes():
    mobile_data = {
        "MCC": [208]*19,
        "MNC": [1, 2, 10, 11, 13, 14, 15, 16, 20, 21, 22, 23, 24, 25, 26, 30, 33, 36, 88],
        "Operator": [
            "Orange", "Orange", "SFR", "SFR", "SFR", "Free Mobile", "Free Mobile", "Free Mobile",
            "Bouygues Telecom", "Bouygues Telecom", "Bouygues Telecom", "Bouygues Telecom", "Bouygues Telecom",
            "Lycamobile", "NRJ Mobile", "Altitude Télécom", "Omea Telecom", "Free Mobile", "Bouygues Telecom"
        ],
        "Description": [
            "Orange - Principal", "Orange - Réseau alternatif", "SFR - Principal", "SFR - Réseau alternatif", "SFR - Réseau alternatif",
            "Free Mobile - Principal", "Free Mobile - Réseau alternatif", "Free Mobile - Réseau alternatif",
            "Bouygues Telecom - Principal", "Bouygues Telecom - Réseau alternatif", "Bouygues Telecom - Réseau alternatif",
            "Bouygues Telecom - Réseau alternatif", "Bouygues Telecom - Réseau alternatif", "Lycamobile - MVNO",
            "NRJ Mobile - MVNO", "Altitude Télécom - MVNO", "Omea Telecom - MVNO", "Free Mobile - Réseau alternatif",
            "Bouygues Telecom - Réseau alternatif"
        ]
    }
    return mobile_data

# Example of how to use this function
if __name__ == "__main__":
    data = get_mobile_mcc_mnc_codes()
    for i in range(len(data["MCC"])):
        print(f"MCC: {data['MCC'][i]}, MNC: {data['MNC'][i]}, Operator: {data['Operator'][i]}, Description: {data['Description'][i]}")


