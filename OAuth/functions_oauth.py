import secrets
import hashlib
import base64


def generate_codes(length=68):
     code_verifier = secrets.token_urlsafe(length)
     code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
     ).rstrip(b'=').decode('utf-8')
     return code_verifier,code_challenge
                    
                    
                    

                    