# Torneira Facial: Sistema Automatizado de Higienização Hospitalar

Projeto de Iniciação Científica desenvolvido no curso de Ciência de Dados e Inteligência Artificial, focado na aplicação de visão computacional, automação e sistemas embarcados para o controle de fluxos de higienização em ambientes de saúde.

---

## Sobre o Projeto

O sistema consiste em uma solução integrada de software e hardware capaz de identificar funcionários cadastrados por meio de reconhecimento facial e acionar automaticamente uma torneira durante o protocolo padrão de lavagem das mãos.

Além da automação do fluxo de água, a aplicação realiza o registro temporal dos procedimentos e a gravação em vídeo para fins de auditoria e análise posterior.

---

## Arquitetura e Funcionamento

O fluxo de execução integra processamento de imagem em tempo real e comunicação serial com microcontroladores:

```text
[Câmera] 
   ↓ 
[OpenCV] 
   ↓ 
[DeepFace / FaceNet] 
   ↓ 
[Python (PySerial)] 
   ↓ 
[Arduino] 
   ↓ 
[Módulo Relé] 
   ↓ 
[Torneira Automatizada]

```

1. **Captura e Detecção:** O OpenCV captura os quadros da webcam e realiza a detecção inicial de rostos.
2. **Identificação:** O DeepFace (utilizando o modelo FaceNet) compara a face detectada com a base de dados local (`funcionarios/`).
3. **Comunicação:** Ao confirmar a identidade do funcionário, o script em Python envia um comando via porta serial (`PySerial`) para o Arduino.
4. **Atuação:** O Arduino aciona o módulo relé, abrindo ou fechando o fluxo da torneira conforme o protocolo estabelecido.
5. **Registro:** Paralelamente, o sistema armazena logs textuais (`logs/`) e grava o procedimento em vídeo (`videos/`).

---

## Estrutura do Diretório de Cadastros

```text
funcionarios/
├── Lucas/
│   └── foto.jpg
└── Katarina/
    └── foto.jpg

```

---

## Protocolo de Higienização

O protótipo opera atualmente com um ciclo padrão de 60 segundos estruturado da seguinte forma:

* **00s – 08s:** Torneira aberta (molhagem inicial e aplicação de sabonete)
* **08s – 50s:** Torneira fechada (fricção e esfregamento das mãos)
* **50s – 60s:** Torneira aberta (enxágue)
* **Após 60s:** Torneira fechada (fim do ciclo)

---

## Stack Tecnológica

### Software

* **Python** (Linguagem principal)
* **OpenCV** (Captura de vídeo e processamento de imagem)
* **DeepFace & FaceNet** (Extração de características e reconhecimento facial)
* **TensorFlow** (Backend para os modelos de aprendizado de máquina)
* **PySerial** (Comunicação serial com o microcontrolador)

### Hardware

* **Arduino** (Unidade microcontrolada)
* **Módulo Relé** (Chaveamento elétrico para a válvula/torneira)
* **Webcam** (Dispositivo de captura visual)
* **Torneira automatizada** (Atuador hidráulico)

---

## Próximas Etapas de Pesquisa

Como parte do cronograma da Iniciação Científica, estão previstas as seguintes melhorias:

* Migração para um banco de dados estruturado.
* Implementação de uma interface para cadastro e gerenciamento de funcionários.
* Desenvolvimento de um painel analítico para acompanhamento dos dados coletados.
* Estudo de viabilidade para integração com prontuários e sistemas hospitalares (sob normas de segurança e LGPD).
* Otimização do pipeline para execução autônoma (sem necessidade de um computador conectado).

---

## Status do Projeto

**Protótipo Funcional** — Em fase de testes de bancada e validação de engenharia.

* Reconhecimento e detecção facial operacionais.
* Comunicação Python–Arduino estável via relé.
* Ciclo de temporização e rotinas de log/vídeo implementados.
