import csv


def writeItems(website, email, password):
    vault = 'test.csv'
    headerList = ['Website', 'email', 'password']
    with open(vault, mode='a+') as vault:
        vault_writer = csv.writer(
            vault, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,)
        vault_writer.writerow(['Website:' + website, ' Email:' + email, ' Password:' + password])


writeItems("google.com", "noah@nemecfamily.com", "123456678")
