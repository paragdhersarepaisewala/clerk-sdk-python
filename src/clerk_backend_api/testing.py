from typing import Any, Dict, List, Optional, TypeVar, Union
import datetime
import uuid

# Import relevant models and types from the SDK
from src.clerk_backend_api.models import (
    User,
    Session,
    Organization,
    EmailAddress,
    PhoneNumber,
    ExternalAccount,
    Verification,
    OrganizationMembership,
    ClerkErrors,
    Web3Wallet,
    SAMLAccount,
    SignIn,
    SignUp,
    Client,
)
from src.clerk_backend_api.types import (
    UserGender,
    User,
)