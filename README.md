

---

# 🗣️ WhisperX Transcriber com Diarização de Falantes

Projeto para transcrição automática de áudio com **identificação dos falantes** (diarização), usando o modelo [WhisperX](https://github.com/m-bain/whisperx). Ideal para entrevistas, podcasts, reuniões e qualquer cenário com múltiplos participantes.

---

## 📌 O que este projeto faz

* Transcrição automática de áudio (áudio → texto)
* Identificação e separação dos falantes (diarização)
* Geração de arquivo `.txt` com timestamps e falantes identificados
* Suporte para execução em GPU (CUDA) para maior velocidade
* Suporte para execução em CPU, caso não tenha GPU disponível
* Compatível com múltiplos modelos WhisperX, do mais leve ao mais preciso

---

## ⚙️ Requisitos mínimos

* Python 3.8 ou superior
* PyTorch instalado (com ou sem suporte a GPU)
* CUDA instalado (apenas para uso com GPU)
* Conta gratuita no [Hugging Face](https://huggingface.co/join) para autenticação na diarização

---

## 📦 Como instalar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/whisperx-transcriber.git
cd whisperx-transcriber
```

### 2. Crie e ative um ambiente virtual

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 🔐 Autenticação Hugging Face para diarização

Para funcionar, a diarização precisa de autenticação via Hugging Face:

1. Crie uma conta gratuita em [huggingface.co/join](https://huggingface.co/join)
2. Gere um token em [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
3. Aceite os termos dos dois modelos usados e marque a opção para o token acessar outros modelos
4. No terminal, execute:

```bash
huggingface-cli login
```

5. Cole seu token quando solicitado

---

## 🚀 Executando o script principal

```bash
python main.py --audio "caminho/do/audio.mp3"
```

Por padrão, o script usará GPU (CUDA) se disponível e o modelo `large-v3`.

### Parâmetros opcionais

| Parâmetro | Descrição                                 | Valor padrão                   |
| --------- | ----------------------------------------- | ------------------------------ |
| --audio   | Caminho para o arquivo de áudio           | Obrigatório                    |
| --output  | Nome do arquivo para salvar a transcrição | `transcricao_com_falantes.txt` |

### Exemplo completo

```bash
python main.py --audio "entrevista.mp3" --output "saida.txt"
```

---

## ⚡ Usando GPU com CUDA

Para acelerar o processamento com GPU, você precisa:

* Ter uma GPU NVIDIA compatível
* Instalar o driver NVIDIA correto
* Instalar CUDA: [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)
* Instalar PyTorch compatível com sua versão CUDA

Verifique sua versão CUDA instalada com:

```bash
nvcc --version
```

Para instalar PyTorch com suporte CUDA, visite: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)
Exemplo para CUDA 11.8:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

lembre-se do pip install -r requirements.txt

---




