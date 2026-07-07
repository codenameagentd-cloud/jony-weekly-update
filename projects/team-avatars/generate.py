#!/usr/bin/env python3
"""Generate team avatars using Gemini 2.0 Flash image generation."""

import os
import sys
import base64
from google import genai
from google.genai import types

API_KEY = "AIzaSyDqXc3N0fiAMoe3aInkcWY-Q5Mr107w_v0"
OUTPUT_DIR = os.path.expanduser("~/.openclaw/workspace-jony/projects/team-avatars/output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

client = genai.Client(api_key=API_KEY)

STYLE_PREFIX = (
    "needle-felted wool character portrait, visible individual wool fibres, "
    "handmade imperfections in the felt surface, raw handcrafted texture with tiny loose fibres, "
    "soft diffused studio lighting, shallow depth of field, solid flat colour background, "
    "centered composition, portrait crop from chest up, warm soft shadows, "
    "miniature handmade figurine aesthetic, macro photography feel"
)

PROMPTS = {
    "jony": f"{STYLE_PREFIX}, solid muted olive green background, brown bear with close-cropped short dense wool fur, small round silver-framed glasses, gentle warm closed-mouth smile, slight stubble texture on chin made of tiny wool dots, soft thoughtful eyes with a glint of warmth, head tilted very slightly to one side, one small round ear slightly folded, restrained but approachable presence, wearing a tiny knitted cream scarf",

    "lisa": f"{STYLE_PREFIX}, solid warm coral background, black-furred cat with distinctive straight-cut bangs fringe across forehead, soft expressive dark eyes with warm catchlights, small delicate gold pendant necklace, gentle knowing smile with a hint of playfulness, head tilted slightly, one paw resting near chin, soft pink inner ears visible, graceful feminine presence with quiet charm",

    "jarvis": f"{STYLE_PREFIX}, solid slate blue background, pale silver-white furred wolf with piercing ice-blue eyes made of glass beads, clearly handmade felt texture throughout, angular facial features rendered in compressed wool, small diamond-shaped felt marking on forehead, calm confident expression with the slightest upward curve at mouth corners, one ear perked up and one slightly relaxed, chunky fluffy neck wool, visible needle marks and wool fibre strands, miniature toy scale",

    "naomi": f"{STYLE_PREFIX}, solid deep teal background, auburn reddish-brown furred fox with bright vivid green eyes, short neat bob-shaped fur around face suggesting bangs, intelligent expression with a subtle asymmetric half-smile, head tilted with gentle curiosity, bushy tail tip just visible at edge, perceptive warm gaze, elegant and playful in equal measure",

    "jennie": f"{STYLE_PREFIX}, solid soft peach background, warm brown and cream-furred rabbit with long flowing ears draped softly, bright genuine warm smile, sparkling dark expressive eyes with catchlights, tiny delicate pearl drop earring accessories hanging from ears, youthful warm approachable expression, gentle and present, soft wool texture throughout",
}

def generate_avatar(name, prompt):
    print(f"Generating {name}...")
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-image-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )
        for i, part in enumerate(response.candidates[0].content.parts):
            if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                ext = part.inline_data.mime_type.split("/")[1]
                path = os.path.join(OUTPUT_DIR, f"{name}.{ext}")
                with open(path, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"  Saved: {path}")
                return path
        print(f"  No image in response for {name}")
        if response.candidates[0].content.parts:
            print(f"  Text: {response.candidates[0].content.parts[0].text[:200]}")
        return None
    except Exception as e:
        print(f"  Error: {e}")
        return None

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    if target == "all":
        for name, prompt in PROMPTS.items():
            generate_avatar(name, prompt)
    else:
        if target in PROMPTS:
            generate_avatar(target, PROMPTS[target])
        else:
            print(f"Unknown: {target}. Options: {list(PROMPTS.keys())}")
