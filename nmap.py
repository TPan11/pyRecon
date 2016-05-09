import os


def get_nmap(options, ip):
    print('Scanning nmap.....')
    command = 'nmap ' + options + ' ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results


print(get_nmap('-F', 'thenewboston.com'))