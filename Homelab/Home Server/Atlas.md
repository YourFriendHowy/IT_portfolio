## File Structure

`/opt/docker/` is the root, one folder per service:

```
/opt/docker/
├── charon/
│   ├── docker-compose.yml   (hermes-owned)
│   └── data/                (charon-owned)
├── arges/
│   ├── docker-compose.yml   (hermes-owned)
│   └── data/                (arges-owned)
```

`hermes` owns the top-level folder and every `docker-compose.yml` inside it, so it can edit any of them. Each service's `data/` subfolder is owned by that service's own no-login system user (charon:988, arges:987, etc.), so the running container only has write access to its own data — never anyone else's.