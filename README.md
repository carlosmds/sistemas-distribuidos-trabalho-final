# rmi-tolerancia-falhas

Alunos: Carlos Medeiros e Matheus da Fonseca

Implementação simples de uma Interface de Objetos Remotos (RMI) que usa replicação para ser tolerante a falhas.

## Run

Para rodar os scripts é necessário ter instalado o Docker em um sistema operacional Linux. 

- ./server.sh - Instancia um novo servidor para o sistema. Pode ser executado múltiplas vezes para instanciar multiplos servidores.
- ./client.sh - Inicia uma inteface cliente descrita abaixo

## Uso do módulo cliente

Escolha uma das opções desejadas do menu:

- 1 - Fazer "echo" de menssagem
- 2 - Listar todas as mensagens
- 0 - Sair da aplicação