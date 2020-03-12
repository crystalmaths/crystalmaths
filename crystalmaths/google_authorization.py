# from apiclient import discovery
# from httplib2 import Http
# import oauth2client
from oauth2client import file, client, tools


def google_authorization():
    """
    This function accesses Google Drive to verify your credentials.
    Once you run it, you should get a link, open this link in a web browser
    and use your Google credentials as requested. Once your cridentials
    accepted by Google, you will geta verification code.
    Copy this code and insert it in a window as requested.
    Once done, you are ready to access files in Google Drive.
    """

    obj = lambda: None
    lmao = {"auth_host_name": 'localhost', 'noauth_local_webserver':
            'store_true', 'auth_host_port': [8080, 8090], 'logging_level':
            'ERROR'}
    for k, v in lmao.items():
        setattr(obj, k, v)

    # authorization boilerplate code
    SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
    store = file.Storage('token.json')
    # store = file.Storage('client_id.json')
    creds = store.get()
    # The following will give you a link if token.json does not exist, the link
    # allows the user to give this app permission
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        # flow = client.flow_from_clientsecrets(credentials, SCOPES)
        creds = tools.run_flow(flow, store, obj)
    return creds
