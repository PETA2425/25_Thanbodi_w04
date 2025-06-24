print(f"เลขจำนวนเฉพาะเลขบวก")

mixed = [-10,-8,-4,-2,0,3,5,7,9,11,13,17,19,23,29,31,37,41]

for num in mixed:
    if num < 0:
        continue
    sq = num**2
    print(f"{num} = {sq}")