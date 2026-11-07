facebook = True
twitter = False
instagram = True

if facebook and instagram:
    print("You are a good influencer!")
elif facebook and twitter:
    print("You are a good influencer!")
elif twitter and instagram:
    print("You are a good influencer!")
else:
    print("You are not a good influencer!")