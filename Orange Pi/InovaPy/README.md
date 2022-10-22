## Instruções para configuração do main.py


Substitua a variável __receiving_ip__ pelo IP da outra Orange Pi. Para descobrir o ip de uma Orange Pi execute o seguinte comando:

```
ip a
```

Já a variável __sending_port__ pode ser qualquer porta entre 49152 e 65535, exceto a porta utilizada na __sending_port__ da outra Orange Pi.

E a variável __receiving_port__ é justamente a porta utilizada na __sending_port__ da outra Orange Pi. 