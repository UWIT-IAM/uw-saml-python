"""UW Identity Provider Configuration."""
from . import IdpConfig, attribute


class UwIdp(IdpConfig):
    """UW's IdP. SP cert and key are not required"""

    entity_id = "urn:mace:incommon:washington.edu"
    sso_url = "https://idp.u.washington.edu/idp/profile/SAML2/Redirect/SSO"
    x509_cert = """
        MIID/TCCAuWgAwIBAgIJAMoYJbDt9lKKMA0GCSqGSIb3DQEBBQUAMFwxCzAJBgNV
        BAYTAlVTMQswCQYDVQQIEwJXQTEhMB8GA1UEChMYVW5pdmVyc2l0eSBvZiBXYXNo
        aW5ndG9uMR0wGwYDVQQDExRpZHAudS53YXNoaW5ndG9uLmVkdTAeFw0xMTA0MjYx
        OTEwMzlaFw0yMTA0MjMxOTEwMzlaMFwxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJX
        QTEhMB8GA1UEChMYVW5pdmVyc2l0eSBvZiBXYXNoaW5ndG9uMR0wGwYDVQQDExRp
        ZHAudS53YXNoaW5ndG9uLmVkdTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC
        ggEBAMH9G8m68L0Hf9bmf4/7c+ERxgDQrbq50NfSi2YTQWc1veUIPYbZy1agSNuc
        4dwn3RtC0uOQbdNTYUAiVTcYgaYceJVB7syWf9QyGIrglZPMu98c5hWb7vqwvs6d
        3s2Sm7tBib2v6xQDDiZ4KJxpdAvsoPQlmGdgpFfmAsiYrnYFXLTHgbgCc/YhV8lu
        bTakUdI3bMYWfh9dkj+DVGUmt2gLtQUzbuH8EU44vnXgrQYSXNQkmRcyoE3rj4Rh
        hbu/p5D3P+nuOukLYFOLRaNeiiGyTu3P7gtc/dy/UjUrf+pH75UUU7Lb369dGEfZ
        wvVtITXsdyp0pBfun4CP808H9N0CAwEAAaOBwTCBvjAdBgNVHQ4EFgQUP5smx3ZY
        KODMkDglkTbduvLcGYAwgY4GA1UdIwSBhjCBg4AUP5smx3ZYKODMkDglkTbduvLc
        GYChYKReMFwxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJXQTEhMB8GA1UEChMYVW5p
        dmVyc2l0eSBvZiBXYXNoaW5ndG9uMR0wGwYDVQQDExRpZHAudS53YXNoaW5ndG9u
        LmVkdYIJAMoYJbDt9lKKMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEB
        AEo7c2CNHEI+Fvz5DhwumU+WHXqwSOK47MxXwNJVpFQ9GPR2ZGDAq6hzLJLAVWcY
        4kB3ECDkRtysAWSFHm1roOU7xsU9f0C17QokoXfLNC0d7KoivPM6ctl8aRftU5mo
        yFJkkJX3qSExXrl053uxTOQVPms4ypkYv1A/FBZWgSC8eNoYnBnv1Mhy4m8bfeEN
        7qT9rFoxh4cVjMH1Ykq7JWyFXLEB4ifzH4KHyplt5Ryv61eh6J1YPFa2RurVTyGp
        HJZeOLUIBvJu15GzcexuDDXe0kg7sHD6PbK0xzEF/QeXP/hXzMxR9kQXB/IR/b2k
        4ien+EM3eY/ueBcTZ95dgVM="""
    attribute_map = {
        "urn:oid:1.3.6.1.4.1.5923.1.1.1.6": "eppn",
        "urn:oid:0.9.2342.19200300.100.1.1": "uwnetid",
        "urn:oid:1.3.6.1.4.1.5923.1.1.1.1": attribute.List("affiliations"),
        "urn:oid:1.3.6.1.4.1.5923.1.5.1.1": attribute.UWGroups("groups"),
        "urn:oid:1.3.6.1.4.1.5923.1.1.1.9": attribute.List("scoped_affiliations"),
    }


class UwIdpTwoFactor(UwIdp):
    two_factor = True


class UwTestIdP(UwIdp):
    entity_id = "urn:mace:incommon:washington.edu:eval"
    sso_url = "https://idp-eval.u.washington.edu/idp/profile/SAML2/Redirect/SSO"


class UwTestIdPTwoFactor(UwTestIdP):
    two_factor = True


uwnetid_attribute_entities = [UwIdp.entity_id, UwTestIdP.entity_id]
