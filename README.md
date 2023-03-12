# IP Lookup Python Script

This Python script uses the `ipwhois` library to look up information about an IP address.

## Usage

To use this script, replace `8.8.8.8` with the IP address you want to look up. The script will create an `IPWhois` object for the IP address, perform a lookup using the `lookup_rdap()` method, and store the results in a dictionary. The script will then print out the organization, country, city, latitude, and longitude information for the IP address.
