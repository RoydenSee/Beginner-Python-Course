monthConversions = {
    "Jan":"January", # Key : Value pair
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}
print(monthConversions["Mar"])
print(monthConversions.get("Mar"))
print(monthConversions.get("luv","Not a valid key."))
