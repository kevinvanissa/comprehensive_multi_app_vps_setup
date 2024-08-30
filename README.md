# Multi-App Deployment with Docker and Caddy

## Overview

This project demonstrates how to deploy a multi-application setup on a Virtual Private Server (VPS) using Docker, Docker Compose, and Caddy. The setup includes:

- **Portfolio App** (`app1`)
- **Blog App** (`app2`)
- **Event App** (`app3`)
- **Todo App** (`app4`)

All apps are built using Flask and Gunicorn and are configured to run on separate subdomains. The database used is MariaDB. The individual apps can run in standalone mode and development mode with docker. These states depend on the APP_STATE environment variable. If running the apps individually in standalone mode, you will need to set the APP_STATE environment variable:
```bash
export APP_STATE=standalone
```
You will also need to create a virtual environment. The structure of these individual apps follow the structure here [flask-htmx-app-structure](https://github.com/kevinvanissa/flask-htmx-app-structure), so you can follow the steps there.
However, the easiest way to run this system, is to use docker compose as demonstrated below.

If running with docker compose, then this will be already set and you will not need to worry about sending the APP_STATE variable.

## Prerequisites

- Docker
- Docker Compose
- A Linux server (VPS) or local environment
- Basic knowledge of Docker, Docker Compose, and Caddy
- Root or sudo privileges for modifying `/etc/hosts` on your local machine (for local testing)

## Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Create a `.env` File**

   Create a `.env` file in the root of the project with the following content:
(**DO NOT** store `.env` file on github as it stores sensitive information. It was stored here just for demonstration.)
   ```env
   DB_PASS=your_mariadb_root_password
   ```

3. **Modify `/etc/hosts` (for local development)**

   To test locally, add the following entries to your `/etc/hosts` file:

   ```
   127.0.0.1 portfolioapp.localhost
   127.0.0.1 blogapp.localhost
   127.0.0.1 eventapp.localhost
   127.0.0.1 todoapp.localhost
   ```

   Replace `127.0.0.1` with your VPS IP address if deploying on a remote server.

4. **Start the Application**

   Build and start the Docker containers using Docker Compose:

   ```bash
   docker compose up --build
   ```

   This command will build the Docker images for each app, set up the MariaDB database, and start the Caddy reverse proxy.

5. **Access the Applications**

   - **Portfolio App**: [https://localhost](https://localhost)
   - **Blog App**: [https://blogapp.localhost](https://blogapp.localhost)
   - **Event App**: [https://eventapp.localhost](https://eventapp.localhost)
   - **Todo App**: [https://todoapp.localhost](https://todoapp.localhost)

   Adjust the URLs as necessary if running on a remote server.

6. **Take down the Application**
```bash
docker compose down
```

## Configuration

### Docker Compose

The `docker-compose.yml` file defines the services:

- **`app1` to `app4`**: The four Flask applications, each with its own Dockerfile.
- **`db`**: The MariaDB database folder with start up sql files for the applications.
- **`caddy`**: The Caddy web server configured to serve the apps on subdomains.

### Caddyfile

The `Caddyfile` located at `./deployment/dev/Caddyfile` contains the configuration for routing requests to the appropriate apps. Adjust this file as needed to match your domain setup.

## Volumes

The Docker Compose configuration uses named volumes for persistent data:

- **`mariadbdata`**: For MariaDB data persistence.
- **`caddy_data`**: For Caddy data.
- **`caddy_config`**: For Caddy configuration.

## Troubleshooting

- **Container Logs**: Check logs for individual containers using:

  ```bash
  docker-compose logs <service_name>
  ```

- **Database Issues**: Ensure the `DB_PASS` in your `.env` file matches the MariaDB root password. 

- **AGAIN DO NOT** store `.env` file on github as it stores sensitive information. It was stored here just for demonstration.
- **Networking**: Ensure no port conflicts and that your VPS firewall allows the necessary ports (80, 443).

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


