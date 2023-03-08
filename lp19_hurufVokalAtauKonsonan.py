print("=== Program Penentu Huruf Vokal dan Konsonan ===")
vokal=['a','i','u','e','o']
huruf=str(input("Masukan huruf\t:")).lower()

if huruf in vokal:
    print(huruf,"adalah huruf vokal")
else :
    print(huruf,"adalah huruf konsonan")