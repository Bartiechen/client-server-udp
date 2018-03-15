## Tutorial: Comunicação Cliente-Servidor via UDP
Retorna uma aposta gerada randomicamente pelo servidor do campeão da copa do mundo de 2018.
Realizada na Russia

## Python
Sistema foi desenvolvido usando Python, então será necessário ter o interpretador instalado em seu sistema, para verificar digite Python no terminal.
Deverá aparecer algo como o abaixo.

    Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
    [GCC 5.4.0 20160609] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

## Servidor
Para ser executado o cliente é necessário que o servidor já esteja ativo. Para isso é deve-se entrar na pasta onde estão os arquivos e digitar no terminal.

    python server.py SEU_IP

Depois de feito isso hora de executar o cliente.

## Cliente
Para executar o cliente utilize o script client.py da pasta. Digitando no terminal o seguinte comando.

    python client.py IP_DO_SERVIDOR

Este linha de comando retornará a aposta que o servidor gerou.
