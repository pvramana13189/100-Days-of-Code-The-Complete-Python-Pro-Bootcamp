name1 = input("What is the your name? ")
name2 = input("What is your supposed other half name? ")

combine = name1 + name2
lower_name = combine.lower()

tcount = int(lower_name.count("t"))
rcount = int(lower_name.count("r"))
ucount = int(lower_name.count("u"))
ecount = int(lower_name.count("e"))
lcount = int(lower_name.count("l"))
ocount = int(lower_name.count("o"))
vcount = int(lower_name.count("v"))

first_count = tcount + rcount + ucount + ecount
secong_count = lcount + ocount + vcount + ecount

total_count = int(str(first_count) + str(secong_count))

if total_count < 10 and total_count > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos")
elif total_count > 40 and total_count < 50:
    print(f"Your score is {total_count}, you are alright together")
else:
    print(f"Your score is {total_count}")