from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import ServiceAccountCreds

from app.constants import GOOGLE_AUTH_URL
from app.core.config import settings

SCOPES = [
    f'{GOOGLE_AUTH_URL}spreadsheets',
    f'{GOOGLE_AUTH_URL}drive'
]

INFO = {
    'type': settings.type,
    'project_id': settings.project_id,
    'private_key_id': settings.private_key_id,
    'private_key': settings.private_key,
    'client_email': settings.client_email,
    'client_id': settings.client_id,
    'auth_uri': settings.auth_uri,
    'token_uri': settings.token_uri,
    'auth_provider_x509_cert_url': settings.auth_provider_x509_cert_url,
    'client_x509_cert_url': settings.client_x509_cert_url
}

cred = ServiceAccountCreds(scopes=SCOPES, **INFO)


async def get_service():
    async with Aiogoogle(service_account_creds=cred) as aiogoogle:
        yield aiogoogle
