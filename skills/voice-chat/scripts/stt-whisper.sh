#!/bin/bash
# STT - Transcribe audio using whisper-cli
# Usage: stt-whisper.sh <audio_file> [language]
# Supports: ogg, mp3, wav, m4a (auto-converts to wav for whisper)

set -euo pipefail

INPUT="$1"
LANG="${2:-zh}"
MODEL="$HOME/.whisper-models/ggml-small.bin"
TMP_WAV="/tmp/whisper_input_$$.wav"

# Convert to wav if not already
EXT="${INPUT##*.}"
if [ "$EXT" != "wav" ]; then
  ffmpeg -i "$INPUT" -ar 16000 -ac 1 "$TMP_WAV" -y 2>/dev/null
  WHISPER_INPUT="$TMP_WAV"
else
  WHISPER_INPUT="$INPUT"
fi

# Transcribe
RESULT=$(whisper-cli -m "$MODEL" -l "$LANG" -f "$WHISPER_INPUT" --no-timestamps 2>/dev/null)

# Cleanup
[ -f "$TMP_WAV" ] && rm -f "$TMP_WAV"

echo "$RESULT"
