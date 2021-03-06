from eth_keys.datatypes import PrivateKey, PublicKey, Signature
from typing import Any, Optional, Union

def backend_property_proxy(name): ...

class KeyAPI:
    backend: Any = ...
    def __init__(self, backend: Optional[Any] = ...) -> None: ...
    @property
    def backend(self): ...
    @backend.setter
    def backend(self, value): ...
    PublicKey: Any = ...
    PrivateKey: Any = ...
    Signature: Any = ...
    def ecdsa_sign(self, message_hash: bytes, private_key: Union[PrivateKey, bytes]) -> Optional[Signature]: ...
    def ecdsa_verify(self, message_hash: bytes, signature: Union[Signature, bytes], public_key: Union[PublicKey, bytes]) -> Optional[bool]: ...
    def ecdsa_recover(self, message_hash: bytes, signature: Union[Signature, bytes]) -> Optional[PublicKey]: ...
    def private_key_to_public_key(self, private_key): ...

lazy_key_api: KeyAPI
