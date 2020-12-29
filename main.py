# python3 list, tuple and dictionary

"""
# list is a mutable sequency
days=["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print(days)
days.append("Twi")
print(days)
del days[len(days)-1:len(days)]
days.reverse()
print(days)
"""

"""
# tuple is an immutable sequency
days=("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
"""

# dictionary
suyoung = {
  "name": "Suyoung",
  "age": 23,
  "Korean": True,
  "fav_food": ["삼겹살", "회", "치킨"]
}

print(suyoung)
print(suyoung["fav_food"])
suyoung["uni"] = "SNUST"
print(suyoung)