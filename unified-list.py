import os, mimetypes, urllib, tqdm
import urllib.request
dir = os.getcwd()

dns_entries = []

# collect the oisd_big_abp list
for line in urllib.request.urlopen('https://nsfw.oisd.nl'):
    dns_entries.append(line.decode('utf-8'))
print(dns_entries)
print('Big list collected')

# collect the oisd_nsfw_abp list
for line in urllib.request.urlopen('https://nsfw.oisd.nl'):
    dns_entries.append(line.decode('utf-8'))
print('NSFW List collected')

# Collect contents of every file found
for root, dirs, files in os.walk(dir):
    for file in files:
        if mimetypes.guess_type(file)[0] == 'text/plain':
            print(file)
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                file_contents = f.readlines()
                f.close()
            dns_entries.append(file_contents)

# uses list comprehension to remove duplicates from the list

dns_entries_dedup = []
for x in tqdm.tqdm(dns_entries):
    if x not in dns_entries_dedup:
        dns_entries_dedup.append(x)

# Creating file
with open(os.path.join(dir, 'dedup-list.txt'), 'w') as f:
    for l in dns_entries:
        f.writelines(l)
