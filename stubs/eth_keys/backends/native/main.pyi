from .ecdsa import ecdsa_raw_recover, ecdsa_raw_sign, private_key_to_public_key
from eth_keys.backends.base import BaseECCBackend
from eth_keys.datatypes import PrivateKey, PublicKey, Signature
from typing import Optional

class NativeECCBackend(BaseECCBackend):
    def ecdsa_sign(self, msg_hash: bytes, private_key: PrivateKey) -> Signature: ...
    def ecdsa_recover(self, msg_hash: bytes, signature: Signature) -> Optional[PublicKey]: ...
    def private_key_to_public_key(self, private_key: PrivateKey) -> PublicKey: ...
