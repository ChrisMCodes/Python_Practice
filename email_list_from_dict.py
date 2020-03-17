#passes in a dictionary
#keys are domains
#values are lists of usernames
#return is a list of email addresses

def email_list(domains):
	emails = []
	for domain in domains:
	  for user in domains[domain]:
	    emails.append(user + "@" + domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
