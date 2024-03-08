## ALX::0x10. HTTPS SSL
This project involves setting up https, creating subdomains, and configuring the server and dns accordingly.

### Usage
1) With one argument
usage: `./0-world_wide_web domain-name`

Example: `./0-world_wide_web nandgeek.tech`

**output**

`The subdomain www.nandgeek.tech is a A record and points to 162.215.226.6`
`The subdomain lb-01.nandgeek.tech is a A record and points to 54.87.3.184`
`The subdomain web-01.nandgeek.tech is a A record and points to 162.215.226.6`
`The subdomain web-02.nandgeek.tech is a A record and points to 54.237.54.104`

2) With two arguments

Usage: `./0-world_wide_web domain-name subdomain`

Example: `./0-world_wide_web nandgeek.tech web-02`

**output**

`The subdomain web-02.nandgeek.tech is a A record and points to 54.237.54.104`
