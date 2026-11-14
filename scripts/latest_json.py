"""Manifeste de mise à jour de Tauri (latest.json) à partir des paquets et de leurs .sig.

Usage : python3 scripts/latest_json.py X.Y.Z dist/ > dist/latest.json

L'extension de mise à jour cherche d'abord `{os}-{arch}-{format}` (le format du paquet
installé : appimage, deb, rpm, app, nsis, msi), puis `{os}-{arch}`.
"""

import datetime
import json
import os
import pathlib
import sys

# ZOLDE_RELEASES_URL : autre adresse (essai local).
REPO = os.environ.get(
    "ZOLDE_RELEASES_URL", "https://github.com/alemoreau/zolde-releases/releases/download"
)

# Suffixe du paquet -> clés du manifeste (la première sert aussi de clé sans format).
FORMATS = [
    (".AppImage", ["linux-x86_64-appimage", "linux-x86_64"]),
    (".deb", ["linux-x86_64-deb"]),
    (".rpm", ["linux-x86_64-rpm"]),
    (".app.tar.gz", ["darwin-aarch64-app", "darwin-aarch64"]),
    ("-setup.exe", ["windows-x86_64-nsis", "windows-x86_64"]),
    (".msi", ["windows-x86_64-msi"]),
]


def main(version: str, dist: pathlib.Path) -> None:
    platforms = {}

    for sig in sorted(dist.glob("*.sig")):
        package = sig.with_suffix("")
        for suffix, keys in FORMATS:
            if package.name.endswith(suffix) and package.exists():
                entry = {
                    "signature": sig.read_text().strip(),
                    "url": f"{REPO}/v{version}/{package.name}",
                }
                for key in keys:
                    platforms.setdefault(key, entry)

    if not platforms:
        sys.exit("aucun paquet signé dans " + str(dist))

    manifest = {
        "version": version,
        "notes": f"Zolde {version}",
        "pub_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "platforms": platforms,
    }
    json.dump(manifest, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main(sys.argv[1], pathlib.Path(sys.argv[2]))
