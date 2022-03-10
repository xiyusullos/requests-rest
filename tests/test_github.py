from requests_rest import Client

base_url = 'https://api.github.com/'
rest_client = Client(base_url, debug=True)


def test_github_organizations():
    Organizations = rest_client('organizations')

    r = Organizations.list().response
    _organizations = r.json()
    print(_organizations)

    Orgs = rest_client('orgs')

    id_ = 'github'
    the_org = Orgs.detail(id_)
    r = the_org.response
    print(r.json())

    r = Orgs.partial_update(id_, {
        'org': id_,
        'billing_email': 'billing_email'
    }).response
    print(r.json())

    Orgs.audit_log = Orgs.make_single_action('audit-log', 'GET')
    r = Orgs.audit_log(id_).response
    print(r.json())

    CredentialAuthorizations = rest_client('credential-authorizations')
    OrgsCredentialAuthorizations = the_org(CredentialAuthorizations)
    r = OrgsCredentialAuthorizations.list().response
    print(r.json())

    Installations = rest_client('installations')
    OrgsInstallations = the_org(Installations)
    r = OrgsInstallations.list().response
    print(r.json())