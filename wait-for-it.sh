#!/bin/sh

# Este script aguarda o banco de dados PostgreSQL estar pronto antes de executar o Django

host="$1"
shift
cmd="$@"

until nc -z "$host" 5432; do
  echo "Aguardando o banco de dados PostgreSQL..."
  sleep 1
done

echo "Banco de dados PostgreSQL está pronto!"
exec $cmd
