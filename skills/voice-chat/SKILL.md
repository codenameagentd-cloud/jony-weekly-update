---
name: voice-chat
description: Voice conversation workflow for Telegram. Use when the user sends a voice message (audio/ogg) or requests voice replies. Handles STT (Whisper) → process → TTS (Azure/ElevenLabs) → send voice message. Auto-detects language for TTS voice selection.
---

# Voice Chat

Bidirectional voice messaging: receive voice → transcribe → respond → send voice back.

## Workflow

### Inbound Voice (user sends audio)

1. Convert ogg to wav: `ffmpeg -i <input.ogg> -ar 16000 -ac 1 /tmp/voice_input.wav -y`
2. Transcribe: `whisper-cli -m ~/.whisper-models/ggml-small.bin -l zh -f /tmp/voice_input.wav --no-timestamps`
3. Process the transcribed text as a normal message
4. Generate voice reply (see Outbound below)

Or use the bundled script:
```bash
scripts/stt-whisper.sh <audio_file> [language]
```

### Outbound Voice (reply with audio)

**Language detection:**
- Chinese or mixed Chinese/English → Azure Jenny Multilingual
- Pure English → ElevenLabs Bella

**Azure TTS (Chinese/mixed):**
```bash
scripts/tts-azure.sh "<text>" /Users/agentdelta/.openclaw/workspace-jony/tts-output.mp3
```

**ElevenLabs TTS (English):**
```bash
scripts/tts-elevenlabs.sh "<text>" /Users/agentdelta/.openclaw/workspace-jony/tts-output.mp3
```

**Send to Telegram:**
```
message(action=send, asVoice=true, channel=telegram, filePath=/Users/agentdelta/.openclaw/workspace-jony/tts-output.mp3)
```

## ⚠️ Important Notes

- The built-in `tts` tool has a bug (generates 0-byte files after first call). **Always use the scripts instead.**
- Output file MUST be under `~/.openclaw/workspace/` for Telegram send to work (security restriction).
- After sending voice, reply with `NO_REPLY` to avoid duplicate text message.
- For `web_fetch` to `wttr.in`: use `exec(curl ...)` instead (blocked by sandbox).

## Trigger Rules

- User sends voice message → auto reply with voice
- User sends text → reply with text (default)
- User explicitly asks for voice → reply with voice
