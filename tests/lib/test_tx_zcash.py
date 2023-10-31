import electrumx.lib.tx as tx_lib
from electrumx.lib.hash import hash_to_hex_str

# Launch test:
# pip3 install pytest
# ~/.local/bin/pytest ./tests/lib/test_tx_zcash.py

# https://zips.z.cash/zip-0225
tests = [
    ("56e806faf4f65661fd2c9294ca3fbc65bc24eb102722a2a21c290ac2dc67b11f","050000800a27a726b4d0d6c2f7c919002aca190001e1a049c2fb3857b9f7198d3bee0d89f55c0f6c58452d59a5b90f016a28f71fd4010000006a4730440220255df3de1aa8039f8f0a2540e5b0a5fa1f6dca956fd3950c1db9ba201d94721c02200325cd66a7de814668409c79e25cb6b29a1256842f16be91c079ff02ad888e330121022c6e35dc470bdb9e80a99ec8ce2738386cc580236c34819f9dcdcf9435e01819feffffff026d68cf0c000000001976a9144fd8aa604033240ad3efb8c8cfc8fe5a5d1f0a8288ac9af71b0a030000001976a91405b8cbd7b6ef547ad44172be8e3bfcb5ae77779b88ac000000"),
    ("25f4d054a83a67dd5f4878861263402e89beadf1d59a9470fa1dd90b11639d7f","050000800a27a726b4d0d6c23abe19006dbe190001ae45bbbbfc709edec68b89c5aafa0914facb3f929c693da149b17c3e85ca005a000000006a47304402201ca943bc8bdf8ca506e43c20947c8936b4100fec949438d5fcbfbde48a443d9c02206a216bd605a02ee60d11bb340ee4bc305e6292037f12856eb48691b775d72fb30121026e04f57735f7ea295ec96248448eaa72fd1bfbd97cd4704b8ae1e1ac82b7862ffeffffff055946f006000000001976a9141660fa90eda82439d36fef67c38b989975c4190488ac9819a800000000001976a914370fa16c4e389ed1b5bd1c8462a429408ed1ee3188ac578eff02000000001976a914550c204e931b8402586609bae63bb7d119a1f78388ac8dee5cb5000000001976a914ff4ef1c8fbae2255d053b998c4ec4cd7d2a35a5088ac4d37ce01000000001976a914cd0a4792f8436beaac60f7748f3f5723497c4bab88ac000000"),
    ("289689291c4adf88c4ce718238e56729770d7040ab9a2f0ef8d04b7e61df4d71","0400008085202f8901b1256aa3dba2771f64b5f678dc7a075006b1ddf9874298d38e8c244b56d466a2010000006a47304402204d016ef3d47c268a4be8ef69bdd3bd7c077afc26ea09f39b6772e7b81f494ff502202734513d42037f44ff31991f48a43e5ae19b6029ec0325fe7d026c3759ad876701210369092ebdc9a84e5c3d74ece766025c799558407515fd3b05a2fcc3efc82f3c41feffffff02572c1601000000001976a9147a0c4851304b99284f5d94819b5096fbb08596a188acaf381d03000000001976a9147e171601543a3277e99486edda1a5049ddf7c0e688ac00000000000000000000000000000000000000"),
    ("ca6abd8ef7d6ef158a4a35ea2c2c0cf122f2f664a88f8fa5b6fd79e48c5bed59","050000800a27a726b4d0d6c20000000068be1900000001a05c5685b75252c400119ebc80878f8003e900b6a6ca9febdcd74d97a129e58ff6c66e590b881722930ff701bcd5381b7c82ea343da022617b6aea98fe9cb8c97eced1a714d6e8a649160b15ec659fc001e17ec405224389505926a0b4785a3401814cc194f3fc5eed11f6b11a3b5eee6675273537413c17a9da5411b832177e91121bc9572146c399626617403b55e502a941ab7fbff6708f8a417f24b98ddc582526d9e36bddef4234a4a70c24874cab827faf76d8b628065ee299dbdf728b56d152357b271efe7633420eb52d3dc381f04ff0924a52a83bdd0cb21ae393fac38b44aa95483da277f78054b58f7739f3fd4d52b7a2b980702415438d6b926d73e4a5205fcffb1d9c94e49638d796ee4fc164f49656fbb03735266dc9396ad2296a40850f91a0d0e2ef331ee7b73ceded08d7a183997f3c9de5d6fd0e7d2bcb5f0286128955048886b22e48e45e7d1a36e521d10eeb0b2e3620c99508213e2e69458ad1b59c71b399022092fe074ccbbb44601cc3ed3b029828f7c387e96dbfe02fe55a91db9d4ba22004e7921dba6dc202f559882ee8e0796e9fd28415e6301840fba7afda13ed92cd533258ef70170b3911f0bb67f03ddceca9d1481d28ddd3e249835052408499a6e84fb72ca33c95fcfd7bfb184ba4479bcba65c0f606885c546df02f373d748d2c3da3f7b8467674ddfa1ab6cae1c70c968983511669ad23e2c79d63bae301719831032e14333f2e50de3548c5a97227af4463fe89c8d26cf5b075fbc20677a67b629ce40466452071800a553e35a035e9f33f0a35736af85b617a95b828df0cc700cc9ada04cbe2c835f7838c17b87c7704600ac9e4469520395e64d0c3a1b3adae419c43671aef6e87b45da4e1993d620507f1ed7df0acfae3a0dae723ab8121ea71fbe90cf19f85685732538f89b039e9bf70684486b3d5c75777a2bf03d5f8c5afc0cbae11253a119e894bd7712e68c6489c9479163d3edabce29fba0d64350e7f95a688e4d138365731baf8abbe12fddd29157ecff161a43fd54237055bef0a734c5a05e95ec8e16aa2a47d485add9f1652f9b23aa11417184d10b5430e0a212cfbc86e76ec537f361a361fbd80286d6dc529528a6b29f52798cdf0397eaf892f6b7e2280c520521e3c92d3c7cd89d26965839dd7dc3ee0bcbbbd8e61afcad546e18537091ae98fca9e8030000000000009f600fe22c07fd60d49559791edcf74ecef542f800ab0adcfeda49684655044c92b7b64d4d49babad06049c4ea3f80fab97a0dabd0efbbddbf0f0da587f1a283f08751b05e84f9d94072052e3ef5daa38be31854f23a7addb15dbcee78c726b633d11fcf282df523fa60109e9b331488017222a74f594c0da57308a3d111776e0aacb93d56966cdc9ea880dde72f8b79044aa39effc78e4d2c096ffa32731c9e38d2f1b0674e653d6a4a3cf5e5a2b1cb9621ac41231cadb9896658b0e4c4f3e1806bd6cae2925406c59e15b62aa6eb3472114eecf6603134864d28d0c2c0759e30ec5be5f7cf2b7926e86a7d4e8a613caf063119e9be48064f64356a8a36a1ca6a1577b0120c536a68f70f56a32935e8868418eedc046fcf8581ed3c182e2c04a982d1cf6d14f5f3c23ad71be8d39a9c424171405cd96c9ca5a85d04b7db74ac552ec1e2f902cc0d272d05d47aaa203f966723939d77eb8600db51c1c8373e70825bd88184bf16f2cf6a9ac98790aed138882f0eb69d3d5d4e6bf4bf9b865bfc0fc5e7b54d184fe88c843884cc813773f00efd39d79067dbf8d67859c3afe42bdc041cf567a25d35527dbd7cfd4253fb90e4e90c570202824eb19faa1a1bc65b45ec99518d1ea5515e8e1f9139443ec4df871038000279342e980e4b354270c70e3b78749696f50aea162c0e52df94f6eb7b616a46131f9300dd00c251ee9b8adbf98f540c32f5c19a3c929453db7c5117eeb2fda9291cdd5314b2d6ae9f880000")
]

def test_tx_txids():
    for test in tests:
        txid = test[0]
        test = bytes.fromhex(test[1])
        deser = tx_lib.DeserializerZcash(test)
        # _tx = deser.read_tx()
        _tx, _tx_hash = deser.read_tx_and_hash()
        # print(type(_tx), hash_to_hex_str(_tx_hash))
        # if len(_tx.outputs) > 0:
        #     for output in _tx.outputs:
        #         print(hash_to_hex_str(_tx_hash) + ": " + output.pk_script.hex() + " - " + str(output.value))
        assert hash_to_hex_str(_tx_hash) == txid

# def main():
#     test_tx_txids();

# if __name__ == "__main__":
#     main()