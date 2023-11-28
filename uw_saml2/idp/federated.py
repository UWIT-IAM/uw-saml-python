"""Federated Identity Providers."""
from . import IdpConfig, attribute


class CascadiaIdp(IdpConfig):
    #  Added this class to address new Cascadia IdP.
    #  Some parts may still need to be udpated.
    #  entityID and sso_url from CCFederationMetadata.xml, from Cascadia.
    #  _attribute_prefix, id_attribute from FredHutchAzureIdp(IdpConfig)
    #  x509_cert from
    #  CCFederationMetadata.xml IDPSSODescriptor/KeyDescriptor/signing
    entity_id = "http://sts.cascadia.edu/adfs/services/trust"
    sso_url = "https://sts.cascadia.edu/adfs/ls/"
    id_attribute = "employeeNumber"
    x509_cert = """
        MIIC3DCCAcSgAwIBAgIQMIdwSJDYuLVNwseBCkxA4zANBgkqhkiG9w0BAQsFADAq
        MSgwJgYDVQQDEx9BREZTIFNpZ25pbmcgLSBzdHMuY2FzY2FkaWEuZWR1MB4XDTIz
        MDQxNjEwNDY1NFoXDTI0MDQxNTEwNDY1NFowKjEoMCYGA1UEAxMfQURGUyBTaWdu
        aW5nIC0gc3RzLmNhc2NhZGlhLmVkdTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
        AQoCggEBAMe4H/m7hmZkSXYtYSRq9Uc23FwiXqPyeP/DwPR5+1lPVRrA5NskAtLI
        5W4FLm7d+PAKBgCr9RvWzEkvG7YeQOXWInqF2/KObTa0LNogO3zI4Pr2yzIOsFkd
        9X/xx0CSlpckMDJdoc15aXTpSC5PDn/yoKR0+Qk+tP3Pd8X1fg0ShbGhnhPl6tk5
        nXwJSTqPwrKgPr36Sk8vf3uPDvoU6vXjW7Dk9Yoo4gu6RwO+riujjrELdR44aaJ2
        8INho3yL6pLQ9UyT+J5agEIwsTEJeVabdhO8bAsRwXK3UOgbqrJbfcCGQJiQKQWv
        6NL5eYDH8yyjyTwzl8aYWNqhmQVGIXkCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEA
        TZul0d3Ambn5rg75I2IsjqQJckDJfVB9fhSQ2fK9fK1yZ9lRQDox5Zidu8q95ugn
        4cmtSqS/260TvsWvRcJK3KbiZ46DmrlANF9qiAjClKIrv3uYHZb0pJd2j+ZKdVOT
        8EQ2uSOElcY7ZBx+55yAzCW8TSGA3TMLRcKXozfk++HFoLEXbZaTo447BUb9b82U
        Mv42rFI66/59obGWdQ6UHyGCvyN4FBd4nYCcpM6pKxOfhMbAA7F6rcCRYisSjkZe
        5FymL4FYVDuJ6WdSaWEIbpojD8+nnJpS8Yal/8qicwMWCT9VpUDHmsZC5WiKmTXm
        RXE3esrKhhuPEkK1Qk0mLw==
    """


