from requests_rest import Client

base_url = 'https://api.github.com/'
rest_client = Client(base_url, debug=True)


def test_github_organizations():
    Organizations = rest_client('organizations')

    r = Organizations.list().response
    print(r.json())
