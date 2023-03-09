# Open input file for reading
with open('emails.txt', 'r') as input_file:
    # Read in all lines and remove any leading/trailing whitespace
    emails = [line.strip() for line in input_file.readlines()]

# Remove any duplicates from the list of emails
unique_emails = list(set(emails))

# Open output file for writing
with open('emails.txt', 'w') as output_file:
    # Write each email to the output file
    for email in unique_emails:
        output_file.write(email + '\n')
