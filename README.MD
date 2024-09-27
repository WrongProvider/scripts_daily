# Gerador de Relatórios Executivos a partir de PDFs de Postura de Segurança

Este repositório contém um script Python que processa arquivos PDF de postura de segurança, utiliza a API da OpenAI para gerar um relatório executivo e salva o resultado em um arquivo `.docx` usando um modelo pré-definido.

## Funcionalidades

- Extrai texto de relatórios PDF.
- Gera resumos executivos personalizados utilizando a API da OpenAI.
- Salva os relatórios gerados em arquivos `.docx` com base em um modelo específico.
- Suporta a geração de relatórios para múltiplos PDFs em uma única execução.

## Pré-requisitos

Antes de usar o script, você precisará:

- **Python 3.x** instalado.
- Conta na **OpenAI** e uma chave de API válida.
- Dependências instaladas listadas abaixo.

### Dependências

Instale as dependências necessárias executando:

```bash
pip install openai PyPDF2 python-docx
