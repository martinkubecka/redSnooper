import tldextract


def main():
    with open('google_domains.txt', 'r') as file:
        lines = file.read().splitlines()

    domains = []
    for entry in lines:
        _, domain, _ = tldextract.extract(entry)
        domains.append(domain)

    domain_set = set(domains)
    domains = list(domain_set)

    with open('parsed_google_domains.txt', 'w') as file:
        for entry in domains:
            file.write(f"{entry}\n")


if __name__ == '__main__':
    main()
