def merge_text_diarization(transcript_segments, diarization_segments):
    """
    Combina os segmentos de transcrição com os segmentos de diarização,
    atribuindo um falante a cada trecho transcrito.
    """
    result = []
    for segment in transcript_segments:
        segment_start = segment["start"]
        segment_end = segment["end"]
        speaker = "Unknown"

        for d in diarization_segments:
            if d["start"] <= segment_start < d["end"]:
                speaker = d["speaker"]
                break

        result.append({
            "start": segment_start,
            "end": segment_end,
            "speaker": speaker,
            "text": segment["text"]
        })
    return result


def save_transcription(transcribed_segments, output_file="transcricao_com_falantes.txt"):
    """
    Salva os segmentos transcritos com identificação dos falantes em um arquivo de texto.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("🗣️ Transcrição com identificação dos falantes:\n\n")
        for seg in transcribed_segments:
            line = f"[{seg['start']:.2f}s - {seg['end']:.2f}s] {seg['speaker']}: {seg['text']}\n"
            f.write(line)
