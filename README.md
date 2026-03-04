| Command                                                                            | Description                                                                                                   |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `docker compose -f docker-compose.yml up -d`                                       | Builds (if needed) and starts all services in detached mode (background) using the `docker-compose.yml` file. |
| `docker compose -f docker-compose.yml ps`                                          | Lists all currently running containers defined in the compose file.                                           |
| `docker compose -f docker-compose.yml ps -a`                                       | Lists all containers (running + stopped) for the compose project.                                             |
| `docker compose -f docker-compose.yml exec django_project bash`                    | Opens an interactive shell (by default `/bin/sh` or `/bin/bash`) inside the `django_project` container.       |
| `docker compose -f docker-compose.yml stop`                                        | Stops all running containers without removing them (they can be restarted).                                   |
| `docker compose -f docker-compose.yml start`                                       | Restarts previously stopped containers without rebuilding or re-creating them.                                |
| `docker compose -f docker-compose.yml down`                                        | Stops and removes all containers, networks, and temporary volumes created by the compose project.             |
| `docker exec -it redis_con redis-cli -u redis://rajesh:Hello123456@127.0.0.1:6379` | Opens an interactive shell inside the `redis_con` container.                                                  |