class CascadiaAzureIdp(IdpConfig):
    """
    Cascadia Azure configuration to replace CascadiaIdp (also, using FH as template)
    App Federation Metadata Url https://login.microsoftonline.com/2505efd9-9f5d-4941-865c-03c9b1b88613/federationmetadata/2007-06/federationmetadata.xml?appid=668d7144-d842-4069-a70b-cae9f6ccc14f
    Login URL: https://login.microsoftonline.com/2505efd9-9f5d-4941-865c-03c9b1b88613/saml2
    Azure AD Identifier: https://sts.windows.net/2505efd9-9f5d-4941-865c-03c9b1b88613/
    Logout URL: https://login.microsoftonline.com/2505efd9-9f5d-4941-865c-03c9b1b88613/saml2
    """

    _azure_tenant_id = "2505efd9-9f5d-4941-865c-03c9b1b88613"
    _attribute_prefix = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims"
    _attribute_prefix2 = "http://schemas.microsoft.com/identity/claims"

    entity_id = f"https://sts.windows.net/{_azure_tenant_id}/"
    sso_url = f"https://login.microsoftonline.com/{_azure_tenant_id}/saml2"
    id_attribute = "employeeNumber"
    x509_cert = """
        MIIC8DCCAdigAwIBAgIQW2YmoB9jVZBN+X8BnmMIbTANBgkqhkiG9w0BAQsFADA0
        MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZp
        Y2F0ZTAeFw0yMzA1MDEyMTQ1MDVaFw0yNjA1MDEyMTQ1MDVaMDQxMjAwBgNVBAMT
        KU1pY3Jvc29mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnRpZmljYXRlMIIBIjAN
        BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr+dzHUWeBI5HozHBuB1hFSh67A7m
        lPJxqnNsw4rGV72niCDSzn8eFZUWH2RDQjWRWdjWaaE39ZTPmrAlhi9II0Ezw8IW
        /kGprP/OF9qtXgYZ3Vd0iLSowtmPtvfVDYHs42VHd1pcCGZO68L9cnk0rxJayqjN
        itljXIIrQ4nqSO2aSCx66m/jA6mGFj36+wJle8zHcBPFKlIxaGLx04A72EPVb8Sp
        s4yc1gKhdEHrvGjmqnjlz997iU1H8esLDAwMihO6Ha6tFdj29/JPCTJMWM2bY4dw
        juTEMncRodHVBADdtvasW6JlhcH6KNqvClxU0/x+1dkiiF/2icHYatdHdQIDAQAB
        MA0GCSqGSIb3DQEBCwUAA4IBAQBRhl49scTEf17CBrT9Lk5vsFCrcS/wMpSi569t
        hUmxrQmx9jyEfQ7M4b3bH50nTU6Z/2whJq1Fcy3gHL8zB8UvGLHWnTE2wHQ1+Yzs
        u+mkjAUOgSiFGX5aVHAco6eU/MwgIBcgA4D0+hmcVlrWQlmdq/juXQ7Bto7KYMu+
        52ui4kMavtgftgtfrNmE9b/eKFqTA3wYEXLZVJzclMm3g3VItWnfvRpF/eG8CpjI
        wJPxARowqyxR5q6PWX5JzOtFzuCx0vJ/jI0o8iAg53fOitgDFj3E6/qxjPhoDY+Q
        Pq4dr8god4m9Nr6k8kFWBbL2sXn1GC72SDeuvk0Q4X3t8tLb
    """
    multi_authn_context_x509 = True


class CollegenetIdp(IdpConfig):
    """
    One thing of note about collegenet is that it encrypts attributes and thus
    requires an SP cert and key.
    """

    _idp_url = "https://shibboleth-idp.collegenet.com"
    entity_id = f"{_idp_url}/idp/shibboleth"
    sso_url = f"{_idp_url}/idp/profile/SAML2/Redirect/SSO"
    # persistent id
    id_attribute = "urn:oid:1.3.6.1.4.1.5923.1.1.1.10"
    mapped_id_attribute = attribute.NestedNameid("remote_user")
    _attribute_prefix = "https://applyweb.collegenet.com/account/attribute-def"
    attribute_map = {f"{_attribute_prefix}/act-userId": "collegenet_userid"}
    x509_cert = """
        MIIDYDCCAkigAwIBAgIUE7bIe4hwDfwhSM8wn4E8Rza/AdEwDQYJKoZIhvcNAQEF
        BQAwKDEmMCQGA1UEAxMdc2hpYmJvbGV0aC1pZHAuY29sbGVnZW5ldC5jb20wHhcN
        MTAwMjExMjMxNTMyWhcNMzAwMjExMjMxNTMyWjAoMSYwJAYDVQQDEx1zaGliYm9s
        ZXRoLWlkcC5jb2xsZWdlbmV0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
        AQoCggEBAIFEn4f9ObsbquJlOPvIazrYJ+cltWyFL5My6Sci6K1L/xTfRNAtGA3U
        DQL3wOALSFtfddl/ULTfQYU2/AZKFj7BwA72lou6G9SUco5QchHUoaiCxnOs1LQ8
        kP2rA5nsxwfJrYnGULx1+c7qKmatN+OftKL96LD6g2rBw794FZd7j29ptrqOv97B
        gzVaH5od8ZMvegsKzpuYf0cOklD0dRJEW0ppb79JLJvSrWVX6K9oAvOXJx7+nHwK
        BGqETOU4nhXXJOgyVqib7d3mCg7YWyJXl1tLnTLZrHLi7bVk2BKUZO2yT62SsBy3
        MkThcDHokvyvwo/GUmF2dnJaYj59afUCAwEAAaOBgTB/MF4GA1UdEQRXMFWCHXNo
        aWJib2xldGgtaWRwLmNvbGxlZ2VuZXQuY29thjRodHRwczovL3NoaWJib2xldGgt
        aWRwLmNvbGxlZ2VuZXQuY29tL2lkcC9zaGliYm9sZXRoMB0GA1UdDgQWBBRf5n4e
        0WSw5ow5doI1M71y7rzfGjANBgkqhkiG9w0BAQUFAAOCAQEAGlTRbPUU9d5ond5O
        O3efuPRoIMCurUo6xaTD39rnr5m94Cr55n3dOwCnvjn0IMQvvvqGBJRD92i0VvZI
        4r63QtU5ZqSeAiNG5FFCA89jnR6P0nZqXV3R3mRaRHDM2apD9pNz2PUtFdktw5AB
        cURaOv4usFw8sWMQg0oM3rHC5VbTCCoQbmiRGiMCIqSEJbZ02JG+lUhrv1jp9xNj
        PjDjvSkxTTH3Mo4Lt7jVww76pgWRDa8L0eZ4sOREQVqMXEMcB3JNy7fFimunvxgw
        fIJN0Yk9uqeMFBoZiL8r0itI9BTt4gk2sYDbNnG6/pqoPS9mwmiM22XEeTeG1x3a
        WWeBDw=="""


