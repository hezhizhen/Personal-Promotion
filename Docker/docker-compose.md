# docker-compose

> for convenience, we replace **docker-compose** with **fig** (somehow I don't know why ... )

## Options

- `-f`: specify an alternate compose file (default is docker-compose.yml)
- `-p`: specify an alternate project name (default is directory name)
- `--verbose`: show more output
- `-v`: print version and exit
- `-H`: daemon socket to connect to
- `--tls`: use TLS; implied by `--tlsverify`

## Commands

- `ps`: list containers (4 columns: name, command, state, ports)
- `rm`: remove stopped service containers
- `up`: build, (re)create, start and attach to containers for a service (`-d`: run containers in the background and print new container names)
- `restart`: restart services
- `stop`: stop running containers without removing them
- `down`: stop containers adn remove containers, networks, volumes and images created by `up`
- `logs`: display log output from services (`-f`: follow log output)
- `pull`: pull service images
