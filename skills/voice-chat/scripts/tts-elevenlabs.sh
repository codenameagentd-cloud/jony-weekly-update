#!/bin/bash
# ElevenLabs TTS - Generate speech from text using Bella
# Usage: tts-elevenlabs.sh <text> [output_path]
# Requires: ~/.config/elevenlabs/api_key

set -euo pipefail

TEXT="$1"
OUTPUT="${2:-/Users/agentdelta/.openclaw/workspace/tts-output.mp3}"
API_KEY=$(cat ~/.config/elevenlabs/api_key)
VOICE_ID="EXAVITQu4vr4xnSDxMaL"
MODEL="eleven_multilingual_v2"

curl -s -o "$OUTPUT" \
  -X POST "https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}" \
  -H "xi-api-key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"${TEXT}\", \"model_id\": \"${MODEL}\", \"voice_settings\": {\"stability\": 0.5, \"similarity_boost\": 0.75}}"

SIZE=$(stat -f%z "$OUTPUT" 2>/dev/null || stat -c%s "$OUTPUT" 2>/dev/null)
if [ "$SIZE" -eq 0 ]; then
  echo "ERROR: Generated file is empty" >&2
  exit 1
fi

echo "$OUTPUT"
