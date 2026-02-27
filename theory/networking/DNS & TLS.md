---
tags: [theory, networking, dns, tls, security]
status: stub
---

# DNS & TLS

> Name resolution and encrypted transport — the two invisible layers under every HTTPS request.

## DNS (Domain Name System)

### Resolving hostname → IP address

### Recursive vs iterative resolution

### DNS hierarchy: root → TLD → authoritative

### Record types: A, AAAA, CNAME, MX, TXT

### TTL and caching

### DNS over HTTPS (DoH)

## TLS (Transport Layer Security)

### Successor to SSL — encrypts the TCP stream

### TLS handshake: negotiate cipher, exchange keys, verify certificate

### Certificates and the CA (Certificate Authority) chain of trust

### TLS 1.2 vs 1.3 — what changed

### mTLS (mutual TLS) — client also presents a cert

## HTTPS = HTTP + TLS

## See also

- [[OSI & TCP-IP Model]]
- [[HTTP]]
