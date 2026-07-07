#!/bin/bash
# Azure TTS - Generate speech from text using Jenny Multilingual
# Usage: tts-azure.sh <text> [output_path]
# Requires: ~/.config/azure-speech/api_key

set -euo pipefail

TEXT="$1"
OUTPUT="${2:-/Users/agentdelta/.openclaw/workspace-jony/tts-output.mp3}"
API_KEY=$(cat ~/.config/azure-speech/api_key)
REGION="eastasia"
VOICE="en-GB-OllieMultilingualNeural"

curl -s -o "$OUTPUT" \
  -X POST "https://${REGION}.tts.speech.microsoft.com/cognitiveservices/v1" \
  -H "Ocp-Apim-Subscription-Key: $API_KEY" \
  -H "Content-Type: application/ssml+xml" \
  -H "X-Microsoft-OutputFormat: audio-16khz-128kbitrate-mono-mp3" \
  -d "<speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xml:lang=\"zh-TW\"><voice name=\"${VOICE}\">${TEXT}</voice></speak>"

SIZE=$(stat -f%z "$OUTPUT" 2>/dev/null || stat -c%s "$OUTPUT" 2>/dev/null)
if [ "$SIZE" -eq 0 ]; then
  echo "ERROR: Generated file is empty" >&2
  exit 1
fi

echo "$OUTPUT"
