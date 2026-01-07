# Architecture & flux réseau

## Composants

- **Frontend** : application web (SSR optionnel)
- **Backend API** : service FastAPI (REST/JSON)
- **Base de données** : PostgreSQL
- **Stockage médias** : NAS monté via PVC (ReadWriteMany)
- **Observabilité** : logs stdout/stderr + métriques (Prometheus)

## Flux réseau

1. Client -> Route OpenShift (TLS)
2. Route -> Service -> Pod (Backend API)
3. Backend -> PostgreSQL (réseau interne)
4. Backend -> NAS (mount via PVC)

## Sécurité

- TLS sur la route
- Secrets via OpenShift Secrets
- Accès DB et NAS restreint au namespace
