# netspresso/cli/commands.py

import click
from netspresso.api.cloudflare import list_zones, create_dns_record, delete_dns_record
from netspresso.ssh.tunnel import SSHTunnelManager

# Comando principal de la CLI
@click.group()
def cli():
    """Netspresso CLI - Gestiona tus túneles SSH y DNS en Cloudflare."""
    pass

# Comando para listar zonas de Cloudflare
@cli.command()
def list_zones_cmd():
    data = list_zones()
    if data['result']:  # Verifica si el arreglo 'result' contiene elementos
        for zone in data['result']:
            click.echo(f"ID: {zone['id']}, Name: {zone['name']}, Status: {zone['status']}")
    else:
        click.echo("No se encontraron zonas DNS.")

# Comando para crear un registro DNS
@cli.command()
@click.argument('zone_id')
@click.argument('record_type')
@click.argument('name')
@click.argument('content')
def create_record(zone_id, record_type, name, content):
    """Crear un registro DNS en una zona específica."""
    response = create_dns_record(zone_id, record_type, name, content)
    click.echo(f"Registro DNS creado: {response}")

# Comando para eliminar un registro DNS
@cli.command()
@click.argument('zone_id')
@click.argument('record_id')
def delete_record(zone_id, record_id):
    """Eliminar un registro DNS de una zona específica."""
    response = delete_dns_record(zone_id, record_id)
    click.echo(f"Registro DNS eliminado: {response}")

# Comando para gestionar un túnel SSH
@cli.command()
@click.argument('local_port', type=int)
@click.argument('remote_host')
@click.argument('remote_port', type=int)
def manage_tunnel(local_port, remote_host, remote_port):
    """Gestionar un túnel SSH."""
    # Suponiendo que tienes una forma de obtener estas configuraciones
    host = "tu_servidor_ssh.com"
    port = 22
    username = "tu_usuario"
    key_file = "/ruta/a/tu/llave/privada"

    tunnel_manager = SSHTunnelManager(host, port, username, key_file)
    with tunnel_manager.tunnel(local_port, remote_host, remote_port):
        click.echo(f"Túnel SSH establecido en el puerto local {local_port}.")

# Punto de entrada principal para la CLI
def main():
    cli()

if __name__ == "__main__":
    main()
