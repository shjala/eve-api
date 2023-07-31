# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: attest/attest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from certs import certs_pb2 as certs_dot_certs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x61ttest/attest.proto\x12\x15org.lfedge.eve.attest\x1a\x11\x63\x65rts/certs.proto\"\xe4\x01\n\nZAttestReq\x12\x36\n\x07reqType\x18\x01 \x01(\x0e\x32%.org.lfedge.eve.attest.ZAttestReqType\x12\x32\n\x05quote\x18\x02 \x01(\x0b\x32#.org.lfedge.eve.attest.ZAttestQuote\x12*\n\x05\x63\x65rts\x18\x03 \x03(\x0b\x32\x1b.org.lfedge.eve.certs.ZCert\x12>\n\x0cstorage_keys\x18\x04 \x01(\x0b\x32(.org.lfedge.eve.attest.AttestStorageKeys\"\x88\x02\n\x0fZAttestResponse\x12\x38\n\x08respType\x18\x01 \x01(\x0e\x32&.org.lfedge.eve.attest.ZAttestRespType\x12\x36\n\x05nonce\x18\x02 \x01(\x0b\x32\'.org.lfedge.eve.attest.ZAttestNonceResp\x12:\n\tquoteResp\x18\x03 \x01(\x0b\x32\'.org.lfedge.eve.attest.ZAttestQuoteResp\x12G\n\x11storage_keys_resp\x18\x04 \x01(\x0b\x32,.org.lfedge.eve.attest.AttestStorageKeysResp\"!\n\x10ZAttestNonceResp\x12\r\n\x05nonce\x18\x01 \x01(\x0c\"W\n\x0eTpmEventDigest\x12\x35\n\thash_algo\x18\x01 \x01(\x0e\x32\".org.lfedge.eve.attest.TpmHashAlgo\x12\x0e\n\x06\x64igest\x18\x02 \x01(\x0c\"\xd0\x01\n\x10TpmEventLogEntry\x12\r\n\x05index\x18\x01 \x01(\r\x12\x11\n\tpcr_index\x18\x02 \x01(\r\x12\x12\n\nevent_type\x18\x03 \x01(\r\x12\x35\n\x06\x64igest\x18\x04 \x01(\x0b\x32%.org.lfedge.eve.attest.TpmEventDigest\x12\x19\n\x11\x65vent_data_binary\x18\x05 \x01(\x0c\x12\x19\n\x11\x65vent_data_string\x18\x06 \x01(\t\x12\x19\n\x11\x65vent_binary_size\x18\x07 \x01(\r\"u\n\x14\x41ttestGPSCoordinates\x12\x38\n\tgps_input\x18\x01 \x01(\x0e\x32%.org.lfedge.eve.attest.AttestGPSInput\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\"d\n\x11\x41ttestVersionInfo\x12>\n\x0cversion_type\x18\x01 \x01(\x0e\x32(.org.lfedge.eve.attest.AttestVersionType\x12\x0f\n\x07version\x18\x02 \x01(\t\"b\n\x0bTpmPCRValue\x12\r\n\x05index\x18\x01 \x01(\r\x12\x35\n\thash_algo\x18\x02 \x01(\x0e\x32\".org.lfedge.eve.attest.TpmHashAlgo\x12\r\n\x05value\x18\x03 \x01(\x0c\"\xa4\x02\n\x0cZAttestQuote\x12\x12\n\nattestData\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x36\n\npcr_values\x18\x03 \x03(\x0b\x32\".org.lfedge.eve.attest.TpmPCRValue\x12:\n\tevent_log\x18\x04 \x03(\x0b\x32\'.org.lfedge.eve.attest.TpmEventLogEntry\x12:\n\x08versions\x18\x05 \x03(\x0b\x32(.org.lfedge.eve.attest.AttestVersionInfo\x12=\n\x08gps_info\x18\x06 \x01(\x0b\x32+.org.lfedge.eve.attest.AttestGPSCoordinates\"\\\n\x0f\x41ttestVolumeKey\x12<\n\x08key_type\x18\x01 \x01(\x0e\x32*.org.lfedge.eve.attest.AttestVolumeKeyType\x12\x0b\n\x03key\x18\x02 \x01(\x0c\"\x9f\x01\n\x10ZAttestQuoteResp\x12<\n\x08response\x18\x01 \x01(\x0e\x32*.org.lfedge.eve.attest.ZAttestResponseCode\x12\x17\n\x0fintegrity_token\x18\x02 \x01(\x0c\x12\x34\n\x04keys\x18\x03 \x03(\x0b\x32&.org.lfedge.eve.attest.AttestVolumeKey\"b\n\x11\x41ttestStorageKeys\x12\x17\n\x0fintegrity_token\x18\x01 \x01(\x0c\x12\x34\n\x04keys\x18\x02 \x03(\x0b\x32&.org.lfedge.eve.attest.AttestVolumeKey\"_\n\x15\x41ttestStorageKeysResp\x12\x46\n\x08response\x18\x01 \x01(\x0e\x32\x34.org.lfedge.eve.attest.AttestStorageKeysResponseCode\"C\n\x13\x41ttestVolumeKeyData\x12\x15\n\rencrypted_key\x18\x01 \x01(\x0c\x12\x15\n\rdigest_sha256\x18\x02 \x01(\x0c*\x88\x01\n\x0eZAttestReqType\x12\x13\n\x0f\x41TTEST_REQ_NONE\x10\x00\x12\x13\n\x0f\x41TTEST_REQ_CERT\x10\x01\x12\x14\n\x10\x41TTEST_REQ_NONCE\x10\x02\x12\x14\n\x10\x41TTEST_REQ_QUOTE\x10\x03\x12 \n\x1cZ_ATTEST_REQ_TYPE_STORE_KEYS\x10\x04*\x93\x01\n\x0fZAttestRespType\x12\x14\n\x10\x41TTEST_RESP_NONE\x10\x00\x12\x14\n\x10\x41TTEST_RESP_CERT\x10\x01\x12\x15\n\x11\x41TTEST_RESP_NONCE\x10\x02\x12\x1a\n\x16\x41TTEST_RESP_QUOTE_RESP\x10\x03\x12!\n\x1dZ_ATTEST_RESP_TYPE_STORE_KEYS\x10\x04*t\n\x0bTpmHashAlgo\x12\x19\n\x15TPM_HASH_ALGO_INVALID\x10\x00\x12\x16\n\x12TPM_HASH_ALGO_SHA1\x10\x01\x12\x18\n\x14TPM_HASH_ALGO_SHA256\x10\x02\x12\x18\n\x14TPM_HASH_ALGO_SHA512\x10\x03*i\n\x0e\x41ttestGPSInput\x12\x1c\n\x18\x41TTEST_GPS_INPUT_INVALID\x10\x00\x12\x1c\n\x18\x41TTEST_GPS_INPUT_PRESENT\x10\x01\x12\x1b\n\x17\x41TTEST_GPS_INPUT_ABSENT\x10\x02*s\n\x11\x41ttestVersionType\x12\x1f\n\x1b\x41TTEST_VERSION_TYPE_INVALID\x10\x00\x12\x1b\n\x17\x41TTEST_VERSION_TYPE_EVE\x10\x01\x12 \n\x1c\x41TTEST_VERSION_TYPE_FIRMWARE\x10\x02*\xdb\x01\n\x13ZAttestResponseCode\x12\"\n\x1eZ_ATTEST_RESPONSE_CODE_INVALID\x10\x00\x12\"\n\x1eZ_ATTEST_RESPONSE_CODE_SUCCESS\x10\x01\x12)\n%Z_ATTEST_RESPONSE_CODE_NONCE_MISMATCH\x10\x02\x12(\n$Z_ATTEST_RESPONSE_CODE_NO_CERT_FOUND\x10\x03\x12\'\n#Z_ATTEST_RESPONSE_CODE_QUOTE_FAILED\x10\x04*Y\n\x13\x41ttestVolumeKeyType\x12\"\n\x1e\x41TTEST_VOLUME_KEY_TYPE_INVALID\x10\x00\x12\x1e\n\x1a\x41TTEST_VOLUME_KEY_TYPE_VSK\x10\x01*\xb4\x01\n\x1d\x41ttestStorageKeysResponseCode\x12-\n)ATTEST_STORAGE_KEYS_RESPONSE_CODE_INVALID\x10\x00\x12-\n)ATTEST_STORAGE_KEYS_RESPONSE_CODE_SUCCESS\x10\x01\x12\x35\n1ATTEST_STORAGE_KEYS_RESPONSE_CODE_ITOKEN_MISMATCH\x10\x02\x42=\n\x15org.lfedge.eve.attestZ$github.com/lf-edge/eve-api/go/attestb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'attest.attest_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025org.lfedge.eve.attestZ$github.com/lf-edge/eve-api/go/attest'
  _globals['_ZATTESTREQTYPE']._serialized_start=2037
  _globals['_ZATTESTREQTYPE']._serialized_end=2173
  _globals['_ZATTESTRESPTYPE']._serialized_start=2176
  _globals['_ZATTESTRESPTYPE']._serialized_end=2323
  _globals['_TPMHASHALGO']._serialized_start=2325
  _globals['_TPMHASHALGO']._serialized_end=2441
  _globals['_ATTESTGPSINPUT']._serialized_start=2443
  _globals['_ATTESTGPSINPUT']._serialized_end=2548
  _globals['_ATTESTVERSIONTYPE']._serialized_start=2550
  _globals['_ATTESTVERSIONTYPE']._serialized_end=2665
  _globals['_ZATTESTRESPONSECODE']._serialized_start=2668
  _globals['_ZATTESTRESPONSECODE']._serialized_end=2887
  _globals['_ATTESTVOLUMEKEYTYPE']._serialized_start=2889
  _globals['_ATTESTVOLUMEKEYTYPE']._serialized_end=2978
  _globals['_ATTESTSTORAGEKEYSRESPONSECODE']._serialized_start=2981
  _globals['_ATTESTSTORAGEKEYSRESPONSECODE']._serialized_end=3161
  _globals['_ZATTESTREQ']._serialized_start=66
  _globals['_ZATTESTREQ']._serialized_end=294
  _globals['_ZATTESTRESPONSE']._serialized_start=297
  _globals['_ZATTESTRESPONSE']._serialized_end=561
  _globals['_ZATTESTNONCERESP']._serialized_start=563
  _globals['_ZATTESTNONCERESP']._serialized_end=596
  _globals['_TPMEVENTDIGEST']._serialized_start=598
  _globals['_TPMEVENTDIGEST']._serialized_end=685
  _globals['_TPMEVENTLOGENTRY']._serialized_start=688
  _globals['_TPMEVENTLOGENTRY']._serialized_end=896
  _globals['_ATTESTGPSCOORDINATES']._serialized_start=898
  _globals['_ATTESTGPSCOORDINATES']._serialized_end=1015
  _globals['_ATTESTVERSIONINFO']._serialized_start=1017
  _globals['_ATTESTVERSIONINFO']._serialized_end=1117
  _globals['_TPMPCRVALUE']._serialized_start=1119
  _globals['_TPMPCRVALUE']._serialized_end=1217
  _globals['_ZATTESTQUOTE']._serialized_start=1220
  _globals['_ZATTESTQUOTE']._serialized_end=1512
  _globals['_ATTESTVOLUMEKEY']._serialized_start=1514
  _globals['_ATTESTVOLUMEKEY']._serialized_end=1606
  _globals['_ZATTESTQUOTERESP']._serialized_start=1609
  _globals['_ZATTESTQUOTERESP']._serialized_end=1768
  _globals['_ATTESTSTORAGEKEYS']._serialized_start=1770
  _globals['_ATTESTSTORAGEKEYS']._serialized_end=1868
  _globals['_ATTESTSTORAGEKEYSRESP']._serialized_start=1870
  _globals['_ATTESTSTORAGEKEYSRESP']._serialized_end=1965
  _globals['_ATTESTVOLUMEKEYDATA']._serialized_start=1967
  _globals['_ATTESTVOLUMEKEYDATA']._serialized_end=2034
# @@protoc_insertion_point(module_scope)