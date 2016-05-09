import os


def get_whois(url):
    print('Scanning Whois.....')
    command = 'whois ' + url
    process = os.popen(command)
    results = str(process.read())
    return results

