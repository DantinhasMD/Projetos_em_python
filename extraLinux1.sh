echo "Limpando o Ambiente"
rm -rf /publico /adm /ven /sec

echo "Criar diretórios"
'''mkdir - cria diretórios'''
mkdir /publico
mkdir /adm
mkdir /ven
mkdir /sec

echo "Criar grupos"
'''groupadd - Cria o grupo'''
groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

echo "Criar usuários"
'''Criamos os usuários com useradd e já colocamos nos grupos corretos - usamos 'openssl' para usar senhas criptografadas'''
useradd carlos -m -s /bin/bash -p $(openssl passwd -crypt teste123) -G GRP_ADM
useradd maria -m -s /bin/bash -p $(openssl passwd -crypt teste123) -G GRP_ADM
useradd joao_ -m -s /bin/bash -p $(openssl passwd -crypt teste123) -G GRP_ADM

useradd debora -m -s /bin/bash -p $(openssl passwd -crypt teste123) -G GRP_VEN
useradd sebastiana -m -s /bin/bash -p $(openssl passwd -crypt teste123) -G GRP_VEN
useradd roberto -m -s /bin/bash -p $(openssl passwd -crypt Senha123) -G GRP_VEN

useradd josefina -m -s /bin/bash -p $(openssl passwd -crypt teste123) -G GRP_SEC
useradd amanda -m -s /bin/bash -p $(openssl passwd -crypt teste123) -G GRP_SEC
useradd rogerio -m -s /bin/bash -p $(openssl passwd -crypt teste123) -G GRP_SEC

echo "Permissões de diretórios"
'''chown - mudar o dono do grupo, nesse caso estamos colocando root como administrador'''
chown root:GRP_ADM /adm
chown root:GRP_VEN /ven
chown root:GRP_SEC /sec
chown root:root /publico

'''chmod - controla as permissões de acesso dos grupos'''
chmod 770 /adm
chmod 770 /ven
chmod 770 /sec
chmod 777 /publico

------------------------------------------------------------------------------
echo "Atualizando o servidor..."
apt-get update
apt-get upgrade -y
apt-get install apache2 -y
apt-get install unzip -y


echo "Baixando e copiando os arquivos da aplicação..."

cd /tmp
wget https://github.com/denilsonbonatti/linux-site-dio/archive/refs/heads/main.zip
unzip main.zip
cd linux-site-dio-main
cp -R * /var/www/html/
