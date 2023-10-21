# Ambiente Virtual (Virtual Invironment - VENV) e Alguns Comandos pip


"O módulo venv oferece suporte à criação de “ambientes virtuais” leves, cada um com 
seu próprio conjunto independente de pacotes Python instalados em seus diretórios site. 
Um ambiente virtual é criado sobre uma instalação existente do Python, conhecido como o 
Python “base” do ambiente virtual, e pode, opcionalmente, ser isolado dos pacotes no 
ambiente base, de modo que apenas aqueles explicitamente instalados no ambiente virtual 
estejam disponíveis."
Fonte: https://docs.python.org/pt-br/3/library/venv.html

### Criando ambiente virtuais

Para criação de um ambiente virtual, você precisa abrir pelo terminal o diretório do 
projeto onde ele será instalado, e depois  usar o comando python -m venv 'definir_nome'.


Depois de criado, você pode ativar e desativar. Para isso será necessário colocar 
no terminal o caminho até o script activate no diretório Scripts dentro do diretório
do ambiente virtual.

Exemplo ativando: 
     venv\Scripts\activate

### COMANDOS IMPORTANTE:

- Para desativar ambiente virtual usar comando: deactivate
- Para atualizar o pacote pip: python.exe -m pip install --upgrade pip
- Para instalar bibliotecas: pip install 'name'
- Para listar os pacotes/lib instalados: pip freeze
- Para verificar todas versões de um pacote/lib: pip index version 'name'
- Para instalar uma versão especifica do pacote\lib: pip install 'name'=='vesão'
- Para atualizar o pacote/lib: pip install 'name' --upgrade
- Para criar o requirements: pip freeze > 'nome'.txt
- Para carregar o requirements: pip freeze -r 'caminho_arquivo'
- Para desinstal um pacote\lib: pip uninstall 'nome' -y
