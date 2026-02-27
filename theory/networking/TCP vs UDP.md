---
tags: [theory, networking, tcp, udp]
status: stub
---

# TCP vs UDP

> Reliability vs speed — the two transport layer protocols.

## TCP (Transmission Control Protocol)

### Connection-oriented — 3-way handshake (SYN, SYN-ACK, ACK)

### Guaranteed delivery, ordering, error checking

### Flow control and congestion control

### Use cases: HTTP, SSH, databases, file transfer

## UDP (User Datagram Protocol)

### Connectionless — fire and forget

### No ordering, no delivery guarantee, no congestion control

### Much lower overhead

### Use cases: DNS, video streaming, games, VoIP

## Comparison

| | TCP | UDP |
|---|---|---|
| Connection | Yes | No |
| Ordered | Yes | No |
| Reliable | Yes | No |
| Speed | Slower | Faster |
| Header size | 20 bytes | 8 bytes |

## TCP connection teardown (4-way FIN)

## TIME_WAIT state

## See also

- [[OSI & TCP-IP Model]]
- [[Sockets]]
- [[HTTP]]
