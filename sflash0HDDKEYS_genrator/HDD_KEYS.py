#!/usr/bin/env python3

from binascii import hexlify, unhexlify
import sys, os, struct
import hashlib, hmac
from Crypto.Cipher import AES

def aes_encrypt_ecb(key, data):
    crypto = AES.new(key, AES.MODE_ECB)
    return crypto.encrypt(data)

def aes_decrypt_ecb(key, data):
    crypto = AES.new(key, AES.MODE_ECB)
    return crypto.decrypt(data)

def aes_encrypt_cbc(key, iv, data):
    crypto = AES.new(key, AES.MODE_CBC, iv)
    return crypto.encrypt(data)

def aes_decrypt_cbc(key, iv, data):
    crypto = AES.new(key, AES.MODE_CBC, iv)
    return crypto.decrypt(data)

def hmac_sha256(key, data):
    return hmac.new(key=key, msg=data, digestmod=hashlib.sha256).digest()

# Convert hex strings to bytes
portability_seed_key = unhexlify('E973A44C578757A73492625D2CE2D76B')
portability_seed = unhexlify('DF0C2552DFC7F4F089B9D52DAA0E572A')

# Generate portability key
portability_key = aes_encrypt_ecb(portability_seed_key, portability_seed)

# Generate keys from seeds
eap_hdd_key_blob_key1_seed = unhexlify('7A49D928D2243C9C4D6E1EA8F5B4E229317E0DCAD2ABE5C56D2540572FB4B6E3')
eap_hdd_key_blob_key2_seed = unhexlify('921CE9C8184C5DD476F4B5D3981F7E2F468193ED071E19FFFD66B693534689D6')

eap_hdd_key_blob_key1 = aes_encrypt_ecb(portability_key, eap_hdd_key_blob_key1_seed)
eap_hdd_key_blob_key2 = aes_encrypt_ecb(portability_key, eap_hdd_key_blob_key2_seed)

use_new_blob = False

with open('sflash0', 'rb') as SFLASH0:
    data = SFLASH0.read()

print('[DEBUG] ' + hexlify(data[0x1C91FC:0x1C9200]).decode('ascii'))

# Use byte literals for comparisons
if data[0x1C91FC:0x1C9200] == b'\xE5\xE5\xE5\x01':
    print('[DEBUG] ' + hexlify(data[0x1C9240:0x1C9250]).decode('ascii'))

if data[0x1C9240:0x1C9250] == b'\xFF' * 16:
    eap_hdd_wrapped_key = data[0x1C9200:0x1C9240]
    print('[DEBUG] LEN 40 | ' + hexlify(eap_hdd_wrapped_key).decode('ascii'))
else:
    eap_hdd_wrapped_key = data[0x1C9200:0x1C9260]
    print('[DEBUG] LEN 60 | ' + hexlify(eap_hdd_wrapped_key).decode('ascii'))

print('[DEBUG] ' + hexlify(data[0x1C9060:0x1C9064]).decode('ascii'))
smi_version = struct.unpack('<i', data[0x1C9060:0x1C9064])[0]

if use_new_blob:
    eap_hdd_key_blob_enc = unhexlify('CFFDCB6ECAE612B7A30A9EDBD8F77E261D629DE5E6CA3F22F439211AC033884F4B5D7D16D0A6F65D3173A2586CF819C7C6F437444C1D9499F6EBC4145E0BBAABC1DE7C63ED1F5A1E1946358C7F181B1FAB6DAB31195D8E611A1CB81B9ACF8B38FF21029FAB568C7A1BCC3E2FBEB25B13F1AFD6A3599EEF09EAEBE32684FDDA29')
    eap_hdd_key_blob_sig = unhexlify('4798B78DD422601F26A32A1FEC5CAB8B256E50958E0B11A31D77DEE201D4D00E')
    eap_hdd_key_blob_iv = unhexlify('462500ECC487F0A8C2F39511E020CC59')
