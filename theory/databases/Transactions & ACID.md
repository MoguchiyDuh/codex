---
tags: [theory, databases, transactions, acid]
status: stub
---

# Transactions & ACID

> Grouping operations so they succeed or fail as a unit — the basis of database reliability.

## What a transaction is

## ACID properties

### Atomicity — all or nothing

### Consistency — valid state to valid state

### Isolation — concurrent transactions don't interfere

### Durability — committed changes survive crashes

## Isolation levels

### Read uncommitted — dirty reads possible

### Read committed — no dirty reads

### Repeatable read — no non-repeatable reads

### Serializable — full isolation, slowest

## Concurrency anomalies

### Dirty read

### Non-repeatable read

### Phantom read

## Locking strategies

### Pessimistic locking

### Optimistic locking (versioning)

## Write-ahead log (WAL) — how durability works

## See also

- [[Relational Model]]
- [[../concurrency/Race Conditions & Atomicity|Race Conditions & Atomicity]]
