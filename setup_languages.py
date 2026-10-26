import argostranslate.package

argostranslate.package.update_package_index()

available_packages = argostranslate.package.get_available_packages()

wanted_pairs = [
    ("en", "fr"), ("fr", "en"),
    ("en", "es"), ("es", "en"),
    ("en", "de"), ("de", "en"),
]

for from_code, to_code in wanted_pairs:
    print(f"Installing {from_code} to {to_code}...")
    package = list(filter(lambda x: x.from_code == from_code and x.to_code == to_code, available_packages))[0]
    argostranslate.package.install_from_path(package.download())
    print(f"Finished {from_code} to {to_code}")

print("Done installing language packages!")