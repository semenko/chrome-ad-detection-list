#!/usr/bin/env python

from hashlib import sha256

map = {}
def update_map(filename):
    with open('hosts-data/' + filename, 'r') as file:
        for line in file.readlines():
            if line.startswith("127.0.0.1") or line.startswith("0.0.0.0"):
                hostname = line.split()[1]
                map[sha256(hostname.strip()).hexdigest()[:16].upper()] = hostname

update_map('someonewhocares.hosts')
update_map('mvps.hosts')
update_map('hosts-file.net')
update_map('malwaredomainlist.com')
update_map('malwaredomains.lehigh.edu')

google_hashes = []
with open('hashed_ad_networks.cc', 'r') as file:
    for line in file.readlines():
        if line.startswith("  \"") and line.endswith("\",\n"):
            google_hashes.append(line.split("\"")[1])

unmapped = []

for hash in google_hashes:
    if hash in map:
        print(map[hash])
    else:
        unmapped.append(hash)

print("%d unmapped of %d total (%.2f%% mapped)" % (len(unmapped), len(google_hashes), (1-(float(len(unmapped))/len(google_hashes)))*100))
