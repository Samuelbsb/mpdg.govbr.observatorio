mpdg.govbr.observatorio: observatorio
====================================
[![Coverage Status](https://coveralls.io/repos/github/Samuelbsb/mpdg.govbr.observatorio/badge.svg?branch=master)](https://coveralls.io/github/Samuelbsb/mpdg.govbr.observatorio?branch=master) [![Build Status](https://travis-ci.org/Samuelbsb/mpdg.govbr.observatorio.svg?branch=master)](https://travis-ci.org/Samuelbsb/mpdg.govbr.observatorio)

Introdução
-----------

Este pacote provê um conjunto de funcionalidades para gerenciar mensagens do Fale Conosco do portal. Dentre as principais:

- Confirmação da mensagem através de token enviado por email;
- Painel administrativo para gerenciamento das mensagens;
- Busca simples e avançada;
- Possibilidade de encaminhar a mensagem para usuários responsáveis por outros setores;
- Categorização e arquivamento de mensagens;
- Estatísticas de mensagens respondidas, em aberto, em atraso e alerta;
- Mensagens de notificação de email customizadas;

Compatibilidade
---------------

O pacote foi testado em versões do Plone 4.x

Instalação
------------

Para habilitar a instalação deste produto em um ambiente que utilize o
buildout:

1. Editar o arquivo buildout.cfg (ou outro arquivo de configuração) e
   adicionar o pacote `mpdg.govbr.observatorio` à lista de eggs da instalação:

        [buildout]
        ...
        eggs =
            mpdg.govbr.observatorio

2. Após alterar o arquivo de configuração é necessário executar
   ''bin/buildout'', que atualizará sua instalação.

3. Reinicie o Plone

4. Acesse o painel de controle e instale o produto
**mpdg.govbr.observatorio: observatorio**.

Estado deste pacote
---------------------

O **mpdg.govbr.observatorio** está em constante atualização e está em sua primeira versão estável aberta. O pacote ainda não possui testes automatizados mas estamos trabalhando para aumentar sua cobertura de testes e assim fornecer uma experiência ainda melhor. Você está convidado a ajudar!

Uso
---

Após instalação, será criado dentro da pasta "/sobre"  uma pasta chamada "observatorio" (/seu-site/sobre/observatorio), essa pasta é o local onde será salvo todo o conteudo do observatorio.

Para escrever uma boa prática, disponível em "/seu-site/sobre/observatorio" na view  "@@nova-boa-pratica" basta preencher os campos solicitado ,também pode ser adicionado quantos anexos o usuário quiser pelo upload de arquivos e imagens.

Após o envio da prática o administrador do site (definido na configuração do observatorio) será alertado por email,analisar a prática pendente e ter sua decisão, após a decisão o usuário será notificado (pratica aprovada,rejeitada) ,será enviado automaticamente  um email com a decisão do administrador para o email fornecido no momento do contato .

Se o usário Comentar a boa prática  será usado o mesmo procedimento de notificação/aprovação/rejeição  de email do exemplo acima .

Na instalação do produto é criado um portlet de navegação com link para "Praticas Pendentes" 

A Práticas Pendentes do observatório é acessível apenas para os usuários que estiverem no grupo de  "administrador / editor" do site  .

Também para as mensagens parametrizadas poderá ser  configuradas em "mpdg.govbr.observatorio: Observatório" . 


