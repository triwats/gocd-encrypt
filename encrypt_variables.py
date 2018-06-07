# Author: Tristan Watson
# Conforming to PEP8 - keep it that way

# Create and store an encrypted variable within GOCD

import argparse
import base64
import json
import requests


def main():
    ''' main: handles the argparse functionality for arguments'''

    # Define type so we can determine input

    parser = argparse.ArgumentParser(description='Create a new GOCD secret variable')

    parser.add_argument('--username',
                        help="GoCD username", required=True)
    parser.add_argument('--password',
                        help='GoCD password', required=True)
    parser.add_argument('--hostname',
                        help='GoCD hostname', required=True)
    parser.add_argument('-d', '--data',
                        help='The string to encode, or filename', required=False, type=str)
    parser.add_argument('--mode',
                        help='file or string', default='string', required=False)
    args = parser.parse_args()

    params = {}
    params['mode'] = str(args.mode)
    params['username'] = str(args.username)
    params['password'] = str(args.password)
    params['hostname'] = str(args.hostname)
    params['data'] = str(args.data)

    username = params.get('username')
    password = params.get('password')
    hostname = params.get('hostname')
    mode = params.get('mode')
    data = params.get('data')

    if str(mode) == 'file':
        encoded_string = encode_file(data)
        output = store_variable(encoded_string, hostname, username, password)
        print 'Encrypted Value:' + '\n' + output
        return output
    elif str(mode) == 'string':
        encoded_string = encode_string(data)
        output = store_variable(encoded_string, hostname, username, password)
        print 'Encrypted Value:' + '\n' + output
        return output
    else:
        print "Error: Unexpected 'mode' entry: please define string or file"
        return None

    print '\n' + 'Encrypted Value:' + '\n' + output


def encode_string(string):
    ''' encode: encode file into base64 '''

    encoded_string = base64.b64encode(string)
    return encoded_string


def encode_file(filename):
    ''' encode: encode file into base64 '''

    with open(filename, "rb") as f:
        encoded_string = base64.b64encode(f.read())
    return encoded_string


def store_variable(encoded_string, hostname, username, password):
    ''' store_variables: make a request with headers to store var '''

    path = '/go/api/admin/encrypt'
    url = 'https://' + hostname + path
    headers = {'Content-Type': 'application/json', 'Accept': 'application/vnd.go.cd.v1+json'}

    data = {}
    data['value'] = str(encoded_string)
    json_data = json.dumps(data)

    # TODO: We should be verifying SSL as soon as that is in place
    r = requests.post(url, auth=(username, password), headers=headers, data=json_data, verify=False)
    response = r.json()

    if r.status_code != 200:
        print 'Error: ' + str(r.status_code)
        print 'Response: ' + str(r.content)
    else:
        if response['encrypted_value']:
            return response['encrypted_value']
        elif 'encrypted_value' not in response:
            return response
        else:
            print "Nothing found"
    return None


if __name__ == "__main__":
    main()
