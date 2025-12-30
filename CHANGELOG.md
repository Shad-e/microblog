# Changelog

All notable changes to this project will be documented in this file.

## [11.0.0] - 2025-11-16

### Added

- CI workflow file
- Docker Compose config file

## [11.1.0] - 2025-11-17

### Added

- Follower functionality

## [11.1.2] - 2025-12-17

### Added

- Adjusted first-10-minutes playbook to create appservers, loadbalancer and database
- All collaborators' SSH key added to authorized_keys.
- Implemented CD strategy

## [11.1.3] - 2025-12-29

### Added

- New security workflow to run Bandit, Trivy and Dockle
- Configured CD workflow to run the security workflow first, only deploying if the security workflow did not bring up any errors

- Updated security groups so that they are applied after virtual machines are created 
- Restricted several ports, allowing only access to internal IP-addresses

- Automated using recommended OpenSSH config in 10-first-minutes