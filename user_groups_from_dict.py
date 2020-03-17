# Solved this for the Google IT Automation course on Coursera
# It seemed useful, so I saved it here

def groups_per_user(group_dictionary):
	user_groups = {}
  
  # iterates over keys (groups)
  for group in group_dictionary:
  
    # iterates through values (users)
		for user in group_dictionary[group]:
    
      # adds relevant data
			if user in user_groups:
			  user_groups[user] += [group]
			else:
			  user_groups[user] = [group]


	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
