from kalkulator_vinner import Kalkulator

kalk = Kalkulator()

print(kalk.kalkuler("1 + 2")) # 3
print(kalk.kalkuler("123 - 17")) # 106
print(kalk.kalkuler("50 / 2")) # 25.0
print(kalk.kalkuler("15 * 3")) # 45
print(kalk.kalkuler("3 ^ 5")) # 243
print(kalk.kalkuler("3 / 0")) # Nulldivisjon