class FredHutchAzureIdp(IdpConfig):
    """
    Azure doesn't do things the Shibboleth way and FredHutch isn't
    acustomed to using ePPN
    """

    _azure_tenant_id = "0054a3ea-b394-418b-ad1a-174138231fd6"
    _attribute_prefix = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims"
    _attribute_prefix2 = "http://schemas.microsoft.com/identity/claims"

    entity_id = f"https://sts.windows.net/{_azure_tenant_id}/"
    sso_url = f"https://login.microsoftonline.com/{_azure_tenant_id}/saml2"
    id_attribute = f"{_attribute_prefix}/employeeid"
    attribute_map = {
        f"{_attribute_prefix}/name": "saml_unique_name",
        f"{_attribute_prefix2}/objectidentifier": "saml_oid",
        f"{_attribute_prefix2}/displayname": "saml_displayname",
        f"{_attribute_prefix2}/authnmethodsreferences": "saml_authncontextclassref",
    }
    x509_cert = """
        MIIC8DCCAdigAwIBAgIQXSlgym02p6lOI7sRBKoZPzANBgkqhkiG9w0BAQsFADA0
        MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZp
        Y2F0ZTAeFw0yMzA2MTIyMzMzMjNaFw0yNjA2MTIyMzMzMTlaMDQxMjAwBgNVBAMT
        KU1pY3Jvc29mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnRpZmljYXRlMIIBIjAN
        BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0XmQSVQIVDywd03NDFM+o4vaRVWH
        M6LtsXILsr2JXmp0MmVNIWjKXkn8XmJkJRR5c2s8In301Aai5n6SwAnLRKMcwNVH
        v/yGgIDGWYnUZ7MX8eNbvNHuLs/5lmA32ymnw7smOY3VkchBkil95r8E+wI/+bjK
        itDQYUcnTT/UwHnIwvR4kVe/TZ9h0XDHnetVxk42WmT3yG57oe2j5IxC0nBUXEEe
        zAtgxasAPC43TONKAnkq+c4R2FKUDw+VEvx4mtCx8wXHGbzZ1qkWAtIICbDUmTRD
        KpAGCPieVHr3y1sQNXlMqiQrzCvGwl3g2uVBgs2B4UGH+LdIfFSeumqrZQIDAQAB
        MA0GCSqGSIb3DQEBCwUAA4IBAQCEByjFXKQEfZyzeW3WmuNDfiAjOd/NjuEJTrWF
        bdxN5X/ZNfhcU5ldI8xKvsASHtKv+sowgH9cdLKHIasxCCTGsRcBBdqoInUSqajO
        zkeyI6FdhnXjVyu8ko/ZyGT1ORjdtjcm3axagOMAyHjWxT28zWoU7+P5x0P7Itdx
        fMU1NZFfOfsaDjM18iSBDcsYIDeSadDh8knyFRxYGXHYrifEEq5qZBgnXXhYZLse
        4BimG9X9nynGlI6QcU5Qj7gnddQOQpk2OFFAGoUBw+vQaZNZLDGGcyvbRaueuXSh
        4gzm/WDtjnJ/Cod/Qg8OfJLEARBkLQZpvCFlTDFJ1dkDDRMC"""
    multi_authn_context_x509 = True


