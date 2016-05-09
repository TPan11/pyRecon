from tld import get_tld


def get_domain_name(url):
    print('Scanning Domain Name.....')
    domain_name = get_tld(url)
    return domain_name
