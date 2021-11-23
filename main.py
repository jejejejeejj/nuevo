#!/bin/venv python3
import click 

@click.group()
def main():
	pass

@main.command()
def add():
	print('añadido')

@main.command()
def rm():
	print('eliminar')

@main.command()
def ls():
	print('contenido')

@main.command()
def table():
	print('tabla')

@main.command()
def mv():
	print('mover')

@main.command()
def edit():
	print('editar datos contactos')

@main.command()
def server():
	print('conectar server')


if __name__ == '__main__':
	main()