else:
    eap_hdd_key_blob_enc = unhexlify('E073B691E177D39642DF2E1D583D0E9A5A49EDF72BE9412E2B433E51490CE973234B84F49E949F03727331D5456F4598F2EDE6D0C11483B84CE3283243D0DE9DC379E915301A805DFAEB292B30374C9BF1C59041509BF11D215C35D5C08E3330807C8229C930FAB88672C4CF7DACA881C323D72346CA07921DB806FC242A2ED1')
    eap_hdd_key_blob_sig = unhexlify('ED4F32C095847C6D3143EFFD61E7582F75F24465855C4E94DAF34885D8D03463')
    eap_hdd_key_blob_iv = unhexlify('3286EA97F3E92C434E1DC170C9289003')

selected_key = eap_hdd_key_blob_key1
computed_signature = hmac_sha256(selected_key[0x10:0x20], eap_hdd_key_blob_enc)
if computed_signature != eap_hdd_key_blob_sig:
    selected_key = eap_hdd_key_blob_key2
    computed_signature = hmac_sha256(selected_key[0x10:0x20], eap_hdd_key_blob_enc)
    if computed_signature != eap_hdd_key_blob_sig:
        print('error: invalid signature')
        sys.exit()

eap_hdd_key_blob = aes_decrypt_cbc(selected_key[0x00:0x10], eap_hdd_key_blob_iv, eap_hdd_key_blob_enc)

# Check magic with bytes literal
if not eap_hdd_key_blob.startswith(b'SCE_EAP_HDD__KEY'):
    print('error: invalid magic')
    sys.exit()

# Commented out the hardcoded blob as it might be test data
'''
eap_hdd_key_blob = b'SCE_EAP_HDD__KEY' + unhexlify(
    'BB6CD66DDC671FAC3664F7BF5049BAA8C4687904BC31CF4F2F4E9F89FA458793811745E7C7E80D460FAF2326550BD7E4D2A0A0D9729DE5D2117D70676F1D55748DC17CDF29C86A855F2AE9A1AD3E915F0000000000000000000000000000000000000000000000000000000000000000'
)
'''

if use_new_blob:
    eap_hdd_unwrapped_key = aes_decrypt_cbc(
        eap_hdd_key_blob[0x60:0x70], 
        b'\0' * 0x10, 
        eap_hdd_wrapped_key[:0x40]
    )
else:
    eap_hdd_unwrapped_key = aes_decrypt_cbc(
        eap_hdd_key_blob[0x50:0x60], 
        b'\0' * 0x10, 
        eap_hdd_wrapped_key[:0x40]
    )

eap_hdd_key_offset = 0x10 if (smi_version == 0xFFFFFFFF or smi_version < 0x4000000) else 0x20
eap_hdd_unwrapped_key_dec = aes_decrypt_cbc(
    eap_hdd_key_blob[eap_hdd_key_offset:eap_hdd_key_offset + 0x10],
    b'\0' * 0x10,
    eap_hdd_unwrapped_key
)

if eap_hdd_unwrapped_key_dec[0x10:0x20] != b'\0' * 0x10:
    eap_hdd_unwrapped_key_dec = aes_decrypt_cbc(
        eap_hdd_key_blob[eap_hdd_key_offset:eap_hdd_key_offset + 0x10],
        b'\0' * 0x10,
        eap_hdd_wrapped_key[:0x10]
    )

if use_new_blob:
    eap_partition_key = hmac_sha256(
        eap_hdd_unwrapped_key_dec[:0x10], 
        eap_hdd_key_blob[0x40:0x50]
    )
else:
    eap_partition_key = hmac_sha256(
        eap_hdd_unwrapped_key_dec[:0x10], 
        eap_hdd_key_blob[0x30:0x40]
    )

tweak_key = eap_partition_key[0x00:0x10]
data_key = eap_partition_key[0x10:0x20]

print('XTS data key:', data_key.hex().upper())
print('XTS tweak key:', tweak_key.hex().upper())

with open('keys.bin', 'wb') as keys:
    keys.write(data_key)
