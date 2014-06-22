#!/usr/bin/env python

from hashlib import sha256

map = {}
with open('someonewhocares.hosts', 'r') as file:
    for line in file.readlines():
        if line.startswith("127.0.0.1"):
            hostname = line.split()[1]
            map[sha256(hostname.strip()).hexdigest()[:16].upper()] = hostname  # TODO: Catch duplicates from collisions?

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

print("%d unmapped of %d total (%d%% mapped)" % (len(unmapped), len(google_hashes), len(unmapped)/len(google_hashes)))