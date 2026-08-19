# 🚰 Torneira Facial — Sistema Inteligente de Higienização Hospitalar

## 📌 Sobre o projeto

O **Torneira Facial** é um **projeto de Iniciação Científica** desenvolvido no curso de **Ciência de Dados e Inteligência Artificial**, com foco na aplicação de **Inteligência Artificial, Visão Computacional e Automação** na área da saúde.

A proposta consiste no desenvolvimento de um sistema inteligente capaz de identificar funcionários por meio de **reconhecimento facial** e controlar automaticamente uma torneira durante um protocolo de higienização das mãos.

O projeto integra **software e hardware**, utilizando Python, DeepFace, OpenCV, Arduino e módulo relé, além de realizar o registro dos procedimentos e a gravação em vídeo.

## 🎯 Objetivo

Desenvolver e estudar uma solução automatizada que possa auxiliar no processo de higienização das mãos em ambientes hospitalares, utilizando reconhecimento facial e automação para:

* Identificar funcionários cadastrados;
* Automatizar a abertura e o fechamento da torneira;
* Executar um protocolo de higienização;
* Registrar os procedimentos realizados;
* Gravar o processo em vídeo;
* Reduzir o desperdício de água;
* Investigar uma futura integração com sistemas hospitalares.

## ⚙️ Funcionamento

O sistema funciona através da integração:

```text
Câmera
   ↓
OpenCV
   ↓
DeepFace
   ↓
Python
   ↓
Arduino
   ↓
Relé
   ↓
Torneira
```

Quando um funcionário é identificado, o Python envia comandos ao Arduino através da comunicação serial. O Arduino controla o relé, que realiza o acionamento da torneira.

Ao mesmo tempo, o sistema registra o procedimento e realiza a gravação em vídeo.

## 🤖 Inteligência Artificial

O reconhecimento facial utiliza **DeepFace** e o modelo **FaceNet**, enquanto o **OpenCV** é responsável pela captura da câmera e detecção inicial dos rostos.

Os funcionários são cadastrados através de imagens:

```text
funcionarios/
├── Lucas/
│   └── foto.jpg
│
└── Katarina/
    └── foto.jpg
```

## 🚿 Protocolo atual

O protótipo possui um ciclo de **60 segundos**:

* 🟢 0–8 segundos: torneira aberta
* 🔴 8–50 segundos: torneira fechada
* 🟢 50–60 segundos: torneira aberta
* 🔴 Após 60 segundos: torneira fechada

## 🎥 Registro

Durante o procedimento, o sistema realiza a gravação em vídeo e gera registros dos eventos.

```text
videos/
logs/
```

Esses dados poderão futuramente ser utilizados para análises, relatórios e estudos relacionados ao processo de higienização.

## 🛠️ Tecnologias

### Software

* Python
* OpenCV
* DeepFace
* FaceNet
* TensorFlow
* PySerial

### Hardware

* Arduino
* Módulo Relé
* Webcam
* Torneira automatizada

## 🚀 Desenvolvimento futuro

Como parte da pesquisa de Iniciação Científica, estão previstas futuras etapas de desenvolvimento:

* Criação de um banco de dados estruturado;
* Cadastro de funcionários;
* Armazenamento dos procedimentos;
* Desenvolvimento de um painel de acompanhamento;
* Análise dos dados coletados;
* Estudo de integração com sistemas hospitalares;
* Aprimoramento do reconhecimento facial;
* Melhorias na segurança e proteção dos dados;
* Funcionamento do sistema sem necessidade de um notebook;
* Inicialização automática do equipamento;
* Testes e validação do protótipo.

## 🏥 Aplicação futura

A pesquisa busca estudar a viabilidade de uma solução que possa futuramente ser utilizada em ambientes hospitalares.

Uma possível arquitetura seria:

```text
Sistema Hospitalar
       ↓
Banco de Dados / API
       ↓
Sistema de Higienização
       ↓
Reconhecimento Facial
       ↓
Arduino
       ↓
Torneira
```

A integração com sistemas hospitalares será estudada durante o desenvolvimento, considerando requisitos de segurança, privacidade, proteção de dados e infraestrutura.

## ⚠️ Status

**🟢 Protótipo funcional — Projeto de Iniciação Científica em desenvolvimento**

Atualmente, o protótipo conta com:

* ✅ Reconhecimento facial
* ✅ Detecção facial
* ✅ Arduino
* ✅ Controle por relé
* ✅ Comunicação Python ↔ Arduino
* ✅ Controle automático da torneira
* ✅ Gravação de vídeo
* ✅ Registro de logs
* ✅ Protocolo automatizado

O projeto ainda está em fase de pesquisa e desenvolvimento e necessita de novas etapas de testes, validação e avaliação antes de qualquer aplicação em ambiente hospitalar real.

## 👨‍🎓 Iniciação Científica

Este projeto está sendo desenvolvido como uma **pesquisa de Iniciação Científica** no curso de **Ciência de Dados e Inteligência Artificial**, buscando aplicar conhecimentos de Inteligência Artificial, Ciência de Dados, Visão Computacional, programação e sistemas embarcados na investigação de uma solução tecnológica para um problema relacionado à saúde.

> **Reconhecer. Automatizar. Registrar. Higienizar.**

