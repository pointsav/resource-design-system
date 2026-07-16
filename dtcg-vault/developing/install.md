# Customer Fork Procedure

Each customer who wants their own design system runs their own instance of the
substrate from a forked vault.

## What you own

When you fork:

- A Git repository with your tokens, components, themes, and research files
- A binary that runs your instance at your own domain
- No SaaS dependency — the substrate runs as a systemd unit on your server

## Steps

1. Fork [`pointsav/pointsav-design-system`](https://github.com/pointsav/pointsav-design-system) on GitHub
2. Clone your fork to your server
3. Edit `vault/themes/` to add your brand's primitive overrides
4. Run the substrate binary pointed at your vault directory
5. Configure your nginx vhost and certbot

## Configuration

The substrate reads three environment variables:

| Variable | Purpose | Example |
|---|---|---|
| `DESIGN_VAULT_DIR` | Path to your vault directory | `/srv/vault` |
| `DESIGN_TENANT` | Your brand name (matches theme filename) | `acme-brand` |
| `DESIGN_BIND` | Address to bind | `127.0.0.1:9094` |

Detailed deployment guides are in the fleet deployment catalog.
