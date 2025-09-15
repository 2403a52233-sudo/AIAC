def deduplicate_emails(emails):
	seen = set()
	result = []
	for email in emails:
		email_lower = email.lower()
		if email_lower not in seen:
			seen.add(email_lower)
			result.append(email)
	return result

# Unit tests
def test_deduplicate_emails():
	assert deduplicate_emails(['A@x.com', 'a@x.com', 'B@y.com']) == ['A@x.com', 'B@y.com']
	assert deduplicate_emails(['a@x.com', 'A@x.com', 'A@x.com']) == ['a@x.com']
	assert deduplicate_emails([]) == []
	assert deduplicate_emails(['C@z.com']) == ['C@z.com']
	assert deduplicate_emails(['A@x.com', 'B@y.com', 'a@x.com', 'b@y.com']) == ['A@x.com', 'B@y.com']

if __name__ == "__main__":
	test_deduplicate_emails()
	print("All tests passed.")
	emails = ['A@x.com', 'a@x.com', 'B@y.com']
	print("Original emails:", emails)
	print("Deduplicated emails:", deduplicate_emails(emails))