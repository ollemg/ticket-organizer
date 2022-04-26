from pyotrs import Client

client = Client("https://centraldeservicos.interop.com.br/otrs/index.pl", "gabriel.barbosa", "WanrltwaezI.7")
client.session_create()
client.ticket_get_by_id(96475)