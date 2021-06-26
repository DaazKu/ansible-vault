# Vault

![Molecule](https://github.com/DaazKu/ansible-vault/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)
[![Galaxy](https://img.shields.io/badge/Galaxy-ansible__vault-informational?logo=Ansible&logoColor=848c96)](https://galaxy.ansible.com/daazku/ansible_vault)

This ansible role install Vault and expect you to **supply your own configuration templates**.

See:
- [`vault_config_template`](#vault_config_template)
- [`vault_extra_config_templates`](#vault_extra_config_templates)

Vault has MANY configuration parameters and trying to cover all of them with ansible variables makes things awfully complicated,
hard to maintain and frustrating when some options are not handled. You might also prefer to use HCL over the JSON format...
For these reasons, this role handles the installation of Vault and use your supplied configuration templates so that everyone's life is made easier!

## Role Variables

### `vault_bin_dir`
- Vault binary directory
- Default value: `/usr/local/bin`

### `vault_config_dir`
- Base configuration directory
- Default value: `/etc/vault`

### `vault_config_template`
- Path to the configuration template to use
    - **Must be supplied**
    - Resulting config will be the file name without the `.j2` extension. ie. `/some/path/config.hcl.j2` would result in `{{ vault_config_dir }}/config.hcl`

### `vault_data_dir`
- Vault data directory for local storage
  - This var is there for your convenience. `/var/lib/vault` would be appropriate here.
- Default value: `''`

### `vault_extra_config_dir`
- Extra configuration directory
- Default value: `{{ vault_config_dir }}/vault.d`

### `vault_extra_config_templates`
- Extra configuration templates to render
    - Resulting configs will be the files name without the `.j2` extension. ie. `/some/path/my-extra-config.hcl.j2` would result in `{{ vault_extra_config_dir }}/my-extra-config.hcl`
- Default value: `[]`

### `vault_group`
- Vault unix group
- Default value: `vault`

### `vault_log_dir`
- Vault log directory
  - Set to something like `/var/log/vault` if you want logs into a file instead of syslog.
- Default value: `''`

### `vault_user`
- Vault unix user
- Default value: `vault`

### `vault_version`
- Version to install
- Default value: 1.7.3
