# Zolde : paquets

Ce dépôt contient les versions installables de Zolde, une application de finances
personnelles qui garde vos données sur vos appareils. Il ne contient pas le code source,
qui est privé.

Les versions sont dans l'onglet [Releases](https://github.com/alemoreau/zolde-releases/releases).

## Installation

### Linux

- **AppImage** (recommandé, toutes distributions) : télécharger `Zolde_X.Y.Z_amd64.AppImage`,
  le rendre exécutable (`chmod +x`), puis le lancer. Les mises à jour remplacent le fichier
  elles-mêmes.
- **Debian, Ubuntu** : `sudo apt install ./Zolde_X.Y.Z_amd64.deb`.
- **Fedora, openSUSE** : `sudo dnf install ./Zolde-X.Y.Z-1.x86_64.rpm`.

Avec le `.deb` ou le `.rpm`, la mise à jour demande le mot de passe administrateur.

### macOS (Apple Silicon)

Ouvrir le `.dmg` et glisser Zolde dans Applications. L'application n'est pas encore
signée par Apple : à la première ouverture, lancer dans un terminal

```bash
xattr -cr /Applications/Zolde.app
```

### Windows

Lancer `Zolde_X.Y.Z_x64-setup.exe`. L'application n'est pas encore signée : Windows
SmartScreen demande une confirmation (« Informations complémentaires », puis
« Exécuter quand même »).

### Android

Télécharger `Zolde_X.Y.Z.apk` sur le téléphone et l'ouvrir ; Android demande d'autoriser
l'installation depuis le navigateur. Pour être prévenu des nouvelles versions :
[Obtainium](https://obtainium.imranr.dev/), avec l'adresse de ce dépôt.

## Mises à jour

Au démarrage, l'application de bureau lit `latest.json` dans la dernière version publiée.
Si une version plus récente existe, elle propose de l'installer. Le paquet est signé par
la clé de Zolde, et l'application refuse tout paquet qui ne l'est pas.

Vos données ne sont pas touchées par une mise à jour. Elles restent dans le dossier de
l'application : `~/.local/share/Zolde` sous Linux.