class SccaIdp(IdpConfig):
    x509_cert = """
        MIIGFzCCBP+gAwIBAgITHQAAAV+l62jdEnLx3AAAAAABXzANBgkqhkiG9w0BAQsF
        ADCB9TELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExDzANBgNVBAcT
        BklydmluZTEfMB0GA1UEChMWU2VjdXJlQXV0aCBDb3Jwb3JhdGlvbjFCMEAGA1UE
        CxM5KGMpIDIwMTUgU2VjdXJlQXV0aCBDb3Jwb3JhdGlvbiAtIEZvciBhdXRob3Jp
        emVkIHVzZSBvbmx5MR0wGwYDVQQLExRDZXJ0aWZpY2F0ZSBTZXJ2aWNlczE8MDoG
        A1UEAxMzU2VjdXJlQXV0aCBHMyBJbnRlcm1lZGlhdGUgQ2VydGlmaWNhdGUgQXV0
        aG9yaXR5IDJBMB4XDTE1MDgyNTE5MTQzMloXDTI1MDUyNzE3NDI0N1owgbcxCzAJ
        BgNVBAYTAlVTMRMwEQYDVQQIEwpXYXNoaW5ndG9uMRAwDgYDVQQHEwdTZWF0dGxl
        MSUwIwYDVQQKExxTZWF0dGxlIENhbmNlciBDYXJlIEFsbGlhbmNlMTIwMAYDVQQL
        EylNYW5hZ2VyIEluZm9ybWF0aW9uIFNlY3VyaXR5IEFyY2hpdGVjdHVyZTEmMCQG
        A1UEAxMdU2VjdXJlQXV0aDAxVk0uc2VhdHRsZWNjYS5vcmcwggEiMA0GCSqGSIb3
        DQEBAQUAA4IBDwAwggEKAoIBAQCpvJ1ejW+XS4VEuY/8RBruZn/ZECeS7cV1Ippo
        ZQsxmJ3PQpb2bQTf6lfqtfVLs7DA7sjX5C7Xcy80RuecVfdbRi+15L5ewwh3lJDD
        vEgtmODne482g4++nHc0r+Tk9wh2mCXk6Bov2z95SjkOgSjR0YQQ4hTWykpky9we
        5TXcPfCl9BSdrnxyWZlabxnY4kKaGHcjCp+/mqzMJ0Eus2j+cfvQPTTp0oUwpRDb
        aD8t/0dEpYbDpjM1Wi6JJ3uxzujK+dm83arxvjSEfqr5/TD3n7pUZb+03zP/PEAO
        FktIDxbe+OgNSQK2YJXNXRYBnIhULakad4ESKsIxiPAWRjutAgMBAAGjggHaMIIB
        1jAOBgNVHQ8BAf8EBAMCBPAwIAYDVR0lAQH/BBYwFAYIKwYBBQUHAwEGCCsGAQUF
        BwMCMB0GA1UdDgQWBBQeD+nQeJjrbxA7UdUHmcJvCgFWfzAzBgNVHREELDAqggls
        b2NhbGhvc3SCHVNlY3VyZUF1dGgwMVZNLnNlYXR0bGVjY2Eub3JnMB8GA1UdIwQY
        MBaAFOktSiOpOlaZiHIelDyJxMDEv5T+MHcGA1UdHwRwMG4wbKBqoGiGZmh0dHA6
        Ly9jbG91ZC5zZWN1cmVhdXRoLmNvbS9DZXJ0SW5mby9TZWN1cmVBdXRoJTIwRzMl
        MjBJbnRlcm1lZGlhdGUlMjBDZXJ0aWZpY2F0ZSUyMEF1dGhvcml0eSUyMDJBLmNy
        bDCBswYIKwYBBQUHAQEEgaYwgaMwgaAGCCsGAQUFBzAChoGTaHR0cDovL2Nsb3Vk
        LnNlY3VyZWF1dGguY29tL0NlcnRJbmZvL011bHRpZmFjdHItVk0yMy5iYW5uZXIu
        bXVsdGlmYWN0b3J0cnVzdDMuY29tX1NlY3VyZUF1dGglMjBHMyUyMEludGVybWVk
        aWF0ZSUyMENlcnRpZmljYXRlJTIwQXV0aG9yaXR5JTIwMkEuY3J0MA0GCSqGSIb3
        DQEBCwUAA4IBAQALVbM7yjZOCMx0l42KVGT5uV+DbflTJ7OFVZDHYYewY6xTaDf3
        Ob3kj5pkHGnKk+Z0hFrg1FixI+/jlzV8jiGI+Ic+oKvemEeyfMrTkGmDlBNznJHA
        NI9ciJ/x8UWMXooYM9il1242T9r+DD+0q5AZhOemhu9iEN2++XzDCZGZLAITNhjo
        5tM6OvHr6xo0Fmr03B11Wwhybgf9ItcFyq14rcwnCQ9/U/p6/jEtYFRUx++a/lZO
        ef3aY+ojRtKVvv0ZaS35cz5lHgVepD0xP/djCj1Uy73JPOkYjuNpq8WsJudj38dC
        4+1iVLOGVJk7934mItYZeFg2VStjumSp830k"""

    def __init__(self, entity_id):
        """This varies by environment and is equivalent to the acs url."""
        self.entity_id = entity_id
        self.sso_url = entity_id


