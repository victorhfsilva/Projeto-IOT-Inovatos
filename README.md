# Projeto IOT - Inovatos Consultoria Jr.

Este repositório tem o objetivo de agrupar a informações e arquivos relacionados ao Projeto IOT da Empresa Júnior Inovatos Consultoria Jr.

Este projeto consiste em fazer a comunicação full duplex entre dois Arduinos e duas Orange Pis.

A comunicação entre estas placas acontecerá seguindo a topologia:

Arduino <---> Orange Pi <---> Orange Pi <---> Arduino

## Instalação do Armbian nas Orange Pis

O Sistema Operacional utilizado nas Orange Pis foi o Armbian 5.90 Ubuntu Bionic disponível em https://armbian.systemonachip.net/archive/orangepizeroplus2-h5/archive/.

Para instalar este sistema operacional, primeiramente faça login utilizando o usuário e senha padrão (root, 1234).

Após criar um novo usuário, conecte-se a rede Wi-Fi utilizando o comando:

```
sudo nmtui-connect
```

Em seguida, atualize o sistema operacional com:
```
sudo apt update;
sudo apt upgrade;
```
Por fim, instale o Armbian no cartão SD utilizando o assistente gráfico através do comando:
```
sudo armbian-config
```

## Habilitando o Protocolo I2C nas placas

No assistente gráfico habilite as funções
i2c0, i2c1, i2c2 nas configurações de hardware.

Em seguida instale os seguintes pacotes:
```
sudo apt install python-smbus python-dev;
sudo apt install i2c-tools;
sudo apt install libi2c-dev;
```
Inclua a linha __i2c-dev__ em __/etc/modules__ utilizando o comando:
```
sudo nano /etc/modules
```
ou utilizando qualquer outro editor de texto.

Para detectar todos os dispositivos conectados aos pinos i2c execute:
```
i2cdetect -y <I2CBUS>
```
Exemplo:
```
i2cdetect -y 0
```