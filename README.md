## Introduction Netspresso
Welcome to the Netspresso project! This innovative tool automates the exposure of services on the internet, leveraging Python, Cloudflare, and the 'sish' library for efficient tunneling.

## Project Participants
- **Sergio Conejero**: DevOps engineer, skilled in Docker, Kubernetes, GCP, scripting, and networks.
- **Edgar Espinosa**: Junior developer and data analyst, focused on Python and Java.
- **Esteban Escobar**: Frontend developer, experienced in Python, JavaScript, TypeScript, NodeJs, VueJs.


### Cloudflare Module
#### Description
Python module for managing Cloudflare streamlines interactions with its API, enabling automated, programmatic operations like zone listing and DNS record management. It simplifies Cloudflare resource administration through user-friendly Python commands, enhancing efficiency and accessibility for developers working with Cloudflare services


### Sish Module
#### Description
'sish' is an open-source alternative to tools like serveo and ngrok, designed for secure tunneling. It facilitates exposing local servers to the internet, often used in development and testing. It's highly configurable, supporting SSH and HTTP(S) protocols, and can be deployed using Docker


### Project Structure

```
# Netspresso Project
netspresso/
│
├── cloudflare/
│ ├── cloudflare/
│ │ ├── init.py
│ │ └── cloudflare.py
│ │
│ ├── tests/
│ │ └── test_cloudflare.py
│ │
│ ├── .env
│ └── requirements.txt
└── sish-lib
├── docker-server-test/
```


### Netspresso server configuration
#### Prerequisites
- Have a own domain (example.com)
- Link domain with Cloudflare


#### Requirements
- Docker
- Docker compose
- Python 3.6+
- Pip (Python package manager)

#### Server Installation
0. Create on-premise or cloud server with nat with public ip.
1. Clone the repository in the server: `git clone [https://github.com/sixpidevs/treexpi-netspresso]`
2. Navigate to the project directory: `cd sish-lib`
3. Create ssh server running the docker image

    - ```bash
      docker run -itd --name sish \
        -v ~/sish/ssl:/ssl \
        -v ~/sish/keys:/keys \
        -v ~/sish/pubkeys:/pubkeys \
        --net=host antoniomika/sish:latest \
        --ssh-address=:22 \
        --http-address=:80 \
        --https-address=:443 \
        --https=true \
        --https-certificate-directory=/ssl \
        --authentication-keys-directory=/pubkeys \
        --private-keys-directory=/keys \
        --bind-random-ports=false
      ```
4. Navigate to the project directory: `cd cloudflare`
5. Install dependencies: `pip install -r cloudflare/requirements.txt`
6. Set up the required environment variables in the `.env` file.
7. Add DNS A record in you domain to use the public ip of this server. 


### Client use
#### Prerequisites
Only ssh client

#### Exposing a Local HTTP Server
To expose a local HTTP server, run:

ssh -R 80:localhost:8080 sish@<your-netspresso-server>
```

#### Exposing a Local HTTPS Server
For a local HTTPS server:
```bash
ssh -R 443:localhost:8443 sish@<your-netspresso-server>
```

#### Custom Subdomain
To use a custom subdomain:
```bash
ssh -R yoursubdomain:80:localhost:8080 sish@<your-netspresso-server>
```

#### Listing Active Tunnels
To list all active tunnels:
```bash
ssh sish@<your-netspresso-server> -t list
```

#### Closing a Tunnel
To close a specific tunnel:
```bash
ssh sish@<your-netspresso-server> -t close <tunnel-id>
```

Replace `<your-netspresso-server>` with your sish server's address and `<tunnel-id>` with the ID of the tunnel you want to close.



## Contributions

Contributions to the project are welcome. Please make sure to follow best development practices and keep the code well documented.

## Licence

MIT
