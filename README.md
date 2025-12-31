### Install Docker
- Windows: https://docs.docker.com/desktop/setup/install/windows-install/
- MacOS: https://orbstack.dev/download
- Linux: https://docs.docker.com/desktop/setup/install/linux/

<br>

### Preparing
- Clone `docker/.env.example` to `docker/.env`

<br>

### Start server
- Change directory to `docker` folder
- Docker compose build and up in background
    ```bash
    docker compose up --build -d
    ```

<br>

### Result
- Check the connection with PostgreSQL
    ```
    host:       localhost
    port:       5432
    username:   pg-admin
    password:   WHnn6WhONrmRrP0HoZ38dmcrVvd1cu67
    db_name:    data-local
    ```
- Access to http://localhost:8000/api/docs to view API document
