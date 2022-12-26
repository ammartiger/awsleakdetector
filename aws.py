#pthyhon script to search for all hidden AWS crdentials in a folder
#Ammar(ammar.ml)

#usage python3 ./filename /home/kali/Desktop/test
import os
import re
import sys

def find_aws_credentials(folder):
  secret_keys = []
  access_keys = []
  passwords = []
  account_ids = []
  accounts = []
  matches = []
  # Search for files in the given folder
  for root, dirs, files in os.walk(folder):
    for file in files:
      # Open the file and read its contents
      with open(os.path.join(root, file), 'r') as f:
        contents = f.read()

        # Search for AWS secret keys
        secret_key_pattern = r'secret_key[\s]*=[\s]*([\S]+)'
        secret_keys += re.findall(secret_key_pattern, contents)

        # Search for AWS access keys
        access_key_pattern = r'access_key_id[\s]*=[\s]*([\S]+)'
        access_keys += re.findall(access_key_pattern, contents)

        # Search for AWS passwords
        password_pattern = r'password[\s]*=[\s]*([\S]+)'
        passwords += re.findall(password_pattern, contents)

        # Search for AWS account IDs
        account_id_pattern = r'aws_account_id[\s]*=[\s]*([\S]+)'
        account_ids += re.findall(account_id_pattern, contents)

        # Search for AWS accounts
        account_pattern = r'_arn[\s]*=[\s]*([\S]+)'
        accounts += re.findall(account_pattern, contents)

      
        # Search for AWS links
        aws_link_pattern = r'[\w-]*\.s3\.amazonaws\.com'
        matches += re.findall(aws_link_pattern, contents)

  # Print the results
  print(f'Secret keys: {secret_keys}')
  print(f'Access keys: {access_keys}')
  print(f'Passwords: {passwords}')
  print(f'Account IDs: {account_ids}')
  print(f'Resorces: {accounts}')
  print(f'AWS links: {matches}')

# Example usage
find_aws_credentials(sys.argv[1])
