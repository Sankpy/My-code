def parsing_string(email_domain):
    first_section=email_domain.find('@')
    Second_section=email_domain.find(' ',first_section)
    domain=email_domain[(first_section+1):Second_section]
    return domain
print(parsing_string('from sakai@unl.edu mail comes'))
print(parsing_string('from sanketofficial49@gmail.com mail comes'))