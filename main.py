import torch
import whisperx
from whisperx.diarize import DiarizationPipeline
import argparse
from utils.diarization_utils import merge_text_diarization, save_transcription



def parse_args():
    parser = argparse.ArgumentParser(description="Transcreve áudios com identificação de falantes usando WhisperX.")
    parser.add_argument('--audio', type=str, required=True, help='Caminho para o arquivo de áudio')
    parser.add_argument('--output', type=str, default='transcricao_com_falantes.txt', help='Arquivo de saída')
    return parser.parse_args()



# Habilita desempenho otimizado para CUDA
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True


def transcribe_audio(audio_path, device="cuda"):
    model = whisperx.load_model("large-v3", device=device)
    transcription = model.transcribe(audio_path)

    if "text" in transcription:
        return transcription, transcription["text"]
    else:
        text = "".join([seg["text"] for seg in transcription.get("segments", [])])
        return transcription, text


def align_transcription(transcription, audio_path, device="cuda"):
    alignment_model, metadata = whisperx.load_align_model(
        language_code=transcription["language"],
        device=device
    )
    return whisperx.align(transcription["segments"], alignment_model, metadata, audio_path, device=device)


def diarize_audio(audio_path, device="cuda"):
    diarize_model = DiarizationPipeline(use_auth_token=True, device=device)
    return diarize_model(audio_path).to_dict(orient="records")


def main():
    args = parse_args()
    audio_file = args.audio
    output_file = args.output
    

    transcription, raw_text = transcribe_audio(audio_file)
    print("\n Transcrição bruta:")
    print(raw_text)


    aligned = align_transcription(transcription, audio_file)


    diarized_segments = diarize_audio(audio_file)


    final_result = merge_text_diarization(aligned["segments"], diarized_segments)


    print("\n Transcrição com identificação dos falantes:")
    for seg in final_result:
        print(f"[{seg['start']:.2f}s - {seg['end']:.2f}s] {seg['speaker']}: {seg['text']}")

    save_transcription(final_result, output_file)
    print(f"\n Transcrição salva em: {output_file}")


if __name__ == "__main__":
    main()
