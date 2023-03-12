from ipwhois import IPWhois

# Enter the IP address to look up
ip_address = "8.8.8.8"

# Create an IPWhois object for the IP address
ipwhois = IPWhois(ip_address)

# Perform the lookup and store the results in a dictionary
results = ipwhois.lookup_rdap()

# Print the results
print(f"IP Address: {ip_address}")
print(f"Organization: {results['asn_description']}")
print(f"Country: {results['asn_country_code']}")
print(f"City: {results['city']}")
print(f"Latitude: {results['latitude']}")
print(f"Longitude: {results['longitude']}")
