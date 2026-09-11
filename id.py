

# the inatial dictionary to start counting tiers
tier_counts = {"Platinum": 0, "Gold": 0, "Silver": 0, "Bronze": 0, "Inactive": 0}
# looking for keys in the total minute dictionary
for contact in total_minutes:
    # if contact from total minutes are big enough for plat tier count them since it starts as zero add one when applicable 
    if get_tier(total_minutes[contact]) == "Platinum":
        # print who the contact is the total minutes of that contact
        print(f"{contact}: {total_minutes[contact]} min ({get_tier(total_minutes[contact])})")
        tier_counts["Platinum"] +=1 
    elif get_tier(total_minutes[contact]) == "Gold":
        print(f"{contact}: {total_minutes[contact]} min ({get_tier(total_minutes[contact])})")
        tier_counts["Gold"] +=1
    elif get_tier(total_minutes[contact]) == "Silver":
        print(f"{contact}: {total_minutes[contact]} min ({get_tier(total_minutes[contact])})")
        tier_counts["Silver"] +=1
    elif get_tier(total_minutes[contact]) == "Bronze":
        print(f"{contact}: {total_minutes[contact]} min ({get_tier(total_minutes[contact])})")
        tier_counts["Bronze"] +=1
    else: 
         tier_counts["Inactive"] +=1
         print(f"{contact}: {total_minutes[contact]} min ({get_tier(total_minutes[contact])})")
         
        
        
 # kinda the same as before but we start with a counter dictionary to get all the minutes for parcing through each tier
tier_counter = {"Platinum": 0, "Gold": 0, "Silver": 0, "Bronze": 0, "Inactive": 0}
# for keys in the total minutes dictionary call minutes the items/the values
for contact, minutes in total_minutes.items():
    if minutes >= 400:
        tier = "Platinum"
    elif minutes >= 200:
        tier = "Gold"
    elif minutes >= 100:
        tier = "Silver"
    elif minutes >= 50:
        tier = "Bronze"
    else:
        tier = "Inactive"

    tier_counter[tier] += 1
    # keys from tier_counter are now called tiers
    contact_tiers[contact] = tier