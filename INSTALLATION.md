# Installation

Ce document décrit l'installation et l'exploitation de la plateforme sur OpenShift.

## Prérequis

- OpenShift 4.x (ou Kubernetes compatible)
- Accès à un registre d'images (interne ou externe)
- Accès à un stockage NAS (NFS/SMB) exposé via une StorageClass/PVC
- Accès à une base PostgreSQL (gérée ou auto-hébergée)
- Accès à un système de secrets (OpenShift Secrets ou vault)

## Besoins infrastructure

- **CPU** : 500m à 2 vCPU selon la charge
- **Mémoire** : 512 MiB à 2 GiB selon la charge
- **Stockage** :
  - **Médias** : volume NAS monté via PVC (ReadWriteMany recommandé)
  - **Logs** : stdout/stderr (centralisé via stack d'observabilité)
- **Réseau** : accès sortant vers la base PostgreSQL

## Variables de configuration (exemples)

- `DATABASE_URL` : URL PostgreSQL (ex: `postgresql://user:pass@host:5432/db`)
- `MEDIA_ROOT` : chemin de montage NAS (ex: `/mnt/media`)
- `LOG_LEVEL` : `info`, `warning`, `error`
- `SECRET_KEY` : clé d'application

## Déploiement via Helm

```bash
helm upgrade --install plateforme-skillforge ./helm/plateforme-skillforge \
  --namespace skillforge \
  --create-namespace
```

## Vérifications après déploiement

- Vérifier que le Pod est en état `Running`
- Vérifier l'accès HTTP via la route OpenShift
- Vérifier l'accès à la base PostgreSQL
- Vérifier l'accès en lecture/écriture au volume NAS

## Backups et maintenance

- **Base PostgreSQL** :
  - `pg_dump` quotidien + conservation 7 à 30 jours
  - tests de restauration réguliers
- **Médias NAS** :
  - snapshots ou sauvegarde régulière selon le NAS
- **Dépendances** :
  - mise à jour mensuelle des dépendances
  - scan sécurité (SCA) hebdomadaire

## Sécurité

- Désactiver l'accès public aux endpoints d'administration
- Appliquer des secrets via OpenShift Secrets
- Activer TLS sur la route
- Limiter les droits de service account
- Activer les scans d'image et SAST dans la CI
