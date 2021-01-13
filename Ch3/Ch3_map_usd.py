def gbp_to_usd(temp):
    return round(temp * .8, 2)


usd = []
gbp = [6.70, 32.51]
for m in map(gbp_to_usd, gbp):
    usd.append(m)

print(usd)

# list comprehension of the map function
usd2 = [gbp_to_usd(temp) for temp in gbp]
print('usd2 is', usd2)
