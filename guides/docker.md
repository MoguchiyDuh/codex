# Docker Cheat Sheet

## Installation

### Universal (Linux)

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER  # Run without sudo (requires logout)
```

---

## Basics

```bash
docker version            # Check version
docker info               # System-wide info
docker help               # General help
```

---

## Containers

```bash
docker run <image>        # Run container
docker run -it <image>    # Run interactive (TTY)
docker run -d <image>     # Run in background (detached)
docker run --rm <image>   # Run and auto-remove on exit
docker run -p 80:80 <img> # Run with port mapping (host:container)
docker run -v /host:/cont # Run with volume mapping

docker ps                 # List running containers
docker ps -a              # List all containers (inc. stopped)
docker stop <id/name>     # Stop container
docker start <id/name>    # Start stopped container
docker restart <id/name>  # Restart container
docker rm <id/name>       # Remove container
docker rm -f $(docker ps -aq) # Remove ALL containers
```

---

## Images

```bash
docker images             # List local images
docker pull <image>       # Download image
docker build -t <tag> .   # Build image from Dockerfile
docker rmi <image>        # Remove image
docker image prune        # Remove unused images
```

### Basic `Dockerfile` Structure

```dockerfile
# 1. Base Image
FROM python:3.9-slim

# 2. Work Directory
WORKDIR /app

# 3. Dependencies (Layer Caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. App Code
COPY . .

# 5. Runtime Config
ENV APP_ENV=production
EXPOSE 80

# 6. Start Command
CMD ["python", "app.py"]
```

> Always use a **.dockerignore** file to skip `node_modules`, `.git`, and large build artifacts to keep images small.

#### `.dockerignore` example

```text
.git
node_modules
*.log
dist/
```

### Multi-Stage Build (Production Pattern)

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Runtime (Final Image)
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

---

## Execution & Inspection

```bash
docker exec -it <id> bash # Open shell in running container
docker logs <id/name>     # View container logs
docker logs -f <id/name>  # Tail container logs
docker inspect <id/name>  # Detailed JSON metadata
docker top <id/name>      # Show running processes in container
docker stats              # Live resource usage (CPU/RAM)
docker cp <id>:<p1> <p2>  # Copy FROM container to host
docker cp <p1> <id>:<p2>  # Copy FROM host to container
```

---

## Docker Compose

```bash
docker-compose up -d      # Start in background
docker-compose down       # Stop and remove containers + networks
docker-compose down -v    # Stop and remove + VOLUMES (data loss!)
docker-compose stop       # Stop containers (don't remove)
docker-compose start      # Start existing containers
docker-compose ps         # List service status
docker-compose logs -f    # Tail all logs
docker-compose logs -f <s># Tail logs for specific service
docker-compose exec <s> <b> # Execute command in service
docker-compose run <s> <b>  # Run one-off command in service
docker-compose build --no-cache # Rebuild from scratch
docker-compose up -d --build    # Rebuild and restart
docker-compose config     # Validate and view config
```

### Basic `docker-compose.yml` Structure

```yaml
version: "3.8"

services:
  web:
    build: . # Build from Dockerfile in current dir
    image: my-app:latest # Name of the built image
    ports:
      - "8080:80" # host:container
    volumes:
      - .:/code # Hot-reloading (host:container)
    environment:
      - DEBUG=true
    depends_on:
      - db # Start order

  db:
    image: postgres:15-alpine
    restart: always
    volumes:
      - db_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=secret

volumes:
  db_data: # Persistent named volume
```

---

## Cleanup & Maintenance

```bash
docker system prune       # Remove UNUSED data (cache, images, etc.)
docker system prune -a    # Remove ALL unused images (not just dangling)
docker volume prune       # Remove unused volumes
docker network prune      # Remove unused networks
```

---

## Search & Ecosystem

- **[lazydocker](https://github.com/jesseduffield/lazydocker)**: Terminal UI for managing containers/images (highly recommended).
- **[ctop](https://github.com/bcicen/ctop)**: Top-like interface for container metrics.
