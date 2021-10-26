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
        MIIC3DCCAcSgAwIBAgIQPLOKuRD2zahHjLCHaRuOEjANBgkqhkiG9w0B
        AQsFADAqMSgwJgYDVQQDEx9BREZTIFNpZ25pbmcgLSBzdHMuY2FzY2Fk
        aWEuZWR1MB4XDTIxMDUyNjA4MjIzMloXDTIyMDUyNjA4MjIzMlowKjEo
        MCYGA1UEAxMfQURGUyBTaWduaW5nIC0gc3RzLmNhc2NhZGlhLmVkdTCC
        ASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMLu9Kw0B0GVCooM
        RTT5WtuOztV53nZVF2K2SHljc5ZK1udiz3qg/BlYgn1hSdiaDL4BcbEo
        u2umchIp8URGpJXAIDhNC7OM8D1MivRVxP1Ei7eG5/WwbTZVG0q4H4x6
        +6AngadYoB5LIHRMcIdXnI7DZ0Py+v9imV8dWJgYFE8Umoz+RV2jmgMV
        Y48hxodmG+h/N7IWwwgLX8bW2Cs2bt7F0/pXWBaGLgrFCj34QmA2Q4Xz
        vcO0pSynpAyx8JiZWQnvWmCV4vnWB4wJ0hJRQTGVdbxiXlykaNU5+qJc
        0Vc8rqrZ8FnrtTxrpjtlG8nbT3lE5YXclLZDVbLIZQaVCSECAwEAATAN
        BgkqhkiG9w0BAQsFAAOCAQEAbxucel2+Nlrimq2b52dUtr2gg9vLj308
        U234e2IEcxaey4m/e/Js7G/BhfiY13wGOqHTFLiOcMh16jkA0ZC7ywMx
        UIKCLLzSL7aoGucVy3lsf4Rqv8Eom0oaVBkw/+cgvlE3cVllLNPxDkss
        qE/XT8UUMstzOGqWb0FuNp3LAtTvLNqVaMKdUdXUtWsQDK+oquxD0l2U
        tL+G0CMCkmJ/bahhsF4BJiMyL+MFO9BhrVEAojIhvwt04jpnlDqk7Md3
        M831nGgl8YQuFBnjEwnl3MqpFsALuXIr1Lq7y0Cxc2Ky0EYvg+nvSnyd
        UxxbKn1l6/GgtOys4W12hpx4KV2Hsg==
    """


class CascadiaStudentIdp(IdpConfig):
    entity_id = "https://idp.cascadia.edu/idp/shibboleth"
    sso_url = "https://idp.student.cascadia.edu/idp/profile/SAML2/Redirect/SSO"
    id_attribute = "urn:mace:washington.edu:dir:attribute-def:stu-validationID"
    x509_cert = """
        MIIDTDCCAjSgAwIBAgIVAKF/idZbWozYUUVYSAZqNtoPhTTpMA0GCSqGSIb3DQEB
        BQUAMCMxITAfBgNVBAMTGGlkcC5zdHVkZW50LmNhc2NhZGlhLmVkdTAeFw0wOTA3
        MTcxNzM0NDZaFw0yOTA3MTcxNzM0NDZaMCMxITAfBgNVBAMTGGlkcC5zdHVkZW50
        LmNhc2NhZGlhLmVkdTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKsC
        6uf6XGhfUYhypRK7BNXr9df4phb1pAISvXXGvICQB/iABP40fbMgk1+RVwjTVXj2
        40JBlmYiHZ69Gcwv6GyIhbouNTb46k5Pp/bmU3K0oqwWHjbE68CyHS5IxRPImAlR
        OeTFI4LFNvnNvZPb7uRhYAg1EgmJXjwscUqssNCmXozesHwM7vEjv/6jfeQ2RLB3
        q2QVVuMEcFYh21+lNY07HmKkxBFSifHu2qKyVpLK7CWd8Qsj7v6cy/ixEc9VJdBJ
        ptridTi2zcv33E4hZGrCvwWjdwPt/evOGOY7umUzOokbT6tqPFTUAmdlEeJKAdyv
        FXVki+85jyJm0xg3FkkCAwEAAaN3MHUwVAYDVR0RBE0wS4IYaWRwLnN0dWRlbnQu
        Y2FzY2FkaWEuZWR1hi9odHRwczovL2lkcC5zdHVkZW50LmNhc2NhZGlhLmVkdS9p
        ZHAvc2hpYmJvbGV0aDAdBgNVHQ4EFgQUtK4D0urHY0BSPPxibiQcjWlp0YkwDQYJ
        KoZIhvcNAQEFBQADggEBAGzAU57okBkfeaRUC1lnOXbjNfX/+XRTBY6dWLhlwxmK
        zJ4yosaCHD6XsXuDwlVOeu0Ms38tvTakGlmLiJ644PKJVfrQeVRY22EKEJnpHMl5
        mIKsRFjSA6we3sot0f/APiMqisieSLJHnd4Q7XXzt5ybBRSbDneEf0ukO+gqGHY2
        TlwHPe9Z73h1R5sQdLlSAUDH/UKm+5uWb0K+o7STppImd0Fs+fEInSIzZk7YpAG3
        v1S5a9uxu9q/jtCa5N49Dgu8H6p9dtqlVtU+v0ZQREpaLSxThI0gXMeDLhHKn+Oh
        4evvj1ikdsX7XBiSpTNiUGMF0D7ZllSqTk+E+/Cyo5Q="""


class CascadiaEmployeeIdp(CascadiaStudentIdp):
    """
    The only difference between an Cascadia Employee and a Student are the
    IdP's endpoint. Even the id_attribute of 'stu-validationID' remains.
    """

    _idp_url = "https://idp.employee.cascadia.edu"
    _attribute_prefix = "urn:mace:washington.edu:dir:attribute-def"
    sso_url = f"{_idp_url}/idp/profile/SAML2/Redirect/SSO"
    attribute_map = {f"{_attribute_prefix}:emp-validationID": "remote_user"}


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


class FredHutchIdp(IdpConfig):
    entity_id = "https://shib.fhcrc.org/idp/shibboleth"
    sso_url = "https://shib.fhcrc.org/idp/profile/SAML2/Redirect/SSO"
    x509_cert = """
        MIIDIzCCAgugAwIBAgIUYqaDH2PjPdZ38g8PPuq3hjmdVQswDQYJKoZIhvcNAQEF
        BQAwGTEXMBUGA1UEAxMOc2hpYi5maGNyYy5vcmcwHhcNMTEwMjIzMjMzNDEwWhcN
        MzEwMjIzMjMzNDEwWjAZMRcwFQYDVQQDEw5zaGliLmZoY3JjLm9yZzCCASIwDQYJ
        KoZIhvcNAQEBBQADggEPADCCAQoCggEBAJDWhNtMACDyyVwdEn7ZTt4teMurPpIQ
        0QAnJB8A/VBo15/kkGQl6GKnjVT0yuXM9iRurwwbDh1nwhIaDX1kVqBCBueu4wh1
        cceN1U+w5mhhWr37jc6hvml9vf/m/2GJcXyOEeneNOf5yo3Lvia4ueoW0qLAbsTr
        36fYe8M1pa0AAudhpqUXDWdlXTfZdkPomufVVef6YpEVpJXxKezaF5BAYeyjAJ+k
        vrIxZXIxghjoFDHkTdf536YAxj23HHp0aUciL2r+QgGhho9i6LRAnMFce5HESL/G
        lIwHJLgvDgozCyw42kEPjQCwU7qBfnY33nmjBHLhw34sFZ1ElMOGbWMCAwEAAaNj
        MGEwQAYDVR0RBDkwN4IOc2hpYi5maGNyYy5vcmeGJWh0dHBzOi8vc2hpYi5maGNy
        Yy5vcmcvaWRwL3NoaWJib2xldGgwHQYDVR0OBBYEFH2yMS2n85KB2MuYt1flMZt4
        rhJLMA0GCSqGSIb3DQEBBQUAA4IBAQAK8eF4qh4l1cMY3X9v3+TN2+Ld+CkowKp/
        ALkr81YRVui4tbMOZ7yQs5WdEY3J4QJrDtQ2tsComdAWb0JIpRwJLHnj1cO3bAel
        jJr8GY4oXUUPGAJpRi5Ly6UKTQKEAHvBdsq6JQQqRLYN5yO1f2lr+QHnizs8rS5a
        +3dB0vs3YxYy1OqKzBLaCH13QkZClNBl87/62OLpnpEm6tAOSiWsD/4unPe2kOW5
        19aqTzwjsV2Am2OINyXSKUK1yA6B5nv9LUzO2ESIH9A06DOYlXWch6u7a0b+3URk
        //e64IUXSJ1NqLsVrX68mC2ysMMojbRiOdmV9mPUcpizb0devpvc"""


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
        MIIC8DCCAdigAwIBAgIQGB680XRFNZhCkepWMRYORjANBgkqhkiG9w0BAQsFADA0
        MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZp
        Y2F0ZTAeFw0yMDAxMjExNjI2NDhaFw0yMzAxMjExNjI2NDhaMDQxMjAwBgNVBAMT
        KU1pY3Jvc29mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnRpZmljYXRlMIIBIjAN
        BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3q25FmIl5g8A0/PsrHHTE9d8/+Om
        j7BGPiZPoml4IZvKeC9cAeE+UdCAOP30QPE0S1+PQHLj0nZwP0X52W7zsXrARfim
        BseOYq0/yuccFEELfywPn9iDEhxJ68jw+QKbkKgfUqPm4/LY2wPLbFXtFL5F3nUB
        M+a3emNlv3C5Gq8hYrevB0jDuNxfqglgrIkAmxNoPrvuOnlAm/FLQSb3EK92WxJ8
        UwBsgOqk4ucSQSQ8BfGlsru8preUrlHv/04q9Byf4tkOFiKL/20IDDAA3shgkqtf
        yOMOkvGmamT5WVT3Ug0JfO18ckwkvWPxSLeclWA9chkmpKrR8+e+7Jz4awIDAQAB
        MA0GCSqGSIb3DQEBCwUAA4IBAQAY2cwjpBCPyTi6NSz/kDq8sIO2H0a+2D1ysmt6
        QgqA/LoDHjnYJ83QHGbAMjIKwopmiLKkiXXyo2mpbqGURSWindf1ab58b/5LhAzv
        mj64tz3btsQrxrJcs2vgrsG3S8oqR3PHGgbAKcoQt6wuX2e0/nf9ZJ+Do/hRQGtL
        lyFsgAW1axDowtLY3Sp8dkRrBlJ6mhMCjfmjgBBiMjRl828nlGJHKiGCdpHh5DSc
        zU0jc67sDs3f04ZzM5F+QZcpjQEOtx6oZOfsLuLZoYhJr/nEPwloY+qIStIBgs7H
        Lci0jyi4EVo6rEh/3JMAnw3mUs2e5naG9j/5Uzvp6crN6gdN"""


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