class TestIdp(IdpConfig):
    _idp_url = "https://thor-idp.cac.washington.edu"
    entity_id = f"{_idp_url}/idp/shibboleth"
    sso_url = f"{_idp_url}/idp/profile/SAML2/Redirect/SSO"
    x509_cert = """
        MIIDVzCCAj+gAwIBAgIUedVWX+JQX04XEack4w0QDiIDGlQwDQYJKoZIhvcNAQEL
        BQAwJjEkMCIGA1UEAwwbdGhvci1pZHAuY2FjLndhc2hpbmd0b24uZWR1MB4XDTE4
        MDEwMzE2MDY0MFoXDTM4MDEwMzE2MDY0MFowJjEkMCIGA1UEAwwbdGhvci1pZHAu
        Y2FjLndhc2hpbmd0b24uZWR1MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKC
        AQEAnTQHW/mvtzJc4MVCt7xa/sOWvvsi19MHf6yPMSXOASILNEmXwqBsmjogVQnK
        urjk9sO4tPSWpRFG3vlk5CjFHUHLZlzY6g+h0qcqE6Rh833rqi9IywY9T5wM5ssH
        BbvAbVvGK53oe31DoNn99Ig+PuW3k9QkzF71zGLCSZtSsYNWaErNx5qVX8C+VITM
        gli5SOmKEJXJuOcCwUl1PjxPez/v+9z5WijFhMbYKPxvfwu2HAr+WwMjHucbm/k3
        au2YLwUo9jt+TLZtxhkQKlXilVYZ8rJeFQ1XenqV6+nlH6nPQ92L1thGR4yx3LfM
        85JR1hScRvOAtDultWgZ4xZCYQIDAQABo30wezAdBgNVHQ4EFgQUkFx2WA1kCtdB
        pbcHqTvNWBR8HVQwWgYDVR0RBFMwUYIbdGhvci1pZHAuY2FjLndhc2hpbmd0b24u
        ZWR1hjJodHRwczovL3Rob3ItaWRwLmNhYy53YXNoaW5ndG9uLmVkdS9pZHAvc2hp
        YmJvbGV0aDANBgkqhkiG9w0BAQsFAAOCAQEAcWf5OeoRmz05/itP4GaUL+uJzO4f
        o3bFvU1QwETMm8Lkukh0sdsyDs6cVwgp8Pt738isj52+jwPSzEl+4Iirh8t7c84o
        J4Yj4lhvDXEb7wPPR1/3xWSaMPFFqNHpqqDp5x1Wq7h7MYc/Pq8ApNTISvtnKar8
        vPEek8lr1WxNQfLgaSUyb3uHOCAaQQnLCQzfQGSpqwcn3OsLxfFP5a0jdcXGNPwg
        Ul/zCgXGtpqj0pgaGKncgEwAX/CItsqUmnia58mMAzUQfbEtawSBw8QztBh1uJ/J
        szamvpcczUDLghpfj8byPjyTBIWAeJFVfmOJRsob+NcspvuZXMcKd8o+RQ=="""
